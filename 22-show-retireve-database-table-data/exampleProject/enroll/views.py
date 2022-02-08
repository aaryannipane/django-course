from django.shortcuts import render
from enroll.models import Student

# Create your views here.
def studentinfo(req):
    stud = Student.objects.all()
    return render(req, 'enroll/studetails.html', {'stu':stud})