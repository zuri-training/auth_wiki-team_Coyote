from django.db import models
from datetime import date, datetime
# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'