from django.shortcuts import render, redirect
from .models import Car
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

@login_required
def add_car(request):
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST or None, request.FILES or None)
        if car_form.is_valid():
            car_form.instance.author = request.user
            car_form.save()
            return redirect('home')
        else:
            return render(request, 'sell_car.html', {
                'form': car_form,
                'title': 'Add Car',
                'errors': car_form.errors,
            })
    else:
        car_form = forms.CarForm()

    return render(request, 'sell_car.html', {'form': car_form})

    

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