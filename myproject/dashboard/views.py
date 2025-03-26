from django.shortcuts import render
from dashboard.models import Book

def search_book(request):
    query = request.GET.get('q')
    books=[]

    if query:
        books = Book.objects.filter(name__icontains=query)  
    return render(request, 'search_request.html', {'books': books})
