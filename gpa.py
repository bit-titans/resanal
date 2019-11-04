from resanal.models import Result,Fetch

for i in Result.objects.filter(batch="2018",sem=1):
    print(i.usn)
    totalgrade = 0
    gpa = 0
    roundoff = 0
    for j in i.maping.all():
        if j.subcode=="18MAT11":
                totalgrade += j.grade*4
        if j.subcode=="18PHY12":
                totalgrade += j.grade*4
        if j.subcode=="18ELE13":
                totalgrade += j.grade*3
        if j.subcode=="18CIV14":
                totalgrade += j.grade*3
        if j.subcode=="18EGDL15":
                totalgrade += j.grade*3
        if j.subcode=="18PHYL16":
                totalgrade += j.grade*1
        if j.subcode=="18ELEL17":
                totalgrade += j.grade*1
        if j.subcode=="18EGH18":
                totalgrade += j.grade*1
    gpa = (totalgrade/200)*10
    roundoff = round(gpa,2)
    print(roundoff)
    i.gpa = roundoff
    i.save()