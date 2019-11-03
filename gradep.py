from resanal.models import Fetch,Result

for  i in Fetch.objects.filter(usn__batch="2015",usn__sem=8,subcode="15CSP85"):
    if i.totalmarks >= 180:
        i.grade = 10
    elif 160 <= i.totalmarks <= 179:
        i.grade = 9
    elif 140 <= i.totalmarks <= 159:
        i.grade = 8
    elif 120 <= i.totalmarks <= 139:
        i.grade = 7   
    elif 100 <= i.totalmarks <= 119:
        i.grade = 6
    elif 80 <= i.totalmarks <= 99:
        i.grade = 5            
    elif 60 <= i.totalmarks <= 79:
        i.grade = 4
    elif i.totalmarks < 60:
        i.grade = 0
    i.save()