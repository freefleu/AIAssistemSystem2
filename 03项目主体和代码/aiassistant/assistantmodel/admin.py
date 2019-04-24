from django.contrib import admin
from assistantmodel.models import Student,Course,Courseselection,Group,File
# Register your models here.
admin.site.register([Student,Course,Courseselection,Group,File])