from resanal.models import Result,Fetch

for i in Result.objects.filter(batch="2017",sem=3):
    print(i.usn)
    totalgrade = 0
    gpa = 0
    roundoff = 0
    for j in i.maping.all():
        if j.subcode=="17MAT31":
                totalgrade += j.grade*4
        if j.subcode=="17CS32":
                totalgrade += j.grade*4
        if j.subcode=="17CS33":
                totalgrade += j.grade*4
        if j.subcode=="17CS34":
                totalgrade += j.grade*4
        if j.subcode=="17CS35":
                totalgrade += j.grade*3
        if j.subcode=="17CS36":
                totalgrade += j.grade*4
        if j.subcode=="17CSL37":
                totalgrade += j.grade*2
        if j.subcode=="17CSL38":
                totalgrade += j.grade*2
        if j.subcode=="17KKX39":
                totalgrade += j.grade*1
    gpa = (totalgrade/280)*10
    roundoff = round(gpa,2)
    i.gpa = roundoff
    i.save()