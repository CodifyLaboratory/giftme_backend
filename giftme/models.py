from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models

from rest_framework_simplejwt.tokens import RefreshToken


class Holiday(models.Model):
    name_of_holiday = models.CharField(max_length=30, verbose_name="Название праздника")
    date_of_holiday = models.DateField("Дата", null=True, blank=True)

    def __str__(self):
        return self.name_of_holiday

    class Meta:
        verbose_name = "Мой праздник"
        verbose_name_plural = "Мои праздники"


class Wish(models.Model):
    STATUS = [
        ('waiting', 'В ожидании'),
        ('gifted', 'Подарено'),
        ('reserved', 'Забронировано')
    ]

    name = models.CharField(max_length=255, verbose_name="Мое желание")
    photo = models.ImageField(upload_to='wish_pic/', verbose_name='Фото моего желания', null=True, blank=True)
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE, null=True, blank=True)
    link_to_wish = models.URLField(verbose_name="Ссылка на желание")
    status = models.CharField(max_length=50, verbose_name="Статус подарка", choices=STATUS, default='waiting')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мое желание'
        verbose_name_plural = 'Мои желания'


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email является объязательным полем')

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None):
        if not password:
            raise TypeError('Пароль не должна быть пустым')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class GiftMeUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True, verbose_name="Электронная почта")
    about = models.CharField(max_length=200, verbose_name="О себе")
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/")
    link_to_social = models.CharField(max_length=255, verbose_name="Ссылка на профиль в соц. сетях")
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE, blank=True, null=True, related_name='wishes')

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
