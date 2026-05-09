from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    
    phone = models.CharField(max_length=500,blank=True,null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']


class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/',blank=True)

    def __str__(self):
        return self.user.username
    