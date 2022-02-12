from django.shortcuts import render
from enroll.models import Student

# Create your views here.
def studentinfo(req):
    # get all data
    stud = Student.objects.all()
    # get single data using primary key value
    # stud = Student.objects.get(pk=2)
    return render(req, 'enroll/studetails.html', {'stu':stud})