from django.shortcuts import render

# Create your views here.
def showCourseOne(request):
    return render(request, 'course/courseOne.html')

def showCourseTwo(request):
    return render(request, 'course/courseTwo.html')