from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import DataInfo

# Create your views here.
def index(request):
    return render(request,'index.html')
def today(request):
    return render(request,'today.html')

@csrf_exempt
def post_data(request,numms):
    Data = DataInfo()
    Data.nums_title = numms
    Data.save()
    return HttpResponse('OK!')