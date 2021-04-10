from django.contrib import admin
from django.urls import path,include
from . import views
from posts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.postHome,name='postHome'),
    path('postComment',views.postComment,name="postComment"),
    path('<str:slug>',views.post,name='post'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
