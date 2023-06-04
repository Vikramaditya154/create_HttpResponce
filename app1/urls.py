from django.urls import path

from app1.views import *
app_name='anything'
urlpatterns=[
    path('start/',start,name='start'),
    path('first/',firsthtml,name='first'),
    
]