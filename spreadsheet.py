import openpyxl
import pprint

pp = pprint.PrettyPrinter(indent=4)

SHEET = 'SaaS'

MONTH_ROW = 1
DAY_ROW   = 3

PERSON_ROW_START = 5
DATA_COL_START   = 'B'

#COLOUR_ONCALL = 
book    = openpyxl.load_workbook('Annual Leave 2018.xlsx',read_only=True,data_only=True)
#sheet   = book.wb('SaaS')

sheet = book[SHEET]
#pp.pprint(sheet)

for cell_address in ('FK9', 'FL9', 'FW6'):
    cell = sheet[cell_address]
    colour = cell.fill.start_color.index
    print("Colour of %s is %s "% (cell_address,colour))