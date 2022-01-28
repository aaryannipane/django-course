from django.shortcuts import render

# Create your views here.
def showCourseOne(request):
    course = {'cname':'Django Baba'} # for dynamic data
    return render(request, 'course/courseOne.html', context=course)

def showCourseTwo(request):
    return render(request, 'course/courseTwo.html')