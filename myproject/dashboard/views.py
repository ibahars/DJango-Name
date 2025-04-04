from django.shortcuts import render
from dashboard.models import Book
from django.shortcuts import render, redirect


def dashboard_view(request):
    token = request.COOKIES.get('auth_token')
    
    if token != 'your_token_value':
        return redirect('/login')  

    return render(request, 'dashboard.html')

def search_book(request):
    query = request.GET.get('q')
    books=[]

    if query:
        books = Book.objects.filter(name__icontains=query)  
    return render(request, 'search_request.html', {'books': books})
