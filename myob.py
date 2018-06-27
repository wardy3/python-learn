from typing import Tuple
import csv
from datetime import datetime
from collections import defaultdict
import re
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)


def amount_as_cents(amount: str)->int:
    """ Convert variously formatted strings into cents

        >>> amount_as_cents('.12')
        12
        >>> amount_as_cents('$  1,234.56')
        123456
        >>> amount_as_cents('4.3')
        430
        >>> amount_as_cents('56')
        5600
        >>> amount_as_cents('')
        0
        >>> amount_as_cents('1.2.3')
        Traceback (most recent call last):
            ...
        ValueError: Can't recognise
    """

    # Clean up anything not a decimal
    no_punc = re.sub(r'[^0-9.]', '', amount)

    match = re.fullmatch(r'(\d*) ( [.] \d+ )?', no_punc, flags=re.VERBOSE)

    if match:
        d, c = match.groups(default='0')
        if d == '':
            d = '0'
        # print(f"got {d} dollars and {c} cents")
        c = round(float(c), 2)
        # print(f"rounded cents to {c}")
        # TODO horrible
        return int((int(d) + c) * 100)
    else:
        raise ValueError(f"Can't recognise {amount} as currency")


# Keep track of when two transactons happen on the same day
unique: dict = dict()


def generate_transaction_id(date: str, is_debit: bool, is_credit: bool)->str:
    """ Make a unique transaction ID out of the transaction date
        Prefix with a d for debit, and c for credit
    """

    assert(is_debit != is_credit)

    date_obj = datetime.strptime(date, r'%d/%m/%y')
    yymmdd = date_obj.strftime(r'%y%m%d')

    if is_debit:
        transaction_id = 'd'
    else:
        transaction_id = 'c'
    transaction_id += yymmdd

    if transaction_id in unique:
        tiebreak = unique[transaction_id]
        unique[transaction_id] += 1
        transaction_id = transaction_id + chr(tiebreak+ord('a')-1)
    else:
        unique[transaction_id] = 1

    return transaction_id


def calculate_tax(amount_inc_cents: int, tax_code: str) -> Tuple[int, int]:
    """ Given a tax inclusive amount (in cents), separate into the tax exclusive
        amount and the tax amount (both in cents)
    """
    if tax_code in ('GST'):
        amount_ex_cents = int(round(amount_inc_cents * 10 / 11, 0))
    elif tax_code in ('N-T', 'FRE', 'INP'):
        amount_ex_cents = amount_inc_cents
    else:
        sys.exit(f"Invalid Tax code {tax_code}")

    tax_amount_cents = amount_inc_cents - amount_ex_cents

    return amount_ex_cents, tax_amount_cents


def format_money(amount_cents: int)->str:
    """ Given an amount in cents (eg 5412) return a money decimal (eg 54.12)
    """
    return re.sub(r'(\d\d)$', r'.\1', str(amount_cents))


def main():

    # Set up Tab-separated output characteristics
    csv.register_dialect('myob', lineterminator='\r', delimiter='\t')

    with open('myob-spend.txt', 'w', newline='') as spendfile, open('myob-receive.txt', 'w', newline='') as receivefile:
        # Spend Money header
        spend_money = ['Cheque Account', 'Cheque #', 'Date', 'Inclusive', 'Co./Last Name',
                       'Addr 1 - Line 1', 'Memo', 'Allocation Account #', 'Ex-Tax Amount', 'Inc-Tax Amount', 'Tax Amount', 'Tax Code',
                       'Delivery Status', ]
        # Receive Money header
        receive_money = ['Deposit Account', 'ID #', 'Date', 'Inclusive', 'Co./Last Name',
                         'Allocation Memo', 'Memo', 'Allocation Account #', 'Ex-Tax Amount', 'Inc-Tax Amount', 'Tax Amount', 'Tax Code', ]

        spend_writer = csv.DictWriter(
            spendfile, fieldnames=spend_money, dialect='myob')
        spend_writer.writeheader()

        receive_writer = csv.DictWriter(
            receivefile, fieldnames=receive_money, dialect='myob')
        receive_writer.writeheader()

        with open('myob.tsv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, dialect='excel-tab')

            for row in reader:
                from_ac, date, company, memo, alloc_ac, dr_amount_inc, cr_amount_inc,  tax_code, manual = [
                    row.get(field, 'missing') for field in ('MYOB a/c', 'Date', 'Narrative', 'Memo', 'alloc a/c',
                                                            ' Debit Amount ', ' Credit Amount ', 'tax code', 'manual')]

                # Skip some rows marked as not to be processed
                if memo == 'Ignore - other half':
                    continue
                elif manual == 'Y':
                    continue

                # Tidy some formatting
                dr_amount_inc_cents = amount_as_cents(dr_amount_inc)
                cr_amount_inc_cents = amount_as_cents(cr_amount_inc)

                if dr_amount_inc_cents == 0 and cr_amount_inc_cents == 0:
                    continue

                is_debit = dr_amount_inc_cents > 0
                is_credit = cr_amount_inc_cents > 0
                assert(is_debit != is_credit)   # Can't have neither or both

                # Calculate fields not in bank export
                transaction_id = generate_transaction_id(
                    date, is_debit, is_credit)

                if is_debit:
                    amount_inc_cents = dr_amount_inc_cents
                    amount_ex_cents, tax_amount_cents = calculate_tax(
                        dr_amount_inc_cents, tax_code)
                else:
                    amount_inc_cents = cr_amount_inc_cents
                    amount_ex_cents, tax_amount_cents = calculate_tax(
                        cr_amount_inc_cents, tax_code)

                amount_inc = format_money(amount_inc_cents)
                amount_ex = format_money(amount_ex_cents)
                tax_amount = format_money(tax_amount_cents)

                if is_debit:
                    spend_writer.writerow({'Cheque Account': from_ac, 'Cheque #': transaction_id, 'Date': date,
                                           'Inclusive': 'X',  'Addr 1 - Line 1': company, 'Memo': memo,
                                           'Ex-Tax Amount': amount_inc, 'Inc-Tax Amount': amount_inc,  'Delivery Status': 'A', })
                    spend_writer.writerow({'Cheque #': transaction_id, 'Date': date,
                                           'Inclusive': 'X',  'Addr 1 - Line 1': company, 'Memo': memo, 'Allocation Account #': alloc_ac,
                                           'Ex-Tax Amount': amount_ex, 'Inc-Tax Amount': amount_inc, 'Tax Amount': tax_amount, 'Tax Code': tax_code, })
                    print('\r', end="", file=spendfile)
                else:
                    receive_writer.writerow({'Deposit Account': from_ac, 'ID #': transaction_id, 'Date': date,
                                             'Inclusive': 'X',   'Memo': memo,
                                             'Ex-Tax Amount': amount_inc, 'Inc-Tax Amount': amount_inc, })
                    receive_writer.writerow({'ID #': transaction_id, 'Date': date,
                                             'Inclusive': 'X',  'Allocation Memo': company, 'Memo': memo, 'Allocation Account #': alloc_ac,
                                             'Ex-Tax Amount': amount_ex, 'Inc-Tax Amount': amount_inc, 'Tax Amount': tax_amount, 'Tax Code': tax_code, })
                    print('\r', end="", file=receivefile)

                # TODO Look at Decimal for these figures

    print(f"All done")


if __name__ == '__main__':
    main()
