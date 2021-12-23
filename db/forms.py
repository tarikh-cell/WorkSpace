from django import forms
from django.forms import ModelForm

from db.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']