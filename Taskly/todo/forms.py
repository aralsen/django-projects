from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from captcha.fields import CaptchaField
from .models import Task, Profile


class CreateUserForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', ]
        exclude = ['password1', 'password2', ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', ]
        exclude = ['user', ]


class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control-file"}))

    class Meta:
        model = Profile
        fields = ['profile_pic', ]
