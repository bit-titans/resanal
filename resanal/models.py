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

