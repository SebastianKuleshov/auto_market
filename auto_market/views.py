from django.shortcuts import render
from car.models import Car


def home(request):
    cars = Car.objects.order_by('-price')[:3]

    return render(request, 'home.html', {'cars': cars})
