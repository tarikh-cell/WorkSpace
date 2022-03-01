from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.TextField(max_length=250) 
    description = models.JSONField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documents_posts'
    )

    def __str__(self):
        return self.title