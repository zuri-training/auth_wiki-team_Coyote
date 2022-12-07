from django.db import models
from datetime import date, datetime
# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_loggedin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Auth_library(models.Model):
    code = models.CharField(max_length=60)
    functionality = models.CharField(max_length=200)
    code_snippet = models.CharField(max_length=5000)
    comments = models.CharField(max_length=5000)
    categories = models.CharField(max_length=60)
    created_by = models.ForeignKey(Users, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.code_name} {self.created_by}'
         
class Comment(models.Model):
    comment_title = models.ForeignKey(Auth_library, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content

class Reactions(models.Model):
    upvote = models.ManyToManyField(Comment, related_name='comment_upvote' )
    downvote = models.ManyToManyField(Comment, related_name='comment_downvote')

    def total_reactions(self):
        return f'{self.upvote.count()} {self.downvote.count()}'
