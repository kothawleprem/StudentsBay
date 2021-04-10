from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search',views.search,name='search'),
    path('register',views.register,name='register'),
    path('handleregister',views.handleregister,name='handleregister'),
    path('login',views.ulogin,name='ulogin'),
    path('handlelogin',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
]
