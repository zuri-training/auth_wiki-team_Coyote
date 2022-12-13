from django.db import models
from datetime import date, datetime
from django.conf import settings
# Create your models here.


class AuthLibrary(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    functionality = models.CharField(max_length=200)
    code_snippet = models.TextField()
    comments = models.CharField(max_length=5000)
    categories = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.functionality} {self.created_by} with my code snippet {self.code_snippet}'


class Comment(models.Model):
    author_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    comment_title = models.ForeignKey(AuthLibrary, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.content} {self.created_at}'
