from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import BaseUserManager


class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=120, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = BaseUserManager()

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin
