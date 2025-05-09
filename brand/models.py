from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Марка')

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name
