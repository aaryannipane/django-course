from django.contrib import admin
from enroll.models import Student

# Register your models here.

# register with decorator (prefered)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid', 'stuname', 'stuemail', 'stupass')


# register normaly
# admin.site.register(Student, StudentAdmin)