from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(req):
#     return HttpResponse("Hello")

def index(request):
    return render(request, 'index.html', content_type='text/html')