from django.contrib.auth.models import AbstractUser
from django.db import models

class Details(models.Model):

    username=models.CharField(max_length=200)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username

