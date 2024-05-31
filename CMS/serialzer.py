from importlib.metadata import MetadataPathFinder
from rest_framework import serializers
from SMS.models import student


class StudentSerialzer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['name','age','mobileno']