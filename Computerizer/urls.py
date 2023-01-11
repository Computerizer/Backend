"""Computerizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap, StaticSitemap
from .views import robots_txt

sitemaps = {
    'Blog':BlogSitemap,
    'Static':StaticSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('Blog.urls')),
    path('auth/', include('Oauth.urls')),
    path('parts/', include('Parts.urls')),
    path('TPA/', include('TPA.urls')),
    path('', include('frontend.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", robots_txt),
]