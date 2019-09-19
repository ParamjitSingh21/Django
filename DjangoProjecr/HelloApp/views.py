from django.shortcuts import render
from django.http import HttpResponse
from HelloApp.models import AccessRecord,Topic,Webpage,Users


# Create your views here.

my_dict = {'index_cont':'I am from HelloApp View',"help":'I am help'}
def index(request):
    return render(request,'HelloApp/index.html',context=my_dict)

def image(request):
    return render(request,'HelloApp/staticImage.html',context=my_dict)

def HelloAppIndex(request):
    return render(request,'HelloApp/help.html',context=my_dict)

def AccessRecords(request):
    record_list = AccessRecord.objects.order_by('date')
    my_dict = {'records':record_list} 
    return render(request,'HelloApp/records.html',context=my_dict)

def UserRecord(request):
    record_list = Users.objects.order_by()
    my_dict = {'UserRecords':record_list} 
    return render(request,'HelloApp/users.html',context=my_dict)