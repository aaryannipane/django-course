from django.urls import path
from . import views

urlpatterns = [
    path('', views.course, name='course'),
]