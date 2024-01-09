from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})

def about_me(request):
    return render(request, 'about_me.html', {})

def contact(request):
    return render(request, 'contact.html', {})