"""jgmphotgraphy URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('portfolio/', include('portfolio.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),

] 
