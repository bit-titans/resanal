from resanal.models import Result,Fetch

for i in Result.objects.filter(batch="2015",sem=8):
    print(i.usn)
    totalgrade = 0
    gpa = 0
    roundoff = 0
    for j in i.maping.all():
        if j.subcode=="15CS81":
                totalgrade += j.grade*4
        if j.subcode=="15CS82":
                totalgrade += j.grade*4
        if j.subcode=="15CS84":
                totalgrade += j.grade*2
        if j.subcode=="15CS834":
                totalgrade += j.grade*3
        if j.subcode=="15CSP85":
                totalgrade += j.grade*5
        if j.subcode=="15CSS86":
                totalgrade += j.grade*2
        if j.subcode=="15CS832":
                totalgrade += j.grade*3
    gpa = (totalgrade/200)*10
    roundoff = round(gpa,2)
    print(roundoff)
    i.gpa = roundoff
    i.save()