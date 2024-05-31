
from tokenize import blank_re
from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50, null=False,blank=False)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=20)
    dob=models.DateField(null=True,blank=True)
    pic=models.ImageField(null=True, blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class courses(models.Model):
    name=models.CharField(max_length=200)
    students=models.ManyToManyField(student,null=True,blank=True)
    def __str__(self):
        return self.name 

class paymentdetailes(models.Model):
    amount=models.IntegerField()
    payment_mode=models.CharField(max_length=200, choices=[('Cash','Cash'),('Debit Card','Debit Card'),('Credit Card','Credit Card'),('PayTM','PayTM')])
    payment_date=models.DateTimeField(auto_now=True)
    student=models.ForeignKey(student,null=False, blank=False,on_delete=models.CASCADE)

