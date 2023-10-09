from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser

class Thing(Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()