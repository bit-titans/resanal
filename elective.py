from resanal.models import Fetch,Result
import xlrd

book = xlrd.open_workbook('20158th.xlsx')
first_sheet = book.sheet_by_index(2)
i = 2

while True:
    if first_sheet.cell_value(i,0) == "end":
        break
    print("USN:-"+first_sheet.cell_value(i,0))
    s = Result.objects.filter(usn=first_sheet.cell_value(i,0),sem=8)[0]
    s1 = Fetch()
    s1.usn = s
    s1.subcode = first_sheet.cell_value(i,3)
    if s1.subcode == "15CS834":
        s1.subname = "SYSTEM MODELING AND SIMULATION"
    elif s1.subcode == "15CS832":
         s1.subname = "MODERN INTERFACE DESIGN"
    s1.intmarks = first_sheet.cell_value(i,4)
    s1.extmarks = first_sheet.cell_value(i,5)
    s1.totalmarks = first_sheet.cell_value(i,6)
    s1.save()
    i = i+1
print('Done')
    
