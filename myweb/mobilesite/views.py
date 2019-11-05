from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import DataInfo,Data_2Info

# Create your views here.
def index_m(request):
    return render(request,'index_m.html')
def today_m(request):

    data = DataInfo.objects.order_by('-id')[0]
    data_2 = Data_2Info.objects.order_by('-id')[0]
    raw_L = round(90*(data.nums_title/100),1)
    raw2_L = round(90*(data_2.nums_title/100),1)
    return render(request,'today.html',{'data':data,'data_2':data_2,'raw_L':raw_L,'raw2_L':raw2_L})
def index(request):
    data = DataInfo.objects.order_by('-id')[0]
    data_2 = Data_2Info.objects.order_by('-id')[0]
    raw_L = round(90*(data.nums_title/100),1)
    raw2_L = round(90*(data_2.nums_title/100),1)
    return render(request,'index.html',{'data':data,'data_2':data_2,'raw_L':raw_L,'raw2_L':raw2_L})
def person(request):
    return render(request,'person.html')
def area(request):
    return render(request,'area.html')

@csrf_exempt
def post_data(request,numms):
    Data = DataInfo()
    Data.nums_title = numms
    Data.save()
    return HttpResponse('OK!')

@csrf_exempt
def post_data_2(request,numms):
    Data = Data_2Info()
    Data.nums_title = numms
    Data.save()
    return HttpResponse('OK!')