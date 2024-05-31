from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Create your models here.
class PersonalDetail(models.Model):
    dateofbirth=models.DateField(null=True,blank=True)
    address=models.CharField(max_length=40,null=True,blank=True)
    pic=models.ImageField(null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

@receiver(signal=post_save,sender=User)
def after_user_save(sender,instance,created,**kwargs):
    if created:
        instance.is_staff=True
        instance.is_superuser=True
        instance.save()
        pd=PersonalDetail()
        pd.user=instance
        pd.save()
        t=Token()
        t.user=instance
        t.save