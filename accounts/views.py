from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': '아이디 혹은 비밀번호가 잘못되었습니다.'})
    else:
        return render(request, 'login.html' )


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login.html')
    return render(request, 'login.html')