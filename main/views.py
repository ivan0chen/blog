from django.shortcuts import render
import datetime

now = datetime.datetime.now()
context = {'like': 'Django 真棒！', 'now': now}
def main(request):
    return render(request, 'main/main.html', context)

def about(request):
    return render(request, 'main/about.html')