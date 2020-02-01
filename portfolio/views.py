from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Portfolio

def home(request):
    portfolios = Portfolio.objects
    return render(request, 'jobs/home.html', {'portfolios':portfolios})

def terms(request):
    return render(request, 'jobs/terms.html')

def privacy(request):
    return render(request, 'jobs/privacy.html')

def favorites(request):
    return render(request, 'jobs/favorites.html')
