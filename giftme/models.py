from django.contrib.auth.models import AbstractUser
from django.db import models


class Test(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
    birth = models.DateTimeField(verbose_name="Дата рождения", null=True, blank=True)

    def __str__(self):
        return self.name


class Wish(models.Model):
    STATUS = [
        ('waiting', 'В ожидании'),
        ('gifted', 'Подарено'),
        ('reserved', 'Забронировано')
    ]

    name = models.CharField(max_length=255, verbose_name="Мое желание")
    photo = models.ImageField(upload_to='wish_pic/', verbose_name='Фото моего желания', null=True, blank=True)
    #holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE, null=True, blank=True)
    link_to_wish = models.URLField(verbose_name="Ссылка на желание")
    status = models.CharField(max_length=50, verbose_name="Статус подарка", choices=STATUS, default='waiting')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мое желание'
        verbose_name_plural = 'Мои желания'


class GiftMeUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name="Электронная почта")
    about = models.CharField(max_length=200, verbose_name="О себе")
    avatar = models.ImageField(upload_to="avatar/")
    link_to_social = models.CharField(max_length=255, verbose_name="Ссылка на профиль в соц. сетях")
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE, blank=True, null=True, related_name='wishes')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Holiday(models.Model):
    name_of_holiday = models.CharField(max_length=30, verbose_name="Название праздника")
    date_of_holiday = models.DateField("Дата", null=True, blank=True)
