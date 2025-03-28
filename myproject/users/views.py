from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


def create_account_view(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Bu email ile zaten kayıtlı bir kullanıcı var.')
            return render(request, 'create_account.html')

        
        hashed_password = make_password(password)
        user = User(name=name, email=email, password=hashed_password)
        user.save()
        
        messages.success(request, 'Kayıt başarılı! Giriş yapabilirsiniz.')
        return redirect('/login')

    return render(request, 'create_account.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email) 
        except User.DoesNotExist:
            messages.error("böyle bir kullanıcı bulunamadı!")
            return redirect('/login')
        
        if check_password(password , user.password):
            messages.success(request, 'giriş başarılı, hoş geldiniz!')
            return redirect('/')
        else:
            messages.error(request ,'şifre yanlış!')
            return redirect('/login')
    
    return render(request, 'login.html')

        
