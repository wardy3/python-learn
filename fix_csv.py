import argparse
import csv
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
parser.add_argument('--in-delimiter', default='|')
parser.add_argument('--in-quote', default='"')
parser.add_argument('--out-delimiter', default=',')
parser.add_argument('--out-quote', default='"')
args = parser.parse_args(sys.argv[1:])

# print(args)

# old_csv, new_csv = sys.argv[1:3]

with open(
        args.input, newline='') as in_fh, open(
            args.output, 'w', newline='') as out_fh:

    dialect = csv.Sniffer().sniff(in_fh.read(1024))
    in_fh.seek(0)
    print(f"del {dialect.delimiter} q {dialect.doublequote} "
          f"esc {dialect.escapechar} term {dialect.lineterminator}")

    reader = csv.reader(
        in_fh,
        delimiter=args.in_delimiter,
        quotechar=args.in_quote,
        dialect=dialect)
    writer = csv.writer(
        out_fh, delimiter=args.out_delimiter, quotechar=args.out_quote)

    # for row in reader:
    # writer.writerow(row)

    writer.writerows(reader)

print(Path(args.output).read_text())