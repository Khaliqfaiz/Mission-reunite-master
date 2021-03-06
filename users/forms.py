from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
   # first_name = forms.CharField(max_length=30) #can be specified as element in the fields
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        first_name = forms.CharField(max_length=30)
        last_name = forms.CharField(max_length=30)
        fields = ['first_name', 'last_name']
