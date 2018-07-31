from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls.base import reverse
import datetime

now = datetime.datetime.now()
context = {'like': 'Django 真棒！', 'now': now}
def main(request):
    return render(request, 'main/main.html', context)

def about(request):
    return render(request, 'main/about.html')

def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, '請以管理者身份登入')
            return redirect(reverse('account:login') + '?next=' + request.get_full_path())
        return func(request, *args, **kwargs)
    return auth