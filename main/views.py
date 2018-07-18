from django.shortcuts import render

context = {'like': 'Django 真棒！'}
def main(request):
    return render(request, 'main/main.html', context)

def about(request):
    return render(request, 'main/about.html')