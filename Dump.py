from resanal.models import Fetch,Result
import xlrd

book = xlrd.open_workbook('2016_6th.xlsx')
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
    s.sem = 6
    s.section = first_sheet.cell_value(i,1)
    s.batch = 2016
    s.save()
    s1 = Fetch()
    s2 = Fetch()
    s3 = Fetch()
    s4 = Fetch()
    s5 = Fetch()
    s6 = Fetch()
    s7 = Fetch()
    s8 = Fetch()
    s9 = Fetch()
    s10 = Fetch()
    s11 = Fetch()
    #sub1
    s1.usn = s
    s1.subcode = "15CS61"
    s1.subname = "CRYPTOGRAPHY, NETWORK SECURITY AND CYBER LAW"
    s1.intmarks = first_sheet.cell_value(i,3)
    s1.extmarks = first_sheet.cell_value(i,4)
    s1.totalmarks = first_sheet.cell_value(i,5)
    s1.save()
    #sub2
    s2.usn = s
    s2.subcode = "15CS62"
    s2.subname = "COMPUTER GRAPHICS AND VISUALIZATION"
    s2.intmarks = first_sheet.cell_value(i,7)
    s2.extmarks = first_sheet.cell_value(i,8)
    s2.totalmarks = first_sheet.cell_value(i,9)
    s2.save()
    #sub3
    s3.usn = s
    s3.subcode = "15CS63"
    s3.subname = "SYSTEM SOFTWARE AND COMPILER DESIGN"
    s3.intmarks = first_sheet.cell_value(i,11)
    s3.extmarks = first_sheet.cell_value(i,12)
    s3.totalmarks = first_sheet.cell_value(i,13)
    s3.save()
    #sub4
    s4.usn = s
    s4.subcode = "15CS64"
    s4.subname = "OPERATING SYSTEMS"
    s4.intmarks = first_sheet.cell_value(i,15)
    s4.extmarks = first_sheet.cell_value(i,16)
    s4.totalmarks = first_sheet.cell_value(i,17)
    s4.save()
    #sub5
    s5.usn = s
    s5.subcode = "15CSL67"
    s5.subname = "SYSTEM SOFTWARE & OPERATING SYSTEM LAB"
    s5.intmarks = first_sheet.cell_value(i,19)
    s5.extmarks = first_sheet.cell_value(i,20)
    s5.totalmarks = first_sheet.cell_value(i,21)
    s5.save()
    #sub6
    s6.usn = s
    s6.subcode = "15CSL68"
    s6.subname = "COMP. GRAPHICS LABORATORY WITH MINI PROJECT"
    s6.intmarks = first_sheet.cell_value(i,23)
    s6.extmarks = first_sheet.cell_value(i,24)
    s6.totalmarks = first_sheet.cell_value(i,25)
    s6.save()
    #sub7 
    s7.usn = s
    s7.subcode = "15CS651"
    s7.subname = "DATA MINING AND DATA WAREHOUSING"
    s7.intmarks = first_sheet.cell_value(i,27)
    s7.extmarks = first_sheet.cell_value(i,28)
    s7.totalmarks = first_sheet.cell_value(i,29)
    if first_sheet.cell_value(i,30) != '-':
        s7.save()
    #sub8
    s8.usn = s
    s8.subcode = "15CS653"
    s8.subname = "Operation Research"
    s8.intmarks = first_sheet.cell_value(i,31)
    s8.extmarks = first_sheet.cell_value(i,32)
    s8.totalmarks = first_sheet.cell_value(i,33)
    if first_sheet.cell_value(i,34) != '-':
        s8.save()
    #sub9
    s9.usn = s
    s9.subcode = "15CS664"
    s9.subname = "PYTHON APPLICATION PROGRAMMING"
    s9.intmarks = first_sheet.cell_value(i,35)
    s9.extmarks = first_sheet.cell_value(i,36)
    s9.totalmarks = first_sheet.cell_value(i,37)
    if first_sheet.cell_value(i,38) != '-':
        s9.save() 
    #sub10
    s10.usn = s
    s10.subcode = "15IM663"
    s10.subname = "Value engineering"
    s10.intmarks = first_sheet.cell_value(i,39)
    s10.extmarks = first_sheet.cell_value(i,40)
    s10.totalmarks = first_sheet.cell_value(i,41)
    if first_sheet.cell_value(i,42) != '-':
        s10.save()  
    #sub11
    s11.usn = s
    s11.subcode = "15MAT661"
    s11.subname = "Linear Algebra"
    s11.intmarks = first_sheet.cell_value(i,43)
    s11.extmarks = first_sheet.cell_value(i,44)
    s11.totalmarks = first_sheet.cell_value(i,45)
    if first_sheet.cell_value(i,46) != '-':
        s11.save()
    i = i+1
print('Done')
