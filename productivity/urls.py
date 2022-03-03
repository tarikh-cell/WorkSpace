from django.urls import path

from .views import ProductivityList, CreateProductivity

app_name = 'productivity_api'

urlpatterns = [
    path('get/', ProductivityList.as_view(), name='list'),
    path('new/', CreateProductivity.as_view(), name='create'),
]