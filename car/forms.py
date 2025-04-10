from django import forms

from . import models


class CarForm(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = ['brand', 'price', 'description', 'image', 'name', 'year', 'milage', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': "Опишіть стан, історію та особливості вашого автомобіля."}),
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Camry'}),
            'year': forms.NumberInput(attrs={'placeholder': 'e.g. 2019'}),
            'price': forms.NumberInput(attrs={'placeholder': 'e.g. 18500'}),
            'milage': forms.NumberInput(attrs={'placeholder': 'e.g. 45000'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. Київ, Україна'}),
        }