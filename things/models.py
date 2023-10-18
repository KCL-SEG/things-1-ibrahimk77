from django.core.validators import RegexValidator
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser

class Thing(Model):
    name = models.CharField(max_length=30, blank=False,unique=True)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])