from django.shortcuts import render
from .models import Project #permite traer los datos de la base de datos para asi hacerlo dinamico 

def portfolio(request):
    projects = Project.objects.all()
    
    return render(request, 'portfolio_section/portfolio.html', {'projects' : projects })