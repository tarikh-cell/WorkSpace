from django.db import models
from django.conf import settings

# Create your models here.
class Productivity(models.Model):
    date = models.DateField(auto_now_add=True)
    duration = models.IntegerField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_productivity'
    )