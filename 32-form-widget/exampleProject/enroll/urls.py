from sys import path_hooks
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]