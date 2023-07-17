from django.urls import path, include
from .views import *

urlpatterns = [
    path('algorithm/activate', algorithm, name='algorithm'),
]















