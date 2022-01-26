from nturl2path import url2pathname
from django.urls import path
from .views import CustomUserCreate
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('login/', views.login_view, name="login_user"),
]