from re import search
from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms  import TextInput, Textarea, CharField, forms
from django import forms
from django.db import models

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'user_name', 'first_name')
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')

    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields' : ('is_staff', 'is_active')}),
    )

admin.site.register(User)