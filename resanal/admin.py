# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
<<<<<<< HEAD
from .models import Result, Fetch, Analize
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.



class ResultResource(resources.ModelResource):

    class Meta:
        model = Result



class ResultAdmin(ImportExportModelAdmin):
    resource_class = ResultResource
    pass

admin.site.register(Result,ResultAdmin)
admin.site.register(Fetch)
admin.site.register(Analize)
=======
from .models import Result, Fetch

# Register your models here.

admin.site.register(Result)
admin.site.register(Fetch)

>>>>>>> 251e90d840ba34262f62b20c27ec7291a10773b9
