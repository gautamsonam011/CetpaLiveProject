"""CetpaLiveProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin 
from django.urls import path,include
from django.shortcuts import render
from django.http import HttpResponse #http://127.0.0.1:8000/
from django.http import *  #http://127.0.0.1:8000/copy/

def get_Numeric_button(request):
    list_button=['btn1', 'btn2', 'btn3', 'btn4', 'btn5', 'btn6', 'btn7', 'btn8', 'btn9', 'btn0']
    for b in list_button:
        if b in request.POST:
            return b[3]
        return '-1'


def view_simple_calc(request):
    if request.method=='GET':
        resp=render(request,'simple.html')
        return resp
    elif request.method=='POST':
        msg=request.POST.get('res','')
        check_no=get_Numeric_button(request)
        if(check_no!=-1):
            msg=msg+check_no
            d1={'msg':msg}
            resp=render(request,'simple.html',context=d1)
            return resp
     
def sum(request):
    return HttpResponse("<h1> Hello I am calling sum</h1>")
def sub(request):
    return HttpResponse("<h1> Hello I am calling sub</h1>")
def mult(request):
    return HttpResponse("<h1> Hello I am calling mult</h1>")
def div(request):
    return HttpResponse("<h1> Hello I am calling div</h1>")

def view_calc(request):
    a=int(request.POST.get("t1",0))
    b=int(request.POST.get("t2",0))
    if request.method=='GET':
         return render( request ,'simple.html')
    elif request.method=='POST':
        if 'btnsum' in request.POST:
            res=a+b
        elif 'btnsub' in request.POST:
            res=a-b
        elif 'btnmul' in request.POST:
            res=a*b
        elif 'btndiv' in request.POST:
            res=a/b
        d1={'a':a,'b':b,'res':res}
        return render(request,'simple.html')

def view_copy(request):
    a=input("Enter the user input")
    b=a
    if request.method=='GET':
        return render(request,'copy.html')
    elif request.method=='POST':
        if (a,b) in request.POST:
            a=b
            b=a

        
            




        


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/',sum),
    path('sub/',sub),
    path('mult/',mult),
    path('div/',div),
    path('calc/',view_calc),
    path('simple/',view_simple_calc),
    path('cms/',include('CMS.urls')), #http://127.0.0.1:8000/cms/
    path('sms/',include('SMS.urls')), #http://127.0.0.1:8000/sms/
    path('sgm/',view_copy),
    path('api/',include('demoapi.urls')), #http://127.0.0.1:8000/api/
    path('session/',include('sessiondemo.urls')), #http://127.0.0.1:8000/session/
    path('tokendemo/',include('tokenauthdemo.urls')),#http://127.0.0.1:8000/tokendemo/
]