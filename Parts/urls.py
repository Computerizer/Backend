from django.urls import path, include
from .views import *

urlpatterns = [
    path('get-all/<str:part>', List_all_part, name='All of Part'),
    #path('get-all/<str:part>/<str:manufacturer>', None, name=''),

]
