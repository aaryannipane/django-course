from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course(request):
    return HttpResponse('Course Page')

def contact(request):
    return HttpResponse('Contact Us Page')

def index(request):
    return HttpResponse('<h1 style="font-family: sans-serif; font-size: 50px; text-align: center; margin-top: 100px;">Welcome To Website</h1>')