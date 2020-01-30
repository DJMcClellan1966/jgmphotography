from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:saved_id>', views.saved_image, name = 'saved_image'),
    path('saved_image', views.saved_image, name = 'saved_image'),

]
