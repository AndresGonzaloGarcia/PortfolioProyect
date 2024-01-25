from django.shortcuts import render
from .models import Skill


def home(request):
    return render(request, 'home.html', {})

def about_me(request):
    skills = Skill.objects.all()
    
    return render(request, 'about_me.html', {'skills': skills})

def contact(request):
    return render(request, 'contact.html', {})