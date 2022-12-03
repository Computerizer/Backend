from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path("post/<str:title>", views.post, name='post'),
    path('about', views.about, name='about'),
    path('recents', views.recents, name='recents')
]