from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


# Create your views here.
my_dict = {'index_cont':'I am from HelloApp View',"help":'I am help'}
def index(request):
    return render(request,'login.html',context=my_dict)