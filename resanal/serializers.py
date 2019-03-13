from rest_framework import serializers
# from django_filters.rest_framework import DjangoFilterBackend
from .models import Result, Fetch, Analize

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        #fields = ('usn','gpa')
        fields = '__all__'
        # filter_backends = (DjangoFilterBackend,)
        # filter_fields = ('sem','section','batch')        

class FetchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fetch
        fields = ('id','usn')

class AnalizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Analize
        fields = '__all__'
    