from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fullname = models.CharField(max_length=128)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.fullname + ' (' + self.username + ')'