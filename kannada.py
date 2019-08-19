from resanal.models import Fetch,Result
import xlrd

book = xlrd.open_workbook('3rd sem-2017batch.xlsx')
first_sheet = book.sheet_by_index(0)
#print(first_sheet.cell_value(0,0))
i = 2

while True:
    if first_sheet.cell_value(i,0) == "end":
        break
    print("USN:-"+first_sheet.cell_value(i,0))
    s = Result.objects.filter(usn=first_sheet.cell_value(i,0),sem=3)[0]
    s1 = Fetch()
    s1.usn = s
    s1.subcode = "17KKX39"
    s1.subname = "KANNADA"
    s1.intmarks = first_sheet.cell_value(i,35)
    s1.extmarks = first_sheet.cell_value(i,36)
    s1.totalmarks = first_sheet.cell_value(i,37)
    grade = 0
    fcd = "F"
    if  first_sheet.cell_value(i,38) == "P":
        grade = 10
        fcd = "FCD"
    s1.grade = grade
    s1.FCD = fcd
    s1.save()
    i = i+1
print('Done')
    
