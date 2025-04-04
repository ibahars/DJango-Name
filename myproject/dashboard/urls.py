from django.urls import path
from django.shortcuts import render
from .views import search_book
from .views import dashboard_view

urlpatterns = [
    path('search', search_book, name='search-book'),
     path('', dashboard_view, name='dashboard'),
]


