from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from account.forms import UserForm

def register(request):
    template = 'account/register.html'
    if request.method == 'GET':
        return render(request, template, {'userForm':UserForm()})

    #POST
    userForm = UserForm(request.POST)
    if not userForm.is_valid():
        return render(request, template, {'userForm':userForm})
    userForm.save()
    messages.success(request, '歡迎註冊')
    return redirect('main:main')

def login(request):
    template = 'account/login.html'
    if request.method == 'GET':
        return render(request, template, {'nextURL':request.GET.get('next')})
    #POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:
        messages.error(request, '請填寫資料！')
        return render(request, template)
    user = authenticate(username=username, password=password)
    if not user:
        messages.error(request, '登入失敗')
        return render(request, template)
    #login success
    auth_login(request, user)
    nextURL = request.POST.get('nextURL')
    if nextURL:
        return redirect(nextURL)
    messages.success(request, '登入成功')
    return redirect('main:main')

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, '歡迎再度光臨')
    return redirect('main:main')