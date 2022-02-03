from django.shortcuts import render

# Create your views here.
def show(req):
    return render(req, 'index.html')