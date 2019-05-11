from django.shortcuts import render
from assistantmodel.models import Student,Course,Courseselection,Group,File
from django.views.decorators import csrf
from django.http import HttpResponseRedirect,HttpResponse
import time
from django.shortcuts import HttpResponse, render, redirect
from django.db.models import Q
from django.http import JsonResponse
import json
from django.core import serializers
from aiassistant import settings
import os
# Create your views here.

# 接收POST请求数据
def login_post(request):
    #ctx = {}
    if request.POST:
        #return HttpResponse(request.POST['id'])
        #自强学堂例子
        #m = Member.objects.get(username=request.POST['username'])
        #if m.password == request.POST['password']:

        #id,name是前端文本框的名字；stu_id,stu_name是数据库的字段名；db_name是从数据库查询得到的结果
        if Student.objects.get(stu_id=request.POST['id']):
            db_student=Student.objects.get(stu_id=request.POST['id'])
            if db_student.stu_password == request.POST['password']:
                request.session['stu_id'] = db_student.stu_id
                request.session['stu_name'] = db_student.stu_name
                return HttpResponse('200')
            else:
                return HttpResponse('err')
        else:
            return HttpResponse('err')
            #ctx['rlt'] ='用户名或密码错误'
    #return render(request, "vue-login.html",ctx)
    return render(request, "vue-login.html")

def index(request):
    ctx={}
    ctx['rlt0'] = request.session['stu_name']
    return render(request,"vue-index.html",ctx)

def myinfo(request):
    ctx={}
    ctx['rlt'] = request.session['stu_name']+'个人信息页面'
    return render(request, "vue-myinfo.html", ctx)

def courseresult(request):
    ctx = {}
    search = request.session['search']
    temp1 = Course.objects.filter(cour_name__contains=search)
    ctx['rlt'] = temp1.filter(courseset__sel_stu=request.session['stu_id']).order_by('cour_id')  # 已选课程
    ctx['rlt2'] = temp1.exclude(courseset__sel_stu=request.session['stu_id']).order_by('-cour_id')  # 未选课程
    return render(request, "result.html", ctx)

def getcourse(request):
    ctx={}
    ctx['rlt0'] = request.session['stu_name']
    ctx['rlt'] = Course.objects.filter(courseset__sel_stu=request.session['stu_id'])#已选课程
    ctx['rlt2'] = Course.objects.exclude(courseset__sel_stu=request.session['stu_id'])  # 未选课程
    ctx['rlt3']=''
    '''Rlt = Course.objects.filter(courseset__sel_stu=request.session['stu_id'])  # 已选课
    Rlt2 = Course.objects.exclude(courseset__sel_stu=request.session['stu_id'])  # 未选课程
    json_data1 = serializers.serialize('json', Rlt)
    json_data1 = json.loads(json_data1)

    json_data2 = serializers.serialize('json', Rlt2)
    json_data2 = json.loads(json_data2)'''

    if "course_id123" in request.GET:#选课操作
    #if request.post.get('course_id123')
        #return HttpResponse("<p>收到POST</p>")
        #return HttpResponse(request.GET['course_id123'][1:11])
        selectcourse_id = request.GET['course_id123'][1:11]
        #ctx['rlt3']=selectcourse_id#rlt3用来检验是否收到表单
        temp3 = Courseselection.objects.filter(sel_stu=Student.objects.get(stu_id=request.session['stu_id']),
                                sel_cour=Course.objects.get(cour_id=selectcourse_id))
        if temp3:
            #return HttpResponse('001')#001表示已选这门课
            ctx['rlt3']=''
        else:
            temp1 = Courseselection(sel_stu=Student.objects.get(stu_id=request.session['stu_id']),
                                    sel_cour=Course.objects.get(cour_id=selectcourse_id),
                                    sel_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                    sel_score=0, sel_grade=0)
            temp1.save()
            temp2 = Course.objects.get(cour_id=selectcourse_id)
            temp2.cour_stunum = temp2.cour_stunum+1
            temp2.save()
            return render(request,"course2.html",ctx)
    #if request.POST.get('course_id456'):#退课操作
    if request.GET.get('course_id456'):
        #dropcourse_id = request.POST.get('course_id456')
        dropcourse_id=request.GET['course_id456'][1:11]
        temp3 = Courseselection.objects.filter(sel_stu=Student.objects.get(stu_id=request.session['stu_id']),
                                               sel_cour=Course.objects.get(cour_id=dropcourse_id))
        if temp3:
            temp1 = Courseselection.objects.get(sel_cour=Course.objects.get(cour_id=dropcourse_id),
                                            sel_stu=Student.objects.get(stu_id=request.session['stu_id']))
            temp1.delete()
            temp2 = Course.objects.get(cour_id = dropcourse_id )
            temp2.cour_stunum = temp2.cour_stunum - 1
            temp2.save()
            return render(request, "course2.html", ctx)
        else:
            #return HttpResponse('001')  # 001表示没选这门课
            ctx['rlt3'] = ''
    if request.GET.get('course_id789'):#组队界面
        #groupcourse_id = request.POST.get('course_id789')
        groupcourse_id=request.GET['course_id789'][1:11]
        temp3 = Courseselection.objects.filter(sel_stu=Student.objects.get(stu_id=request.session['stu_id']),
                                               sel_cour=Course.objects.get(cour_id=groupcourse_id))
        if temp3:
            request.session['groupcourse_id'] = groupcourse_id
            #return render(request, "groups.html", ctx)
            return redirect('http://127.0.0.1:8000/group-before')
        else:
            #return HttpResponse('001')
            ctx['rlt3'] = ''

    if request.POST.get('sea'):  # 搜索
        #return HttpResponse('000')
        search = request.POST.get('sea')
        request.session['search'] = search
        return redirect('http://127.0.0.1:8000/result')
   # return render(request, "vue-course.html",{ 'rlt': json.dumps(json_data1),'rlt2':json.dumps(json_data2)})
    return render(request,"course2.html",ctx)

def register(request):
    if request.POST:
        temp=Student.objects.filter(stu_id=request.POST.get('idq'))
        if temp:
            return HttpResponse('001')
        else:
            temp1=Student(stu_id=request.POST.get('idq'),stu_name=request.POST.get('nameq'),stu_password=request.POST.get('passwordq'),
                          stu_gender=request.POST.get('genderq'),stu_college=request.POST.get('collegeq'),stu_label1=request.POST.get('label1q'),
                          stu_label2=request.POST.get('label2q'),stu_label3=request.POST.get('label3q'),stu_label4=request.POST.get('label4q'),
                          stu_label5=request.POST.get('label5q'),stu_label6=request.POST.get('label6q'),)
            temp1.save()
        return HttpResponseRedirect('/login-post/')
    return render(request,"register.html")

def groups_before(request):
    groupcourse_id = request.session['groupcourse_id']
    ctx = {}
    temp=Group.objects.filter(group_courid=groupcourse_id)
    ctx['rlt'] = temp

    if request.POST.get('group_id'):
        ren=request.session['stu_id']
        temp2 = temp.filter(Q(group_leader=ren)|Q(group_member1=ren)|Q(group_member2=ren)|Q(group_member3=ren)
                          |Q(group_member4=ren))
        if temp2:
            return HttpResponse('001')#每个人只能加入一个队伍
        else:
            group_id2 = request.POST.get('group_id', None)
            group_position = request.POST.get('group_position', None)
            temp1 = Group.objects.get(group_id=group_id2)
            if group_position=='1':
                temp1.group_member1 = Student.objects.get(stu_id=request.session['stu_id'])
            elif group_position == '2':
                temp1.group_member2 = Student.objects.get(stu_id=request.session['stu_id'])
            elif group_position=='3':
                temp1.group_member3 = Student.objects.get(stu_id=request.session['stu_id'])
            elif group_position=='4':
                temp1.group_member4 = Student.objects.get(stu_id=request.session['stu_id'])
            temp1.save()
    if request.POST.get('new_name'):
        ren = request.session['stu_id']
        temp2 = temp.filter(Q(group_leader=ren) | Q(group_member1=ren) | Q(group_member2=ren) | Q(group_member3=ren)
                            | Q(group_member4=ren))
        if temp2:
            return HttpResponse('001')  # 每个人只能加入一个队伍
        else:
            temp1=Group(group_courid=Course.objects.get(cour_id=groupcourse_id),
                  group_leader=Student.objects.get(stu_id=ren),
                  group_name=request.POST.get('new_name', None))
            temp1.save()
    return render(request, "groups.html", ctx)

'''def groups(request):
    group_id = request.POST.get('group_id', None)
    #groups_id = int(group_id) - 1
    group_position = request.POST.get('group_position',None)
    if(data_group[groups_id][group_position] != ''):
        print('hello,data')
        return HttpResponse('sorry')
    else:
        print("获得新的值：")
        member = request.POST.get('users',None)
        print("member的值："+ member)
        data_group[groups_id][group_position] = member
        return render(request, "groups.html", {'data':data_group})
    temp1=Group.objects.get(group_id=group_id)
    groupmember='group_member'+group_position
    temp1.groupmember=Student.objects.get(stu_id = request.session['stu_id'])
    temp1.save()'''
'''def newBuild(request):
    global id
    newBuild_master = request.POST.get('users',None)
    id += 1
    newData = {'id':id,'master':newBuild_master,'member1':'','member2':'','member3':'','member4':''}
    data_group.append(newData)
    return render(request, "groups.html", {'data': data_group})'''

def mygroup(request):
    ctx={}
    ren = request.session['stu_id']
    ctx['rlt'] = Group.objects.filter(Q(group_leader=ren) | Q(group_member1=ren) | Q(group_member2=ren) | Q(group_member3=ren)
                            | Q(group_member4=ren))
    if request.POST.get('group_id'):
        groupid = request.POST.get('group_id')
        request.session['file_group_id'] = groupid
        return redirect('http://127.0.0.1:8000/file-before')
    #else:
        #return HttpResponse('001')
    return render(request, "mygroup.html", ctx)

def file_before(request):
    ctx={}
    #ren = request.session['stu_id']
    ctx['rlt'] = Group.objects.filter(group_id=request.session['file_group_id'])
    return render(request, "fileinput.html", ctx)

def file_post(request):
    if request.method=='POST':

        file_obj = request.FILES.get('file')
        #print(file_obj.name,'---------')
        temp = {'fileName': file_obj.name}
        #file_name.append(temp)#添加数据名字到一个数组里面
        temp1=File(file_renname=request.session['stu_name'], file_filename=file_obj.name,
                   file_groups=request.session['file_group_id'],
                   file_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        temp1.save()
        f = open(os.path.join(settings.MEDIA_ROOT,'',file_obj.name),'wb')
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('yes')
    return render(request,'fileinput.html')

'''def file_down(request):
    temp1=File.objects.filter(file_groups=request.session['file_group_id'])
    file_name=[]
    #ren_name=[]
    for i in temp1:
        file_name.append(i.file_filename)
        #ren_name.append(i.file_filename)

    return JsonResponse(file_name,safe=False)'''

def file_down(request):
    temp1=File.objects.filter(file_groups=request.session['file_group_id'])
    dataitem=[]
    for i in temp1:
        temp=[]
        temp.append(i.file_filename)
        temp.append(i.file_renname)
        temp.append(i.file_time)
        dataitem.append(temp)
    return JsonResponse(dataitem,safe=False)