from django.shortcuts import render

# Create your views here.
def showHome(req):
    return render(req, 'index.html')

def showCourse(req):
    return render(req, 'course.html')

def showAbout(req):
    return render(req, 'about.html')