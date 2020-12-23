from django.db import models

# Create your models here.


class UserInfo(models.Model):

    firstname = models.CharField(max_length=30)
    lastname1 = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    username = models.CharField(max_length=20)