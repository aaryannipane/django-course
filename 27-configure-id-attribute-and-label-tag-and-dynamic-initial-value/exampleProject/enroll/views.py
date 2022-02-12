from django.shortcuts import render

from .forms import StudentRegistration

# Create your views here.

def showForm(req):
    # load form object 
    # fm = StudentRegistration(auto_id='some_%s')
    # fm = StudentRegistration(auto_id=False)
    fm = StudentRegistration(auto_id=True, label_suffix=" > ", initial = {'name':'jhon'})
    
    return render(req, 'enroll/index.html', {'form':fm})
