from django.urls import path
from django.shortcuts import render
from .views import search_book

urlpatterns = [
    path('search', search_book, name='search-book'),
     path('', lambda request: render(request, 'dashboard.html'), name='dashboard'),
]


