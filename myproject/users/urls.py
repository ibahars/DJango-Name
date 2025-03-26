from django.urls import path
from django.shortcuts import render
from .views import create_account_view
from .views import login_view


urlpatterns = [
    path('login/', login_view , name='login'),
    path('register/', create_account_view, name='register'),
]
