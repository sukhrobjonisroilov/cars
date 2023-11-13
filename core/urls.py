from  django.urls import path
from core.views.auth import sing_in
from core.views.home import home
from core.views.ctg_views import ctg_view
urlpatterns = [
    path('',sing_in,name='login'),
    path('home/',home,name='home'),
    path('ctg/<key>/<status>/',ctg_view,name ='ctg')
]