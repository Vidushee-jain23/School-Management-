from django.contrib import admin
from .models import StudentInfo
# Register your models here.
@admin.register(StudentInfo)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','dob','fatherName','fatherOccupation','motherName','motherOccupation','address','city','state','mobileNo')
