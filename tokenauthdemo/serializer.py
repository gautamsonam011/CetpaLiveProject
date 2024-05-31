from dataclasses import fields
from ssl import _PasswordType
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model=User

fields=['username','password']