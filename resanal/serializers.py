from rest_framework import serializers
from .models import Result, Fetch

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ('usn','gpa')
        #fields = '__all__'

class FetchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fetch
        fields = '__all__'