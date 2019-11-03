from resanal.models import Fetch
j = 1
for i in Fetch.objects.filter(usn__batch="2015",usn__sem=8,subcode="15CSP85"):
    if 140 <= i.totalmarks <= 200:
        FCD = "FCD"
    elif 120 <= i.totalmarks <= 139:
        FCD = "FC"
    elif 100 <= i.totalmarks <= 119:
        FCD = "SC"
    elif 80 <= i.totalmarks <= 99:
        FCD = "P"
    else:
        FCD = "F"

    print("Entry "+str(j)+":-FCD="+FCD)
    j += 1
    i.FCD = FCD
    print(FCD)
    i.save()
