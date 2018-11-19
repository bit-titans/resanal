from django.views import generic
from django.db.models import Avg
from django.shortcuts import get_object_or_404, render
from django.db import IntegrityError
from django.http import HttpResponse
from rest_framework.views import APIView
from drf_multiple_model.views import ObjectMultipleModelAPIView,FlatMultipleModelAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Result, Fetch, Analize
from . crawlusn import CrawlResult
from . analizeResult import ResultAnalize
from .serializers import ResultSerializer, FetchSerializer, AnalizeSerializer
import requests
import bs4
from lxml import html
import re


class MultiAPIView(ObjectMultipleModelAPIView):
    def get_querylist(self):
        

        
        qsemester= self.request.query_params.get('sem')
        qbatch = self.request.query_params.get('batch')
        if(qsemester and qbatch):
            querylist = (
                
                {
                    'queryset': Result.objects.filter(sem = qsemester, batch=qbatch, gpa__gte = 4),
                    'serializer_class': ResultSerializer,
                    'label': 'passCount'
                },
                {
                    'queryset': Result.objects.filter(sem = qsemester, batch=qbatch, gpa__lt = 4),
                    'serializer_class': ResultSerializer,
                    'label': 'failCount',
                },
            )

            return querylist
            # filter_backends = [filters.SearchFilter,]
            # search_fields = ('usn',)
   
class ResultList(APIView):
    def get(self,request):
        #results = Result.objects.all()
        #serializer = ResultSerializer(results, many=True )
        #return Response(.data)
        queryset = Result.objects.order_by('-gpa')
        qsemester= self.request.query_params.get('sem')
        qsection = self.request.query_params.get('sec')
        qbatch = self.request.query_params.get('batch')
        
        
        if(qsemester and qbatch and qsection is not None):
            results = queryset.filter(sem = qsemester, batch = qbatch, section = qsection)

            serializer = ResultSerializer(results, many=True )
            return Response(serializer.data)

        if(qsemester and qbatch is not None):
            results = queryset.filter(sem = qsemester, batch = qbatch)

            serializer = ResultSerializer(results, many=True )
            return Response(serializer.data)
    # def get_serializer_class(self):
    #     return ResultSerializer
    
    def post(self):
        pass

class FetchList(APIView):
    def get(self, request):
        
        fetches = Fetch.objects.filter(usn__sem = 4,usn__section = 'C', usn__batch = 2016,subcode='15CS42',totalmarks__gte= 40)

        serializer = FetchSerializer(fetches, many=True )
        return Response(serializer.data)

    def post(self):
        pass

def crawl(request):
    
    resultcrawl = CrawlResult()
    resultcrawl.initiate()

    return HttpResponse("<h1>Crawling Done</h1>")
    
class ResultsView(generic.ListView):
    template_name = 'resanal/index.html'
    context_object_name = 'all_student'

    def get_queryset(self):
        return Result.objects.all()

   
def analysis(request):

    resultanalize = ResultAnalize()
    resultanalize.analizeresult()

    return HttpResponse("<h1> Analysis Done! Check your website</h1>")
                    

 
class  AnalizeApi(APIView):
    def get(self, request):
        qsemester= self.request.query_params.get('sem')
        qsection = self.request.query_params.get('sec')
        qbatch = self.request.query_params.get('batch')
        qsubcode = self.request.query_params.get('scode').rpartition(' ')[0]

        if(qsemester and qbatch and qsubcode and qsection):
            reqAnalysis = Analize.objects.filter(batch = qbatch, sem = qsemester, sec = qsection, subcode = qsubcode)
        elif(qsemester and qbatch and qsubcode):
            reqAnalysis = Analize.objects.filter(sem = qsemester, batch = qbatch, subcode = qsubcode)
        else:
            pass

        serializer = AnalizeSerializer(reqAnalysis, many=True )
        return Response(serializer.data)

    def post(self):
        pass






    


    






