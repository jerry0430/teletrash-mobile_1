from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'index.html')
def today(request):
    return render(request,'today.html')