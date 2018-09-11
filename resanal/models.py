# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Result(models.Model):
    name = models.CharField(max_length = 11,unique=True)
    usn = models.CharField(max_length = 50)
    sem = models.IntegerField()
    section = models.CharField(max_length=1)
    batch = models.IntegerField()
    gpa = models.FloatField()

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
    grade = models.IntegerField()

class Analysis(models.Model):
    sem = models.IntegerField()
    subcode = models.CharField(max_length = 10, unique = True)
    subname = models.CharField(max_length = 100)
    pass_count = models.IntegerField()
    fail_count = models.IntegerField()
    

    def __str__(self):
        return self.initial.name
