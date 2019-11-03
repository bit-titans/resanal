from resanal.models import Fetch,Result
import xlrd

book = xlrd.open_workbook('20171st.xlsx')
first_sheet = book.sheet_by_index(0)
#print(first_sheet.cell_value(0,0))
i = 2
while True:
    if first_sheet.cell_value(i,0) == "end":
        break
    print("USN:-"+first_sheet.cell_value(i,0))
    s = Result()
    s.name = first_sheet.cell_value(i,2)
    s.usn = first_sheet.cell_value(i,0)
    s.sem = 1
    s.section = first_sheet.cell_value(i,1)
    s.batch = 2017
    s.save()
    s1 = Fetch()
    s2 = Fetch()
    s3 = Fetch()
    s4 = Fetch()
    s5 = Fetch()
    s6 = Fetch()
    s7 = Fetch()
    #sub1
    s1.usn = s
    s1.subcode = "17MAT11"
    s1.subname = "ENGINEERING MATHEMATICS-I"
    s1.intmarks = first_sheet.cell_value(i,3)
    s1.extmarks = first_sheet.cell_value(i,4)
    s1.totalmarks = first_sheet.cell_value(i,6)
    s1.save()
    #sub2
    s2.usn = s
    s2.subcode = "17PHY12"
    s2.subname = "ENGINEERING PHYSICS"
    s2.intmarks = first_sheet.cell_value(i,8)
    s2.extmarks = first_sheet.cell_value(i,9)
    s2.totalmarks = first_sheet.cell_value(i,11)
    s2.save()
    #sub3
    s3.usn = s
    s3.subcode = "17CIV13"
    s3.subname = "ELEMENTS OF CIVIL ENGG. & MECHANICS"
    s3.intmarks = first_sheet.cell_value(i,13)
    s3.extmarks = first_sheet.cell_value(i,14)
    s3.totalmarks = first_sheet.cell_value(i,16)
    s3.save()
    #sub4
    s4.usn = s
    s4.subcode = "17EME14"
    s4.subname = "ELEMENTS OF MECHANICAL ENGINEERING"
    s4.intmarks = first_sheet.cell_value(i,18)
    s4.extmarks = first_sheet.cell_value(i,19)
    s4.totalmarks = first_sheet.cell_value(i,21)
    s4.save()
    #sub5
    s5.usn = s
    s5.subcode = "17ELE15"
    s5.subname = "BASIC ELECTRICAL ENGINEERING"
    s5.intmarks = first_sheet.cell_value(i,23)
    s5.extmarks = first_sheet.cell_value(i,24)
    s5.totalmarks = first_sheet.cell_value(i,26)
    s5.save()
    #sub6
    s6.usn = s
    s6.subcode = "17WSL16"
    s6.subname = "WORKSHOP PRACTICE"
    s6.intmarks = first_sheet.cell_value(i,28)
    s6.extmarks = first_sheet.cell_value(i,29)
    s6.totalmarks = first_sheet.cell_value(i,31)
    s6.save()
    #sub7 
    s7.usn = s
    s7.subcode = "17PHYL17"
    s7.subname = "ENGINEERING PHYSICS LAB."
    s7.intmarks = first_sheet.cell_value(i,33)
    s7.extmarks = first_sheet.cell_value(i,34)
    s7.totalmarks = first_sheet.cell_value(i,35)
    s7.save()
    i = i+1
print('Done')
