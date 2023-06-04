from django.urls import path

from app2.views import *
app_name='something'
urlpatterns=[
    path('New/',New,name='new'),
    path('csk/',html_page,name='csk')
    
]