from django.shortcuts import render
from .models import Skill, Academic


def home(request):
    return render(request, 'home.html', {})

def about_me(request):
    skills = Skill.objects.all()
    academics = Academic.objects.all()
    
    return render(request, 'about_me.html', {'skills': skills, 'academics': academics})

def contact(request):
    return render(request, 'contact.html', {})