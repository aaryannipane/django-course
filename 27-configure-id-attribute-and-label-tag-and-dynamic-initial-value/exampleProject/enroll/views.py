from django.shortcuts import render

from .forms import StudentRegistration

# Create your views here.

def showForm(req):
    # load form object 
    # fm = StudentRegistration(auto_id='some_%s')
    # fm = StudentRegistration(auto_id=True)
    fm = StudentRegistration(auto_id=False)
    return render(req, 'enroll/index.html', {'form':fm})
