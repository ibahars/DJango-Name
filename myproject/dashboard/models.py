from django.db import models
from django.http import JsonResponse
from users.models import User
from django.views.decorators.http import require_GET

@require_GET
def user_statistics(request):
    token = request.COOKIES.get('auth_token')
    user = User.objects.filter(token=token).first()

    if not user:
        return JsonResponse({'error': 'Kullanıcı bulunamadı'}, status=401)

    # "Okudum" olan kitap sayısı
    read_books = Status.objects.filter(userid=user, status='Okudum').count()

    # "Okudum" olan kitapların toplam sayfa sayısı
    total_read_pages = Status.objects.filter(userid=user, status='Okudum').aggregate(
        total=models.Sum('bookpage')
    )['total'] or 0

    # "Okuyacağım" olan kitap sayısı
    to_read_books = Status.objects.filter(userid=user, status='Okuyacağım').count()

    return JsonResponse({
        'read_books': read_books,
        'total_read_pages': total_read_pages,
        'to_read_books': to_read_books
    })

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    page = models.IntegerField()

    def __str__(self):
        return self.name
    
class Status(models.Model):
    STATUS_CHOICES = [
        ('Okudum', 'Okudum'),
        ('Okuyorum', 'Okuyorum'),
        ('Okuyacağım', 'Okuyacağım'),
    ]

    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    bookname = models.CharField(max_length=255)
    bookpage = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.bookname} - {self.status}"
