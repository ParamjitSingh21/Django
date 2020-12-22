from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.Form):

    firstname = forms.CharField(max_length=30, required=False, help_text='Optional.')
    lastname = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(max_length=30, required=False, help_text='Optional.')
    password2 = forms.CharField(max_length=30, required=False, help_text='Optional.')
       
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'password1', 'password2', )