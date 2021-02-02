from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models import Model


class Test(Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
    birth = models.DateTimeField(verbose_name="Дата рождения", null=True, blank=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    zip_code = models.CharField(max_length=6)
    username = models.CharField(blank=True, null=True, max_length=150)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["zip_code", "username"]

    def __str__(self):
        return self.email
