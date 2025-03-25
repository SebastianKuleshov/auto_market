from django.db import models
from django.contrib.auth.models import User
from brand.models import Brand

# Create your models here.

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    milage = models.PositiveIntegerField(default=0)
    year = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='cars/media/uploads', blank=True, null=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    buyers = models.ManyToManyField(
        User, related_name='bought_cars', blank=True)

    def __str__(self):
        return self.name