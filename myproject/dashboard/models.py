from django.db import models
from users.models import User


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
