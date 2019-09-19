from django.urls import path
from HelloApp import views
# from django.conf.urls import url

urlpatterns = [
    # url(r"^/$", views.index, name="Hello"),
    
    path('',views.index,name='help'),
    path('img',views.image,name='image'),
    path('help',views.HelloAppIndex,name='index'),
    path('records',views.AccessRecords,name="records"),
    path('users',views.UserRecord,name="UserRecords"),
]
