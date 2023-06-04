from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def New(request):
    return HttpResponse('<h1> app2 url mapping is successfully created</h1>')
def html_page(request):
    return render(request,'csk.html')