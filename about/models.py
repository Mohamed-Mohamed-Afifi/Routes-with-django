from email.policy import default
from django.db import models

# Create your models here.


class car(models.Model):
    name = models.CharField(max_length=50, default="mohamed"),
    gender = models.CharField(max_length=10, default="male")
