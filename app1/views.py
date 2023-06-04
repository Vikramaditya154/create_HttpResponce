from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def start(request):
    return HttpResponse('<h1>sai prathap loverboy</h1>') 
def firsthtml(request):
    return render(request,'app1file.html') 