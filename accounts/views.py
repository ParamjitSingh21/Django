from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from .forms import SignUpForm
from django import forms

# Create your views here.


def SignUp(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        pass1 = form['password1'].value
        pass2 = form['password2'].value

        # if pass1 != pass2:
        #     raise forms.ValidationError("Password don't match")

        print(pass2,pass1)
    return render(request, 'SignUp.html', {'form': form})