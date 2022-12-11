from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
# Create your models here.

class Users(AbstractUser):
        first_name = models.CharField(max_length=60)
        last_name = models.CharField(max_length=60)
        username = models.CharField(max_length=20, unique=True)
        email =  models.EmailField(max_length=50)
        password = models.TextField(validators=[validate_password])
        password2 = models.TextField()
        isLoggedIn = models.BooleanField(default=False)
        

        def __str__(self):
            return f'{self.first_name} {self.last_name}'

class Auth_library(models.Model):
    code = models.ForeignKey('Code', on_delete = models.CASCADE)
    #functionality = models.CharField(max_length=500)
    #code_snippet = models.TextField(null=True, blank=True)
    comment = models.ForeignKey('Comments', on_delete = models.CASCADE, default=True)
    categories = models.ForeignKey('Categories', on_delete = models.CASCADE)
    created_by = models.ForeignKey('Users', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.code} {self.created_by}'
         
class Categories(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

class Code(models.Model):
    title = models.CharField(max_length=60)
    categories = models.ForeignKey('Categories', on_delete=models.CASCADE)
    functionality = models.CharField(max_length=500)
    code_snippet = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey('Comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.created_by}'
class Comments(models.Model):
    users=models.ForeignKey('Users', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ForeignKey('Reactions', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.content} {self.users}'

class Reactions(models.Model):
    users = models.ForeignKey('Users', on_delete=models.CASCADE)
    likes = models.ManyToManyField('Comments', related_name='liked_comment' )
    

    def total_reactions(self):
        return self.likes.count()

class Community(models.Model):
    users=models.ForeignKey('Users', on_delete=models.CASCADE)
    questions = models.TextField(null=True, blank=True)
    comment = models.ForeignKey('Comments', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.questions} {self.users}'
