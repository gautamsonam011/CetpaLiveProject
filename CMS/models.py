from django.db import models

# Create your models here.
class Customer(models.Model):
    cid=models.IntegerField()
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=200)
    sallary=models.IntegerField()
    post=models.CharField(max_length=50)
    def __str__(self):
        return self.name

