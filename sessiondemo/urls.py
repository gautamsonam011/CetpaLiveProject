from django.urls import path
from.views import *

# Base URL-http://127.0.0.1:8000/session/

urlpatterns = [
    path('count/',view_page_visit_count),
    path('write/',view_write_cookie),
    path('read/',view_read_cookie),
]
