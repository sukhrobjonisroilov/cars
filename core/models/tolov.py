from  django.db import  models

from core.helper.helper import card_mask
from .auth import User
class Card(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=128,default='Rental Cash')
    number  = models.CharField(max_length=20)#86000417
    mask = models.CharField(max_length=20,null=True,blank=True)#8600***
    expire = models.CharField(max_length=5)
    token = models.CharField(max_length=256,unique=True)
    balance=models.BigIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='cards')

    def save(self,*args,**kwargs):
        self.mask =card_mask(self.number)
        return  super(Card,self).save(*args,**kwargs)


    def str(self):
        return self.mask

class Minitoring(models.Model):
    tr_id = models.CharField(max_length=128,unique=True)
    sender = models.ForeignKey(Card,on_delete=models.SET_NULL,null=True,related_name='sender')
    receiver = models.ForeignKey(Card,on_delete=models.SET_NULL,null=True,related_name='receiver')
    amount=models.IntegerField(default=0)
    status = models.SmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def str(self):
        return self.tr_id