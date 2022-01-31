from django.shortcuts import render

# Create your views here.
from datetime import datetime

# method 1
def viewCourse(request):
    d = datetime.now()
    amount = 233.34434

    student = {
        'name':'Aryan',
        'age':19,
        'education':'graduate'
    }

    names = ['Babu', 'Onkar', 'Aryan', 'Akshay', 'Abhishek']

    car = {'car1':{'name':'ferrari', 'price':200}, 'car2':{'name':'BMW', 'price':100}, 'car3':{'name':'Mercedes', 'price':150}, }

    data = {'cname': 'Django', 'dt': d, 'price':amount, 'vidhyatri':student, 'students':names, 'cars':car}
    return render(request, 'course/django.html', context= data)