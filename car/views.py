from django.shortcuts import render
from .models import Car
from django.contrib import messages

# Create your views here.

def add_car(request):
    pass

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)

    if request.method == 'POST':
        if 'buy_now' in request.POST:
            if car.quantity > 0:
                car.buyers.add(request.user)
                car.quantity -= 1
                car.save()
                messages.success(request, 'Car purchased successfully!')
            else:
                messages.error(request, 'Car is out of stock!')

    
    return render(request, 'car_detail.html', {'car': car})

def browse_cars(request):
    pass