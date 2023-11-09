from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    AbstractBaseUser
    )
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class CustomUser(AbstractUser):
    profile_pic       = models.ImageField  (upload_to = r'Users/profile-pics', blank=True, default=r'Users/profile-pics/default-profile-pic.jpg')
    sub_to_newsletter = models.BooleanField(default=True)
    own_pc            = models.BooleanField(default=False) 

    def __str__(self):
        return self.username

