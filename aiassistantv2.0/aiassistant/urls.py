"""aiassistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import settings
from assistantmodel import views,tests
from django.views.static import serve

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^admin/',admin.site.urls),
    url(r'^login-post',views.login_post),
    url(r'^index/',views.index),
    url(r'^course',views.getcourse),
    url(r'^result',views.courseresult),
    url(r'^register',views.register),
    url(r'^group-before',views.groups_before),
    url(r'^mygroup',views.mygroup),
    url(r'^file-before',views.file_before),
    url(r'media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
    path('file_post/',views.file_post,name='file_post'),
    path('file_down/',views.file_down,name='file_down'),
    url(r'^myinfo',views.myinfo),
    #url(r'^testdb$',tests.testdb),#要有$符号，否则运行不成功
]
