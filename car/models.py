from django.db import models
from django.contrib.auth.models import User
from brand.models import Brand

# Create your models here.

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Марка')
    name = models.CharField(max_length=100, verbose_name='Назва')
    milage = models.PositiveIntegerField(default=0, verbose_name='Пробіг (км)')
    year = models.PositiveIntegerField(default=0, verbose_name='Рік випуску')
    location = models.CharField(max_length=100, verbose_name='Місцезнаходження')
    description = models.TextField(verbose_name='Опис')
    image = models.ImageField(upload_to='cars/media/uploads', blank=True, null=True, verbose_name='Зображення')
    price = models.FloatField(verbose_name='Ціна')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    buyer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer', blank=True, null=True, verbose_name='Покупець')

    class Meta:
        verbose_name = 'Автомобіль'
        verbose_name_plural = 'Автомобілі'

    def __str__(self):
        return self.name