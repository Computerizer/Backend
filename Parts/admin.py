from django.contrib import admin
from .models import manufacturer, cpu, aircooler, watercooler, gpu, ram, hdd, ssd, motherboard, psu, case, fan

# Register your modes here.
admin.site.register(manufacturer)

admin.site.register(cpu)

admin.site.register(aircooler)

admin.site.register(watercooler)

admin.site.register(gpu)

admin.site.register(ram)

admin.site.register(hdd)

admin.site.register(ssd)

admin.site.register(motherboard)

admin.site.register(psu)

admin.site.register(fan)

admin.site.register(case)
