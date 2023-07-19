from django.urls import path, include
from .views import *

urlpatterns = [
    path('algorithm/activate', algorithm_api, name='algorithm function'),
    path('algorithm/reset-uses', reset_uses, name='reset algorithm uses' )
]















