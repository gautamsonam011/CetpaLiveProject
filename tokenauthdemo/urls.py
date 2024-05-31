from django.urls import path
from.views import *
from rest_framework.authtoken.views import obtain_auth_token

# Base URL=>> http://127.0.0.1:8000/tokendemo/
urlpatterns = [
    path('register/',view_register),
    path('login/',obtain_auth_token),
    #path('secure/',view_secure),
]
