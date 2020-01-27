from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('terms', views.terms, name = 'terms'),
    path('privacy', views.privacy, name = 'privacy'),


]
