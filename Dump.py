from resanal.models import Fetch,Result
import xlrd

book = xlrd.open_workbook('2017_4th_DIP.xlsx')
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
    s.sem = 4
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
    s8 = Fetch()
    #sub1
    s1.usn = s
    s1.subcode = "17MAT41"
    s1.subname = "ENGINEERING MATHEMATICS - IV"
    s1.intmarks = first_sheet.cell_value(i,3)
    s1.extmarks = first_sheet.cell_value(i,4)
    s1.totalmarks = first_sheet.cell_value(i,5)
    s1.save()
    #sub2
    s2.usn = s
    s2.subcode = "17CS42"
    s2.subname = "OBJECT ORIENTED CONCEPTS"
    s2.intmarks = first_sheet.cell_value(i,7)
    s2.extmarks = first_sheet.cell_value(i,8)
    s2.totalmarks = first_sheet.cell_value(i,9)
    s2.save()
    #sub3
    s3.usn = s
    s3.subcode = "17CS43"
    s3.subname = "DESIGN AND ANALYSIS OF ALGORITHMS"
    s3.intmarks = first_sheet.cell_value(i,11)
    s3.extmarks = first_sheet.cell_value(i,12)
    s3.totalmarks = first_sheet.cell_value(i,13)
    s3.save()
    #sub4
    s4.usn = s
    s4.subcode = "17CS44"
    s4.subname = "MICROPROCESSORS AND MICROCONTROLLERS"
    s4.intmarks = first_sheet.cell_value(i,15)
    s4.extmarks = first_sheet.cell_value(i,16)
    s4.totalmarks = first_sheet.cell_value(i,17)
    s4.save()
    #sub5
    s5.usn = s
    s5.subcode = "17CS45"
    s5.subname = "SOFTWARE ENGINEERING"
    s5.intmarks = first_sheet.cell_value(i,19)
    s5.extmarks = first_sheet.cell_value(i,20)
    s5.totalmarks = first_sheet.cell_value(i,21)
    s5.save()
    #sub6
    s6.usn = s
    s6.subcode = "17CS46"
    s6.subname = "DATA COMMUNICATION"
    s6.intmarks = first_sheet.cell_value(i,23)
    s6.extmarks = first_sheet.cell_value(i,24)
    s6.totalmarks = first_sheet.cell_value(i,25)
    s6.save()
    #sub7 
    s7.usn = s
    s7.subcode = "17CSL47"
    s7.subname = "DESIGN AND ANALYSIS OF ALGORITHMS LABORATORY"
    s7.intmarks = first_sheet.cell_value(i,27)
    s7.extmarks = first_sheet.cell_value(i,28)
    s7.totalmarks = first_sheet.cell_value(i,29)
    s7.save()
    #sub8
    s8.usn = s
    s8.subcode = "17CSL48"
    s8.subname = "MICROPROCESSORS LABORATORY"
    s8.intmarks = first_sheet.cell_value(i,31)
    s8.extmarks = first_sheet.cell_value(i,32)
    s8.totalmarks = first_sheet.cell_value(i,33)
    s8.save()  
    i = i+1
print('Done')
