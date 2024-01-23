from django.shortcuts import render

def portfolio(request):
    return render(request, 'portfolio_section/portfolio.html', {})