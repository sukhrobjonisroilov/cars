from  django.urls import path
from core.views.auth import sing_in
from core.views.home import home
urlpatterns = [
    path('',sing_in,name='login'),
    path('home/',home,name='home')
]