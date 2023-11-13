from django import forms

from core.models.cars import Brand,Car
from core.models.auth import User

class BrendForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields ='__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['phone','fio','g_year','g_seria','g_ctg','user_type']