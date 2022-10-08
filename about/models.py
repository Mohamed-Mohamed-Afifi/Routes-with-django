from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.


class car(models.Model):
    name = models.CharField(max_length=50, default="mohamed")
    gender = models.CharField(max_length=10, default="male")
    image = models.ImageField(upload_to='photes/%y/%m%d', default="null")
# name of row

    def __str__(self):
        return self.name
# name of table

    class Meta:
        verbose_name = "admin"
