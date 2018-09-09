# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Result(models.Model):
    name = models.CharField(max_length = 11)
    usn = models.CharField(max_length = 50)
    gpa = models.FloatField()
    #volume = models.IntegerField

    def __str__(self):
        return self.name

class Fetch(models.Model):
    initial = models.ForeignKey(Result,on_delete=models.CASCADE)
    subcode = models.CharField(max_length = 10)
    subname = models.CharField(max_length = 100)
    intmarks = models.IntegerField()
    extmarks = models.IntegerField()
    totalmarks = models.IntegerField()

    def __str__(self):
        return self.initial.name
