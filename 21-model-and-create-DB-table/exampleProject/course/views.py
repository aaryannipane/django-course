from django.shortcuts import render

# Create your views here.
def course(req):
    return render(req, 'index.html')