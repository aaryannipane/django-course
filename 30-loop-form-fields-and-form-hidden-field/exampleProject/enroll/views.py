from django.shortcuts import render
from .forms import StudentRegistration


# Create your views here.
def home(req):
    fm = StudentRegistration()
    return render(req, 'enroll/home.html', {'form':fm})