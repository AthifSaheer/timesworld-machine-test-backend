from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

role_choice = [
    ('student','student'),
    ('staff','staff'),
    ('admin','admin'),
    ('editor','editor'),
]

class CustomUser(AbstractUser):
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField('email address', blank=False)       
    role = models.CharField(max_length=10, choices=role_choice)
    country = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    