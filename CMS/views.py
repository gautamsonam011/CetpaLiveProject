from lib2to3.pgen2.token import NL
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import HttpResponse
from CMS.models import Customer

# Create your views here.
class Employee:
    def __init__(self):
        self.name=""
        self.age=0
        self.address=""

def getNEmployee(n):
    list_emp=[]
    for i in range(n):
        emp=Employee()
        emp.name="Sonam"+str(i)
        emp.age=23+i
        emp.address="Delhi"+str(i)
        list_emp.append(emp)
    return list_emp

def numbers(n):
    nl=[]
    for i in range(1,n+1):
        nl.append(i)
    return nl


def view_dtl(request):
    employees=getNEmployee(10)
    res=numbers(20)
    d1={'numbers':res,'employees':employees}
    
    resp=render(request,'CMS/dtl.html', context=d1)
    return resp
def view_cmshome(request):
    if request.method=='GET':
        resp=render(request,'CMS/home.html')
        return resp
    elif request.method=='POST':
        if 'btnadd'in request.POST:
            cus=Customer()
            cus.cid=request.POST.get('txtcid','NA')
            cus.name=request.POST.get('txtname','NA')
            cus.age=request.POST.get('txtage','NA')
            cus.mobileno=request.POST.get('txtmobileno','NA')
            cus.address=request.POST.get('txtaddress','NA')
            cus.save()
            return HttpResponse("<h1>Customer Added Successfully with ID"+str(cus.id)+"!!</h1>")
        elif 'btnsearch' in request.POST:
            cid=int(request.POST.get('txtid',0))  
            cus=Customer.objects.get(id=cid)
            d1={'cus':cus} 
            resp=render(request, 'CMS/home.html', context=d1)
            return resp
        elif 'btnupdate' in request.POST:
            cus=Customer()
            cus.id=int(request.POST.get('txtid',0))   
            if Customer.objects.get(id=cus.id):
                cus.cid=request.POST.get('txtcid','NA')
                cus.name=request.POST.get('txtname','NA')
                cus.age=request.POST.get('txtage','NA')
                cus.mobileno=request.POST.get('txtmobileno','NA')
                cus.address=request.POST.get('txtaddress','NA')
                cus.save()
                return HttpResponse("<h1>Customer Updated Successfully with ID"+str(cus.id)+"!!</h1>")
        elif 'btndelete' in request.POST:
            cus_id=int(request.POST.get('txtid',0))
            Customer.objects.filter(id=cus_id).delete()
            return HttpResponse("<h1>Customer Deleted Successfully with ID"+str(cus_id)+"!!</h1>")
        elif 'btnshow' in request.POST:
            cus_all=Customer.objects.all()
            d1={'Customers':cus_all}
            resp=render(request, 'CMS/home.html', context=d1)
            return resp
