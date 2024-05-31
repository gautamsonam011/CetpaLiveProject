from django.shortcuts import render        


# Create your views here.

def view_page_visit_count(request):
    count=request.session.get("count","NA")
    if count=="NA":
        count=1
    else:
        count=count+1
        d1={'count':count}
        resp= render(request,'sessiondemo/count.html',context=d1)
        return resp

def view_write_cookie(request):
    if request.method=='GET':
        resp=render(request,'sessiondemo/writecookie.html')
        return resp
    elif request.method=='POST':
        username=request.POST.get('txtuser','NA')
        resp=render(request,'sessiondemo/writecookie.html')
        resp.set_cookie(key='user',value=username,max_age=60*60*24*365) # Persistent(Set Time)
        return resp


def view_read_cookie(request):
    if request.method=='GET':
        resp=render(request,'sessiondemo/read.html')
        return resp
    elif request.method=='POST':
        username=request.COOKIES.get('user','NA')
        if username=='NA':
            d1={'msg':'Cookies Not Found!'}
        else:
            d1={'msg':username}
        resp=render(request,'sessiondemo/read.html',context=d1)
        return resp





        