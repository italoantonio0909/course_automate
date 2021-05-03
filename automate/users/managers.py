from django.contrib.auth.models import BaseUserManager as BUM
from django.db import models

from .utils import validate_password


class BaseUserManager(BUM):

    def create_user(
        self,
        email: str,
        first_name: str,
        last_name: str,
        is_active=True,
        is_admin=False,
        password=None,
    ):

        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(
            email=email,
            first_name=first_name.title(),
            last_name=last_name.title(),
            is_admin=is_admin,
            is_active=is_active
        )
        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(
        self,
        email,
        first_name: str,
        last_name: str,
        password: str
    ):

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_active=True,
            is_admin=True
        )
        user.is_superuser = True
        user.save(using=self._db)

        return user
