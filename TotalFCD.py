from resanal.models import Result, Fetch

k = 1
for i in Result.objects.filter(batch="2015",sem=7):
    total = 0
    for j in i.maping.all():
        total += j.totalmarks
    if total >= 560:
        FCD = "FCD"
    elif 480 <= total <= 559:
        FCD = "FC"
    elif 400 <= total <= 499:
        FCD = "SC"
    #elif i.gpa == None:
     #   FCD= "-"
    else:
        FCD = "P"
    print("Entry " + str(k) + ":-FCD=" + FCD)
    k += 1
    i.totalFCD = FCD
    i.save()
