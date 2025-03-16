from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('login/', lambda request: render(request, 'login.html'), name='login'),
    path('register/', lambda request: render(request, 'create_account.html'), name='register'),
]
