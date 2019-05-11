from django.test import TestCase

# Create your tests here.
from assistantmodel.models import Student,Course,Group,Courseselection,Group,File
from django.http import HttpResponse
from django.shortcuts import HttpResponse, render, redirect
import time


'''def testdb(request):
    test1 = Group(group_courid=Course.objects.get(cour_id='0000000002'),
                  group_leader=Student.objects.get(stu_id='1231231231'),
                  group_name='天下第一')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")'''
'''def testdb(request):
    temp1 = Group.objects.get(group_id='2')
    temp1.group_member1 = Student.objects.get(stu_id='1212121212')
    temp1.save()
    return HttpResponse("<p>数据添加成功！</p>")'''



def testdb(request):
    temp1=Course(cour_id='0000000005',cour_name='C语言基础',cour_teacher='得到的',cour_timeplace='爱对方身份',
                 cour_college='计算机',cour_stunum=0,cour_score=6.7,cour_avescore=87,cour_failrate=0.18)
    temp1.save()
    return HttpResponse("<p>数据添加成功！</p>")
