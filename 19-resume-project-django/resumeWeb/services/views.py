from django.shortcuts import render

# Create your views here.
def services(req):
    context = {'service':'active'}
    return render(req, 'services/services.html', context)