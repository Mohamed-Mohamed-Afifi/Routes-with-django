from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def aboutView(request):
    data = [{'name': 'mohamed', 'age': 22, 'gender': 'male'}, {'name': 'hany',
                                                               'age': 30, 'gender': 'male'}, {'name': 'gamal', 'age': 15, 'gender': 'male'}]
    user = {'data': data}
    return render(request, 'about/index.html', user)


def products(request):
    return HttpResponse("productOne")
