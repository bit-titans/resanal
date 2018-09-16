# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Result(models.Model):

    class Meta:
        unique_together = (('usn', 'sem', ),)

    #name = models.CharField(max_length = 11,unique=True)
    name = models.CharField(max_length = 40)
    usn = models.CharField(max_length = 50)
    sem = models.IntegerField(null=True)
    section = models.CharField(max_length=1,null=True)
    batch = models.IntegerField(null=True)
    gpa = models.FloatField(null=True, blank = True)

    #volume = models.IntegerField

    def __str__(self):
        return (self.name)

class Fetch(models.Model):
    res = models.ForeignKey(Result,on_delete=models.CASCADE)
    subcode = models.CharField(max_length = 10)
    subname = models.CharField(max_length = 100)
    intmarks = models.IntegerField()
    extmarks = models.IntegerField()
    totalmarks = models.IntegerField()
    grade = models.IntegerField(null=True)


# class Analysis(models.Model):

#     class Meta:
#         unique_together = (('batch', 'sem', 'subcode'),)

#     batch = models.IntegerField()
#     sem = models.IntegerField()
#     subcode = models.CharField(max_length = 10)
#     subname = models.CharField(max_length = 100)
#     pass_count = models.IntegerField()
#     fail_count = models.IntegerField()



    def __str__(self):
        return self.res.name
