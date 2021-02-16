from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models import Model


class Test(Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
    birth = models.DateTimeField(verbose_name="Дата рождения", null=True, blank=True)

    def __str__(self):
        return self.name


class GiftMeUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name="Электронная почта")
    about = models.CharField(max_length=200, verbose_name="О себе")
    username = models.CharField(blank=True, null=True, max_length=150)
    avatar = models.ImageField(upload_to="avatars/")
    link_to_social = models.CharField(max_length=255, verbose_name="Ссылка на профиль в соц. сетях")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Holiday(Model):
    name_of_holiday = models.CharField(max_length=30, verbose_name="Название праздника")
    date_of_holiday = models.DateField("Дата", null=True, blank=True)
