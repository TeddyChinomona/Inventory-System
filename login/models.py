from django.contrib.auth.models import AbstractUser, BaseUserManager,PermissionsMixin
from django.db import models
from django.utils import timezone



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.username