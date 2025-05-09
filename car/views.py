from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from brand.models import Brand
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
            if not car.buyer:
                car.buyer = request.user
                car.save()
                messages.success(request, 'Авто успішно придбано!')
            else:
                messages.info(request, 'Авто вже придбано!')

    
    return render(request, 'car_detail.html', {'car': car})

def browse_cars(request):
    brands = Brand.objects.all()

    selected_brand = request.GET.get('brand')
    available = request.GET.get('available')

    if selected_brand:
        brand = get_object_or_404(Brand, name=selected_brand)
        cars = Car.objects.filter(brand=brand).select_related('brand', 'author')
    else:
        cars = Car.objects.all().select_related('brand', 'author')

    if available:
        cars = cars.filter(buyer__isnull=True)

    return render(request, 'browse_cars.html', {
        'cars': cars,
        'brands': brands,
        'selected_brand': selected_brand,
        'available': available,
    })