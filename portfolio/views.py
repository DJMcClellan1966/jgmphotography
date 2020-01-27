from django.shortcuts import render, get_object_or_404
from .models import Portfolio

def home(request):
    portfolios = Portfolio.objects
    return render(request, 'jobs/home.html', {'portfolios':portfolios})

def terms(request):
    return render(request, 'jobs/terms.html')

def privacy(request):
    return render(request, 'jobs/privacy.html')    
