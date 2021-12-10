from django.contrib import admin
from .models import TeacherInfo
# Register your models here.
@admin.register(TeacherInfo)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','dob','subject','qualification','experience','mobileNo')

