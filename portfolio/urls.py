from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('terms', views.terms, name = 'terms'),
    path('privacy', views.privacy, name = 'privacy'),
    path('favorites', views.favorites, name = 'favorites'),
    #path('login', views.login, name = 'login'),
    #path('signup', views.signup, name = 'signup'),
    path('gallerybase', views.gallerybase, name = 'gallerybase'),
    path('root', views.root, name = 'root'),
    path('base', views.base, name = 'base'),
]
