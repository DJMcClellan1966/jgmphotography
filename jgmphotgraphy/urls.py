"""jgmphotgraphy URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from photologue.sitemaps import GallerySitemap, PhotoSitemap
from portfolio import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('portfolio/', include('portfolio.urls')),
    path('accounts/', include('allauth.urls')),
    path('photologue/', include('photologue.urls')),
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

sitemaps = {
    'photologue_galleries': GallerySitemap,
    'photologue_photos': PhotoSitemap,
}
