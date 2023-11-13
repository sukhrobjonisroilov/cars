from django.db import models
from .auth import User
from datetime import datetime as dt


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='cars')
    raqam = models.CharField(verbose_name='Davlat raqam', max_length=15)
    xk = models.TextField()
    price = models.IntegerField(default=0, verbose_name='kunlik ijara')
    status = models.BooleanField(default=True)
    yili = models.IntegerField(verbose_name='Chiqarilgan yili')

    def __str__(self):
        return self.name


class Arenda(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, blank=True, null=True)
    # date_from = models.DateField(default=dt.today().date())
    date_to = models.DateField(default=dt.today().strftime(f"%Y-%m-0{dt.today().day + 1}"))
    summa = models.BigIntegerField(default=0)
    payt_type = models.CharField(max_length=50, choices=[
        ('Naqd', 'Naqd'),
        ('Plastik', 'Plastik'),
        ('Bolib tolash', 'Bolib tolash')
    ])

    def __str__(self):
        return f'{self.summa}ga {self.payt_type}'
