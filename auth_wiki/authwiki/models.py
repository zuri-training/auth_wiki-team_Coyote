from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password

from django.conf import Settings
# Create your models here.

class Users(AbstractUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50)
    password = models.TextField(validators=[validate_password])
    password2 = models.TextField()
    isLoggedIn = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'