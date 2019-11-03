from resanal.models import Fetch,Result
import xlrd

book = xlrd.open_workbook('20158th.xlsx')
first_sheet = book.sheet_by_index(0)
i = 2
while True:
    if first_sheet.cell_value(i,0) == "end":
        break
    print("USN:-"+first_sheet.cell_value(i,0))
    s = Result()
    s.name = first_sheet.cell_value(i,2)
    s.usn = first_sheet.cell_value(i,0)
    s.sem = 8
    s.section = first_sheet.cell_value(i,1)
    s.batch = 2015
    s.save()
    s1 = Fetch()
    s2 = Fetch()
    s3 = Fetch()
    s4 = Fetch()
    s5 = Fetch()
    #sub1
    s1.usn = s
    s1.subcode = "15CS81"
    s1.subname = "INTERNET OF THINGS AND APPLICATIONS"
    s1.intmarks = first_sheet.cell_value(i,3)
    s1.extmarks = first_sheet.cell_value(i,4)
    s1.totalmarks = first_sheet.cell_value(i,5)
    s1.save()
    #sub2
    s2.usn = s
    s2.subcode = "15CS82"
    s2.subname = "BIG DATA ANALYTICS"
    s2.intmarks = first_sheet.cell_value(i,7)
    s2.extmarks = first_sheet.cell_value(i,8)
    s2.totalmarks = first_sheet.cell_value(i,9)
    s2.save()
    #sub3
    s3.usn = s
    s3.subcode = "15CS84"
    s3.subname = "INTERNSHIP/PROFESSIONAL PRACTICE"
    s3.intmarks = first_sheet.cell_value(i,11)
    s3.extmarks = first_sheet.cell_value(i,12)
    s3.totalmarks = first_sheet.cell_value(i,13)
    s3.save()
    #sub4
    s4.usn = s
    s4.subcode = "15CSP85"
    s4.subname = "PROJECT WORK PHASE II"
    s4.intmarks = first_sheet.cell_value(i,15)
    s4.extmarks = first_sheet.cell_value(i,16)
    s4.totalmarks = first_sheet.cell_value(i,17)
    s4.save()
    #sub5
    s5.usn = s
    s5.subcode = "15CSS86"
    s5.subname = "SEMINAR"
    s5.intmarks = first_sheet.cell_value(i,19)
    s5.extmarks = first_sheet.cell_value(i,20)
    s5.totalmarks = first_sheet.cell_value(i,21)
    s5.save()
    i = i+1
print('Done')
