from django.urls import path
from django.shortcuts import render
from .views import search_book
from .views import dashboard_view 
from dashboard import views

urlpatterns = [
    path('search', search_book, name='search-book'),
    path('', dashboard_view, name='dashboard'),
    path('save_status/', views.save_status, name='save_status'),

]


