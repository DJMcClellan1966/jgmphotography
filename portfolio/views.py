from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView, LoginView
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
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

def gallerybase(request):
    return render(request, 'jobs/gallerybase.html')

#def signup(request):
        #return render(request, 'jobs/signup.html')


#def login(request):
        #return render(request, 'jobs/login.html')

def root(request):
    return render(request, 'photologue/root.html')

def base(request):
    return render(request, 'accounts/base.html')
