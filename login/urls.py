from django.urls import path
from login import views
# from django.conf.urls import url

urlpatterns = [
    # url(r"^/$", views.index, name="Hello"),
    
    path('',views.index,name='index'),
]