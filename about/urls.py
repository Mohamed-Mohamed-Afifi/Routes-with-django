
from django.urls import path
from . import views
urlpatterns = [
    path('', views.aboutView, name='about'),
    path('productone/', views.aboutView, name='productOne')
]
