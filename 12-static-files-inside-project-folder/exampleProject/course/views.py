from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def show_course(req):
    # return HttpResponse("Hello")
    return render(req, 'index.html')