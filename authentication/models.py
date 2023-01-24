
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


class User(AbstractUser):

    email = models.EmailField(unique=True, help_text='Your email')
    is_verify = models.BooleanField(default=False, verbose_name='account verified')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:

        ordering = ["id"]