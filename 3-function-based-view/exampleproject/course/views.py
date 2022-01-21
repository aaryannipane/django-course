from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    return HttpResponse('Hello World')

def show_html(request):
    return HttpResponse('<h1 style="background: lightblue; text-align:center;">Hello Puthon</h1>')

# for home page
def index(req):
    return HttpResponse('<body style="background: #555;">Home Page</body>')