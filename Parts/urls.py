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
    path('get/psu', List_all_psu, name=''),
    path('get/fan', List_all_fan, name=''),
    path('get/case', List_all_case, name=''),

    path('get/cpu/<str:manufacturer>', List_specific_cpu, name='specific-cpu'),
    path('get/gpu/<str:manufacturer>', List_specific_gpu, name='specific-gpu'),
    path('get/ram/<str:manufacturer>', List_specific_ram, name='specific-ram'),
    path('get/ssd/<str:manufacturer>', List_specific_ssd, name='specific-ssd'),
    path('get/hdd/<str:manufacturer>', List_specific_hdd, name='specific-hdd'),
    path('get/watercooler/<str:manufacturer>', List_specific_watercooler, name='specific-watercooler'),
    path('get/aircooler/<str:manufacturer>', List_specific_aircooler, name='specific-aircooler'),
    path('get/mobo/<str:manufacturer>', List_specific_mobo, name='specific-mobo'),
    path('get/psu/<str:manufacturer>', List_specific_psu, name='specific-psu'),
    path('get/fan/<str:manufacturer>', List_specific_fan, name='specific-fan'),
    path('get/case/<str:manufacturer>', List_specific_case, name='specific-case'),

]
