from unicodedata import name
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.showHome, name='home'),
    path('course/', views.showCourse),
]

# we can do this same thing in urls.py file of project folder except for include() functions