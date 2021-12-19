from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),

    path('api/user', api.user_api, name='user api'),
]