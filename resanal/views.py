from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.views import APIView
from drf_multiple_model.views import ObjectMultipleModelAPIView,FlatMultipleModelAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Result, Fetch
from . crawlusn import CrawlResult
from .serializers import ResultSerializer, FetchSerializer
import requests
import bs4
from lxml import html
import re


class MultiAPIView(ObjectMultipleModelAPIView):
    def get_querylist(self):
        

        
        qsemester= self.request.query_params.get('sem')
        qsection = self.request.query_params.get('sec')
        qbatch = self.request.query_params.get('batch')
        qsubcode = self.request.query_params.get('scode').rpartition(' ')[0]
        if(qsemester and qsection and qbatch and qsubcode is not None):
            querylist = (
                
                {
                    'queryset': Fetch.objects.filter(usn__sem = qsemester, usn__section  = qsection, usn__batch=qbatch,subcode = qsubcode, totalmarks__gte = 40),
                    'serializer_class': FetchSerializer,
                    'label': 'passCount'
                },
                {
                    'queryset': Fetch.objects.filter(usn__sem = qsemester, usn__section  = qsection, usn__batch=qbatch,subcode = qsubcode, totalmarks__lt = 40),
                    'serializer_class': FetchSerializer,
                    'label': 'failCount',
                },
            )

            return querylist
            # filter_backends = [filters.SearchFilter,]
            # search_fields = ('usn',)
   
class MultiAPIView1(ObjectMultipleModelAPIView):
    def get_querylist(self):
        #results = Result.objects.all()
        #serializer = ResultSerializer(results, many=True )
        #return Response(.data)
        setquery = Result.objects.order_by('-gpa')
        qsemester= self.request.query_params.get('sem')
        qsection = self.request.query_params.get('sec')
        qbatch = self.request.query_params.get('batch')
        serializer_class = ResultSerializer
        
        
        if(qsemester and qbatch is not None):
            querylist = (
                
                {
                    'queryset': setquery.filter(sem = qsemester, batch = qbatch, gpa__gte = 4),
                    'serializer_class': ResultSerializer,
                    'label': 'passCount'
                },
                {
                    'queryset': setquery.filter(sem = qsemester, batch = qbatch, gpa__lt = 4),
                    'serializer_class': ResultSerializer,
                    'label': 'failCount',
                },
                {
                    'queryset': setquery.filter(sem = qsemester, batch = qbatch),
                    'serializer_class': ResultSerializer,
                    'label': 'totalResult',
                },

            )

            return querylist
        
        #     queryset = queryset.filter(sem=qsemester,batch=qbatch)
        # serializer = ResultSerializer(queryset, many=True )
        # return Response(serializer.data)
    def get_serializer_class(self):
        return ResultSerializer
    


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

    return HttpResponse("<h1>Crawling on process</h1>")
    
class ResultsView(generic.ListView):
    template_name = 'resanal/index.html'
    context_object_name = 'all_student'

    def get_queryset(self):
        return Result.objects.all()

   

    






