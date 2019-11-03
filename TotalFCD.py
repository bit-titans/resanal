from resanal.models import Result, Fetch

k = 1
for i in Result.objects.filter(batch="2017",sem=1):
    total = 0
    for j in i.maping.all():
        total += j.totalmarks
    if total >= 490:
        FCD = "FCD"
    elif 420 <= total <= 489:
        FCD = "FC"
    elif 350 <= total <= 419:
        FCD = "SC"
    else:
        FCD = "P"
    print("Entry " + str(k) + ":-FCD=" + FCD)
    k += 1
    i.totalFCD = FCD
    i.save()
