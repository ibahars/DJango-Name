from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name