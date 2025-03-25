from django.urls import path
from django.shortcuts import render
from .views import create_account_view


urlpatterns = [
    path('login/', lambda request: render(request, 'login.html'), name='login'),
    path('register/', create_account_view, name='register'),
]
