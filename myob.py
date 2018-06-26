import csv
from datetime import datetime
import re
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Set up Tab-separated output characteristics

csv.register_dialect('myob', lineterminator='\r', delimiter='\t')

# class myob(csv.Dialect):
# lineterminator = '\r'


with open('myob-export', 'w', newline='') as importfile:
    # Import header
    fieldnames = ['Cheque Account', 'Cheque #', 'Date', 'Inclusive', 'Co./Last Name',
                  'Addr 1 - Line 1', 'Memo', 'Allocation Account #', 'Ex-Tax Amount', 'Inc-Tax Amount', 'Tax Code']

    # myob_dialect = myob()
    writer = csv.DictWriter(
        importfile, fieldnames=fieldnames, dialect='myob')
    writer.writeheader()

    with open('myob.tsv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, dialect='excel-tab')

        for row in reader:
            # pp.pprint(row)

            from_ac, date, company, memo, alloc_ac, amount_inc, tax_code, manual = [
                row[field] for field in ('MYOB a/c', 'Date', 'Narrative', 'Memo', 'alloc a/c', 'Debit Amount', 'tax code', 'manual')]

            # Skip some rows
            if memo == 'Ignore - other half':
                continue
            elif manual == 'Y':
                continue

            # Tidy some formatting
            # XXX print(f"got amount as <{amount_inc}> ", end='')
            amount_inc_no_punc = re.sub(r'[^0-9.]', '', amount_inc)
            # XXX print(f"after no punc amount is <{amount_inc_no_punc}>")

            if amount_inc_no_punc == '':
                amount_inc_no_punc = '0'

            # XXX print(f"turning <{amount_inc}> ", end='')
            amount_inc_format = format(float(amount_inc_no_punc), '08.2f')
            # XXX print(f"into <{amount_inc_format}>")

            # Calculate fields not in bank export
            date_obj = datetime.strptime(date, r'%d/%m/%y')
            yymmdd = date_obj.strftime(r'%y%m%d')

            chqnum = 'd' + yymmdd + 'a' + amount_inc_format.replace('.', '')

            if tax_code == 'GST':
                amount_ex = float(amount_inc_no_punc) * 10 / 11
                amount_ex = format(amount_ex, '.2f')
            elif tax_code in ('N-T', 'FRE', 'INP'):
                amount_ex = amount_inc_no_punc
            else:
                pp.pprint(row)
                sys.exit(f"Tax code {tax_code}")

            writer.writerow({'Cheque Account': from_ac, 'Cheque #': chqnum, 'Date': date,
                             'Inclusive': 'X', 'Co./Last Name': '', 'Addr 1 - Line 1': company, 'Memo': memo, 'Allocation Account #': '', 'Ex-Tax Amount': amount_inc_no_punc, 'Inc-Tax Amount': amount_inc_no_punc, 'Tax Code': ''})
            writer.writerow({'Cheque Account': '', 'Cheque #': chqnum, 'Date': date,
                             'Inclusive': 'X', 'Co./Last Name': '', 'Addr 1 - Line 1': company, 'Memo': memo, 'Allocation Account #': alloc_ac, 'Ex-Tax Amount': amount_ex, 'Inc-Tax Amount': amount_inc_no_punc, 'Tax Code': tax_code})

print("\n\nAll done")
