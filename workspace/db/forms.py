from django import forms
from django.forms import ModelForm

from db.models import User

class UserForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)
    
    class Meta:
        model = User
        fields = ['username', 'password']