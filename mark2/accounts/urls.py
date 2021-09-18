from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('explore',views.explore,name='explore'),
    path('other_profile',views.other_profile,name='other_profile'),
    path('my_profile',views.my_profile,name='my_profile'),
]