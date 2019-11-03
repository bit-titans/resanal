from resanal.models import Result,Fetch

for i in Result.objects.filter(batch="2017",sem=1):
    print(i.usn)
    totalgrade = 0
    gpa = 0
    roundoff = 0
    for j in i.maping.all():
        if j.subcode=="17MAT11":
                totalgrade += j.grade*4
        if j.subcode=="17PHY12":
                totalgrade += j.grade*4
        if j.subcode=="17CIV13":
                totalgrade += j.grade*4
        if j.subcode=="17EME14":
                totalgrade += j.grade*4
        if j.subcode=="17ELE15":
                totalgrade += j.grade*4
        if j.subcode=="17WSL16":
                totalgrade += j.grade*2
        if j.subcode=="17PHYL17":
                totalgrade += j.grade*2
    gpa = (totalgrade/240)*10
    roundoff = round(gpa,2)
    print(roundoff)
    i.gpa = roundoff
    i.save()