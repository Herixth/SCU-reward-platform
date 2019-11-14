# mysite_login/urls.py

from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
#    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
]