from django.shortcuts import render, redirect

from django.contrib.auth import login
from .forms import UserRegistrationForm
# Create your views here.

# Create your views here.


def SignUp2(request):
    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')
    
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'SignUp.html', context)

def index(request):
    return render(request, 'login.html')


def SignUp(request):
    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')
    
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)