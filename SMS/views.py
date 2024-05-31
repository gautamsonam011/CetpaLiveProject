from django.shortcuts import render
from SMS.models import *

# Create your views here.
def view_paymentdetailes(request):
    if request.method=='GET':
        resp=render(request,'SMS/payment.html')
        return resp
    elif request.method=='POST':
        sid=int(request.POST.get('txtid',0))
        stu=student.objects.get(id=sid)
        allp=stu.paymentdetailes_set.all()
        d1={'payment':allp,'stu':stu}
        resp=render(request,'SMS/payment.html',context=d1)
        return resp
def get_course_wise_student_details(request):
    c=courses.objects.all()
    d1={'courses':c}
    if request.method=='GET':
         c=courses.objects.get(id=1)
         d1['cid']=c.id
         d1['cname']=c.name
         allstu=c.students.all()
         d1['students']=allstu
         resp=render(request,'SMS/course.html',context=d1)
         return resp
    elif request.method=='POST':
        course_id=int(request.POST.get('courses',0))
        c=courses.objects.get(id=course_id)
        d1['cid']=c.id
        d1['cname']=c.name
        allstu=c.students.all()
        d1['students']=allstu
        resp=render(request,'SMS/course.html',context=d1)
        return resp

    

    