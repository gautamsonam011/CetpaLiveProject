from django.urls import path
from.views import *

# Base URL => http://127.0.0.1:8000/sms/form/



urlpatterns=[
    path('payment/',view_paymentdetailes),
    path('courses/',get_course_wise_student_details),
    
    

]