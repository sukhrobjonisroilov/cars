from django import forms

from core.models.cars import Brand


class BrendForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
