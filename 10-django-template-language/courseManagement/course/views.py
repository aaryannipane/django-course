from django.shortcuts import render

# Create your views here.
from datetime import datetime

# method 1
def viewCourse(request):
    d = datetime.now()
    amount = 233.34434
    data = {'cname': 'Django', 'dt': d, 'price':amount}
    return render(request, 'course/django.html', context= data)