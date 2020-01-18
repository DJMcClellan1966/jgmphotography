from django.shortcuts import render, get_object_or_404

from .models import Portfolio

def home(request):
    portfolios = Portfolio.objects
    return render(request, 'jobs/home.html', {'portfolios':portfolios})

def detail(request, portfolio_id):
    details = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'jobs/details.html', {'portfolio':details})

def privacy(request):
    return render(request, 'jobs/privacy.html')

def terms(request):
    return render(request, 'jobs/terms.html')
