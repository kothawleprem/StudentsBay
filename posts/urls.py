from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.postHome,name='postHome'),
    path('<str:slug>',views.post,name='post')
]
