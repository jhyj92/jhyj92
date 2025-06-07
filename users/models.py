from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model extending Django's AbstractUser."""

    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.username
