from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from  django.db import  models


class UserM(UserManager):
    def create_user(self, username, phone, password,is_staff=False,is_superuser=False, **extra_fields):
        user = self.model(
            username=username,
            phone=phone,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username,phone, password, **extra_fields):
        return self.create_user(username,phone,password,is_staff=True,is_superuser=True)


class User(AbstractBaseUser,PermissionsMixin):
    phone = models.CharField(max_length=12, unique=True)
    username = models.CharField(max_length=120, blank=True, null=True)
    fio = models.CharField(max_length=200)
    # Prava uchun
    g_year = models.DateField(verbose_name='Guvohnoma_Yili', null=True, blank=True)
    g_seria = models.DateField(verbose_name='Guvohnoma_Seriasi', null=True, blank=True)
    g_ctg = models.CharField(max_length=25, verbose_name='Guvohnoma Categoryasi')

    # admin uchun
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    user_type = models.SmallIntegerField(choices=[
        (1, 'Admin'),
        (2, 'User')
    ], default=1)
    objects = UserM()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username','user_type']

    def get_user_name(self):
        return f'{self.fio.split()[0] if not self.username else self.username}'