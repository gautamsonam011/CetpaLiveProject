from django.urls import path
from .views import *

#Bbase URL=>> http://127.0.0.1:8000/cms/

urlpatterns = [
    path('dtl/',view_dtl),
    path('home/',view_cmshome),
    
]
