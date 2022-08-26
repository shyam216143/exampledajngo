from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def home(request):
    
    context={'fruits':fruits.objects.all()}
     # return HttpResponse("hello this is Shyam Kumar")
    return render(request , 'home.html', context) 
    