from django import forms
from django.contrib.auth.forms import  UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2','profile')
        username = forms.TextInput(attrs={'placeholder': 'username'})
        #username=forms.TextInput(attrs={'placeholder':'username'})
        email=forms.CharField(max_length=200,required=True, widget=forms.EmailInput(attrs={'placeholder':'email'}))
        password1=forms.PasswordInput(attrs={'placeholder':"password"})
        password2=forms.PasswordInput(attrs={'placeholder':"confirm password"})
        profile=forms.CharField(widget=forms.ImageField())



# login
class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(required=True,max_length=200,widget=forms.PasswordInput(attrs={'placeholder':"Password"}))