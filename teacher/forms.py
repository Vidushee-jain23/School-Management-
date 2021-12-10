from django import forms
from django.forms import widgets
from django.forms.widgets import PasswordInput, Textarea
from .models import TeacherInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateTeacher(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = '__all__'
    

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Retype Password', widget= PasswordInput)
    class Meta:
        model = User
        fields = ['username']