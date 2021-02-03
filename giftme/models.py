from django.contrib.auth.models import AbstractUser
from django.db import models


class GiftMeUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name="Электронная почта")
    about = models.CharField(max_length=200, verbose_name="О себе")
    avatar = models.ImageField(upload_to="avatar/")
    link_to_social = models.CharField(max_length=255, verbose_name="Ссылка на профиль в соц. сетях")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email