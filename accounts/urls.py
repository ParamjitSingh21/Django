from django.urls import path
from .views import SignUp,SignUp2

app_name = 'accounts' 

urlpatterns = [
    path('signUp',SignUp, name='sign-up'),
    path('signUp2',SignUp2, name='sign-up2'),

]