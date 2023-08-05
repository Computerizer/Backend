from .models import cpu, gpu, ram, motherboard as mobo, case, aircooler, watercooler, ssd, hdd, fan, case, psu
from datetime import datetime, timedelta, date
from .scraper import *
from builtins import Exception
from django.core.exceptions import *
from django.db import *


def update(part) -> float:
    oldPrice = part.current_price
    try:
        amazon = amazonPrice(part.url)
    except Exception:
        print(f'Error in Amazon Web Scrpaer Price ({datetime.now()})')
        print('-')
        print(Exception)
    try:
        newegg = neweggPrice(part.url)
    except Exception:
        print(f'Error in Newegg Web Scrpaer Price ({datetime.now()})')
        print('-')
        print(Exception)
    if amazon < newegg:
        link = part.amazon_url
        newPrice = amazon
        part.update(current_price=newPrice, previous_price=oldPrice,\
        amazon_price=amazon, newegg_price=newegg, lowest_Price_Link=link)
        part.save()
        return
    elif amazon > newegg:
        link = part.newegg_url
        newPrice = newegg
        part.update(current_price=newPrice, previous_price=oldPrice,\
        amazon_price=amazon, newegg_price=newegg, lowest_Price_Link=link)
        part.save()
        return

class updaterException(Exception):
    def __init__(self, message, extra_info):
        super().__init__(message)
        self.extraInfo = extra_info

def cpuUpgrade() -> float:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = cpu.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for cpuObject in parts:
            update(cpuObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'CPU ----> {DBError}')

def gpuUpgrade() -> float:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = gpu.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for gpuObject in parts:
            update(gpuObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'GPU ----> {DBError}')

def ramUpgrade() -> float:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = ram.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for ramObject in parts:
            update(ramObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'RAM ----> {DBError}')

def moboUpgrade() -> float:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = mobo.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for moboObject in parts:
            update(moboObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'MOBO ----> {DBError}')

def caseUpgrade() -> float:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = case.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for caseObject in parts:
            update(caseObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'CASE ----> {DBError}')

def wcUpgrade() -> float:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = watercooler.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for wcObject in parts:
            update(wcObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'WC ----> {DBError}')

def acUpgrade() -> float:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = aircooler.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for acObject in parts:
            update(acObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'AC ----> {DBError}')

def psuUpgrade() -> float:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = psu.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for psuObject in parts:
            update(psuObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'PSU ----> {DBError}')

def ssdUpgrade() -> float:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = ssd.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for ssdObject in parts:
            update(ssdObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'SSD ----> {DBError}')

def hddUpgrade() -> float:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = hdd.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for hddObject in parts:
            update(hddObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'HDD ----> {DBError}')

def main() -> float:
    cpuUpgrade()
    gpuUpgrade()
    moboUpgrade()
    caseUpgrade()
    wcUpgrade()
    acUpgrade()
    psuUpgrade()
    ssdUpgrade()
    hddUpgrade()


