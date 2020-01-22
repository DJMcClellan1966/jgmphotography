from django.urls import path

from . import views

urlpatterns = [
    path('<int:portfolio_id>/', views.detail, name='detail'),
    path('', views.privacy, name ='privacy'),
    path('jobs/', views.terms, name ='terms'),
]
