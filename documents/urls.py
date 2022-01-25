from django.urls import path
from django.views.generic import TemplateView

app_name = 'documents'

urlpatterns = [
    path('', TemplateView.as_view(template_name="documents/index.html")),
]