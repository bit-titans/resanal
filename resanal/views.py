from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.views import APIView
from drf_multiple_model.views import ObjectMultipleModelAPIView,FlatMultipleModelAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Result, Fetch
from .serializers import ResultSerializer, FetchSerializer
import requests
import bs4
from lxml import html
import re


class MultiAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {
            'queryset': Result.objects.all(),
            'serializer_class': ResultSerializer,
            'label': 'usn_gpa',
        },
        {
            'queryset': Fetch.objects.all(),
            'serializer_class': FetchSerializer,
            'label': 'indMarks'
        },
    ]
    # filter_backends = [filters.SearchFilter,]
    # search_fields = ('usn',)

class ResultList(APIView):
    def get(self, request):
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True )
        return Response(serializer.data)

    def post(self):
        pass

class FetchList(APIView):
    def get(self, request):
        fetches = Fetch.objects.all()
        serializer = FetchSerializer(fetches, many=True )
        return Response(serializer.data)

    def post(self):
        pass

def crawl(request):


    url = "http://results.vtu.ac.in/vitaviresultcbcs2018/resultpage.php"
    result = requests.get(url)

    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='token']/@value")))[0]


    def store_result(scode,sname,imarks,emarks,copymarks,marks,containers_new):
        rname = containers_new[3].text.encode('utf-8')[2:]
        rusn = containers_new[1].text.encode('utf-8')[3:]
        rgpa = round(((sum(marks))/28.0),2)

        r = Result.objects.create(name= rname, usn = rusn, gpa = rgpa)
        for i in xrange(8):
            Fetch.objects.create(initial = r, subcode= scode[i],subname=sname[i],intmarks= imarks[i],extmarks= emarks[i],totalmarks= copymarks[i])


    def get_gpa(containers,containers_new):
        copymarks = []
        marks = []
        imarks = []
        emarks = []
        scode = []
        sname = []
        index = [10,16,22,28,34,40,46,52]
        index1 = [8,14,20,26,32,38,44,50]
        index2 = [9,15,21,27,33,39,45,51]
        index3 = [6,12,18,24,30,36,42,48]
        index4 = [7,13,19,25,31,37,43,49]

        for ind in index:
            marks.append((containers[ind].text).encode('utf-8'))
            copymarks.append((containers[ind].text).encode('utf-8'))
        for ind in index1:
            imarks.append((containers[ind].text).encode('utf-8'))
        for ind in index2:
            emarks.append((containers[ind].text).encode('utf-8'))
        for ind in index3:
            scode.append((containers[ind].text).encode('utf-8'))
        for ind in index4:
            sname.append((containers[ind].text).encode('utf-8'))
        # marks.append((containers[16].text).encode('utf-8'))
        # marks.append((containers[22].text).encode('utf-8'))
        # marks.append((containers[28].text).encode('utf-8'))
        # marks.append((containers[34].text).encode('utf-8'))
        # marks.append((containers[40].text).encode('utf-8'))
        # marks.append((containers[46].text).encode('utf-8'))
        # marks.append((containers[52].text).encode('utf-8'))
        for i in xrange(len(marks)):
            marks[i] = float(marks[i])
        for i in xrange(len(imarks)):
            imarks[i] = float(imarks[i])
        for i in xrange(len(emarks)):
            emarks[i] = float(emarks[i])
        
        for i in xrange(0,6):
            if(marks[i]<40):
                marks[i] = 0
            elif(marks[i]<45):
                marks[i] = 4*4  
            elif(marks[i]<50):
                marks[i] = 5*4
            elif(marks[i]<60):
                marks[i] = 6*4
            elif(marks[i]<70):
                marks[i] = 7*4
            elif(marks[i]<80):
                marks[i] = 8*4
            elif(marks[i]<90):
                marks[i] = 9*4
            else:
                marks[i] = 10*4
        for i in xrange(6,8):
            if(marks[i]<40):
                marks[i] = 0
            elif(marks[i]<45):
                marks[i] = 2*4
            elif(marks[i]<50):
                marks[i] = 2*5
            elif(marks[i]<60):
                marks[i] = 2*6
            elif(marks[i]<70):
                marks[i] = 2*7
            elif(marks[i]<80):
                marks[i] = 2*8
            elif(marks[i]<90):
                marks[i] = 2*9
            else:
                marks[i] = 2*10
        #print(round(((sum(marks))/28.0),2),containers_new[1].text.encode('utf-8')[3:],containers_new[3].text.encode('utf-8')[2:])

        store_result(scode,sname,imarks,emarks,copymarks,marks,containers_new)

    def crawler(usn):
        try:

            url = 'http://results.vtu.ac.in/vitaviresultcbcs2018/resultpage.php'
            headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
            form_data = {'lns':usn,
                        'token':authenticity_token,
                        'current_url':"http://results.vtu.ac.in/vitaviresultcbcs2018/index.php"}
            req = requests.post(url, data=form_data)
            soup = bs4.BeautifulSoup(req.text,"html.parser")
            containers = soup.find_all('div', class_ = 'divTableCell')
            containers_new = soup.find_all('td')

            get_gpa(containers,containers_new)
            
        except IndexError:
            return None
        except ValueError:
            return None

    def initiate(p,q,usn_series):
        for i in range(p,q):
            if (len(str(i)) == 1):
                usn = usn_series +"00"+str(i)
            elif (len(str(i)) == 2):
                usn = usn_series+"0"+str(i)
            else:
                usn = usn_series + str(i)
            crawler(usn)
    
    initiate(1,5,"1bi15cs")
    return HttpResponse("<h1>Crawling on process</h1>")
    
class ResultsView(generic.ListView):
    template_name = 'companies/index.html'
    context_object_name = 'all_student'

    def get_queryset(self):
        return Result.objects.all()

   

    






