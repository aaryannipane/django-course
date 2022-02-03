from django.shortcuts import render
# Create your views here.
def showCourse(request):
    return render(request, 'course/index.html')