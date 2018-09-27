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
        #results = Result.objects.all()
        #serializer = ResultSerializer(results, many=True )
        #return Response(serializer.data)

        queryset = Result.objects.order_by('-gpa')
        qsemester= self.request.query_params.get('sem')
        qsection = self.request.query_params.get('sec')
        qbatch = self.request.query_params.get('batch')
        
        if(qsection and qsemester and qbatch is not None):
            queryset = queryset.filter(section=qsection,sem=qsemester,batch=qbatch)
        serializer = ResultSerializer(queryset, many=True )
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
    
    resultcrawl = CrawlResult()
    series = "1bi16cs"
    resultcrawl.initiate(1,200,series)

    return HttpResponse("<h1>Crawling on process</h1>")
    
class ResultsView(generic.ListView):
    template_name = 'resanal/index.html'
    context_object_name = 'all_student'

    def get_queryset(self):
        return Result.objects.all()

   

    






