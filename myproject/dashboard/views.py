from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Book, Status
from django.shortcuts import render, redirect
from users.models import User
from users.models import User
import json


def dashboard_view(request):
    token = request.COOKIES.get('auth_token')
    user = User.objects.filter(token=token).first()

    if not user:
        return redirect('/login')

    return render(request, 'dashboard.html', {'user': user})

def search_book(request):
    query = request.GET.get('q')
    books=[]

    if query:
        books = Book.objects.filter(name__icontains=query)  
    return render(request, 'search_request.html', {'books': books})

def save_status(request):
    if request.method == 'POST':
        token = request.COOKIES.get('auth_token')
        user = User.objects.filter(token=token).first()

        if not user:
            return JsonResponse({'message': 'Kullanıcı bulunamadı'}, status=401)

        data = json.loads(request.body)
        bookname = data.get('bookname')
        author = data.get('author')
        page = int(data.get('page'))
        status_value = data.get('status')

        # Kitabı bulma ya da oluştur
        book, _ = Book.objects.get_or_create(name=bookname, author=author, page=page)

        # Aynı kullanıcı ve kitap için varsa eski status kaydını silme
        Status.objects.filter(userid=user, bookid=book).delete()

        # Yeni kaydı oluşturma
        Status.objects.create(
            userid=user,
            username=user.name,
            bookid=book,
            bookname=book.name,
            bookpage=book.page,
            status=status_value
        )

        return JsonResponse({'message': 'Durum başarıyla güncellendi'})
