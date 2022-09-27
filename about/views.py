from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def aboutView(request):
    return HttpResponse("About page")
def products(request):
    return HttpResponse("productOne")