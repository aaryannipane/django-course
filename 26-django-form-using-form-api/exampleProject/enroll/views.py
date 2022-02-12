from django.shortcuts import render

from .forms import StudentRegistration

# Create your views here.

def showForm(req):
    # load form object 
    fm = StudentRegistration()
    return render(req, 'enroll/index.html', {'form':fm})
