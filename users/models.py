from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE) #one user has only one profile and if an user is deleted , corresponding profile is deleted but vice versa is not true
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

    
