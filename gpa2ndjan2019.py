from resanal.models import Result,Fetch

for i in Result.objects.filter(batch="2018"):
    print(i.usn)
    totalgrade = 0
    gpa = 0
    roundoff = 0
    for j in i.maping.all():
        if j.subcode=="18EGH18":
                totalgrade += j.grade*1
        if j.subcode=="18MAT21":
                totalgrade += j.grade*4
        if j.subcode=="18CHE22":
                totalgrade += j.grade*4
        if j.subcode=="18CPS23":
                totalgrade += j.grade*3
        if j.subcode=="18ELN24":
                totalgrade += j.grade*3
        if j.subcode=="18ME25":
                totalgrade += j.grade*3
        if j.subcode=="18CHEL26":
                totalgrade += j.grade*1
        if j.subcode=="18CPL27":
                totalgrade += j.grade*1
    gpa = (totalgrade/200)*10
    roundoff = round(gpa,2)
    i.gpa = roundoff
    i.save()