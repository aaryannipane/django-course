from django.shortcuts import render

# Create your views here.

# method 1
def viewCourse(request):
    course_name = {'cname': 'Django'}
    return render(request, 'course/django.html', context=course_name)