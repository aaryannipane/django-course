from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showForm(req):
    fm = StudentRegistration()
    return render(req, 'index.html', {'form':fm})