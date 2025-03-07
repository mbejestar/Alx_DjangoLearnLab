from django.db import models  
from django.contrib.auth.models import AbstractUser  

class CustomUser(AbstractUser):  
    date_of_birth = models.DateField(null=True, blank=True)  
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
