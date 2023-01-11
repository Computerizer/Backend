from django.urls import path, include
from .views import *

urlpatterns = [
    path('get/cpu', List_all_cpu, name='cpu'),
    path('get/gpu', List_all_gpu, name='gpu'),
    path('get/ram', List_all_ram, name='ram'),
    path('get/ssd', List_all_ssd, name='ssd'),
    path('get/hdd', List_all_hdd, name='hdd'),
    path('get/watercooler', List_all_watercooler, name='watercooler'),
    path('get/aircooler', List_all_aircooler, name='aircooler'),
    path('get/mobo', List_all_mobo, name='mobo'),
    path('get/psu', List_all_psu, name='psu'),
    path('get/fan', List_all_fan, name='fan'),
    path('get/case', List_all_case, name='case'),

]















