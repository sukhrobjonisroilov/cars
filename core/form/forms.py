from django import forms

from core.models.cars import Brand, Car


class BrendForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'