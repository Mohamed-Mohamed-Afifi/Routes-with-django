from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .models import car
from . import models


def aboutView(request):
    datas = car.objects.all()
    admins = {'data': datas}
    return render(request, 'about/index.html', admins)


def products(request):
    return HttpResponse("productOne")
