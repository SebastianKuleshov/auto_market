from django.urls import path
from . import views

urlpatterns = [
    path('add_car/', views.add_car, name='add_car'),
    path('car_detail/<int:car_id>/', views.car_detail, name='car_detail'),
    path('browse-cars/', views.browse_cars, name='browse_cars'),
]
