from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): # this function takes http request and return httpRespond
    return render(request,"hello/index.html")

def hasan(request):
    return HttpResponse("Hello, Hasan!")

def safat(request):
    return HttpResponse("Hello, Safat!")

def greet(request, name):
    return render(request,"hello/greet.html",{
        "name": name.capitalize()
    })
