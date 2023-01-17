from ..models import cpu, gpu, ram, motherboard, case, \
    aircooler, watercooler, ssd, hdd, fan, case, psu
from datetime import datetime
from .main import *


def cpuUpdate():
    cpus = cpu.objects.get()


