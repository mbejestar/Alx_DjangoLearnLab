from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # Users biography
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Profile pictureupload
    following = models.ManyToManyField(
        'self',  # Self-referential relationship
        symmetrical=False,  
        related_name='followers',  # reverse relationship for followers
        blank=True
    )

    def __str__(self):
        return self.username
