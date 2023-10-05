from .models import cpu, gpu, ram, motherboard as mobo, case, aircooler, watercooler, ssd, hdd, fan, case, psu
from datetime import datetime, timedelta, date
from .scraper import *
from builtins import Exception
from django.core.exceptions import *
from django.db import DatabaseError
import asyncio


async def update(part) -> None:
    oldPrice = part.current_price
    try:
        amazon = amazonPrice(part.url)
    except Exception:
        print(f'Error in Amazon Web Scraper Price ({datetime.now()})')
        print('-')
        print(Exception)
    try:
        newegg = neweggPrice(part.url)
    except Exception:
        print(f'Error in Newegg Web Scraper Price ({datetime.now()})')
        print('-')
        print(Exception)
    if amazon < newegg:
        link = part.amazon_url
        newPrice = amazon
        part.update(current_price=newPrice, previous_price=oldPrice,
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


async def cpuUpgrade() -> str:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = cpu.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for cpuObject in parts:
            await update(cpuObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'CPU ----> {DBError}')


async def gpuUpgrade() -> str:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = gpu.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for gpuObject in parts:
            await update(gpuObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'GPU ----> {DBError}')


async def ramUpgrade() -> str:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = ram.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for ramObject in parts:
            await update(ramObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'RAM ----> {DBError}')


async def moboUpgrade() -> str:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = mobo.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for moboObject in parts:
            await update(moboObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'MOBO ----> {DBError}')


async def caseUpgrade() -> str:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = case.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for caseObject in parts:
            await update(caseObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'CASE ----> {DBError}')


async def wcUpgrade() -> str:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = watercooler.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for wcObject in parts:
            await update(wcObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'WC ----> {DBError}')


async def acUpgrade() -> str:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = aircooler.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for acObject in parts:
            await update(acObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'AC ----> {DBError}')


async def psuUpgrade() -> str:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = psu.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for psuObject in parts:
            await update(psuObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'PSU ----> {DBError}')


async def ssdUpgrade() -> str:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = ssd.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for ssdObject in parts:
            await update(ssdObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'SSD ----> {DBError}')


async def hddUpgrade() -> str:
    condition = datetime.today() - timedelta(days=3)
    try:
        parts = hdd.objects.get(last_modified_lt=condition)[:5]
        if parts.count() == 0:
            raise updaterException('Nothing to upgrade Currently', extra_info=f'{datetime.today()}')
        
        for hddObject in parts:
            await update(hddObject)
        return 'Success'
    
    except DatabaseError as DBError:
        raise updaterException(message='CHECK PRODUCTION DB for problems', extra_info=f'HDD ----> {DBError}')


async def main():
    try:
        tasks = [
            cpuUpgrade(),
            gpuUpgrade(),
            ramUpgrade(),
            moboUpgrade(),
            caseUpgrade(),
            wcUpgrade(),
            acUpgrade(),
            psuUpgrade(),
            ssdUpgrade(),
            hddUpgrade(),
        ]
        results = await asyncio.gather(*tasks)
        print(results)
    except updaterException as e:
        print(f'Error in updater ({datetime.now()})')
        print('-')
        print(f'Message: {e.message}')
        print(f'Extra Info: {e.extraInfo}')
