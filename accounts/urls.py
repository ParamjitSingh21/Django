from django.urls import path
from .views import SignUp

app_name = 'accounts' 

urlpatterns = [
    path('signUp',SignUp, name='sign-up'),
]