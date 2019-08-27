from resanal.models import Result,Fetch

for i in Result.objects.filter(batch="2017",sem=4):
    print(i.usn)
    totalgrade = 0
    gpa = 0
    total = 270
    roundoff = 0
    for j in i.maping.all():
        if j.subcode=="17MAT41":
                totalgrade += j.grade*4
        if j.subcode=="17CS42":
                totalgrade += j.grade*3
        if j.subcode=="17CS43":
                totalgrade += j.grade*4
        if j.subcode=="17CS44":
                totalgrade += j.grade*4
        if j.subcode=="17CS45":
                totalgrade += j.grade*4
        if j.subcode=="17CS46":
                totalgrade += j.grade*4
        if j.subcode=="17CSL47":
                totalgrade += j.grade*2
        if j.subcode=="17CSL48":
                totalgrade += j.grade*2
        if j.subcode=="17CPH49":
                totalgrade += j.grade*1
                total = 280
    gpa = (totalgrade/total)*10
    roundoff = round(gpa,2)
    print(roundoff)
    i.gpa = roundoff
    i.save()