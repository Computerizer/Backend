from .models import *

JSON = {
    'budget': 4000,
    'fps': 144,
    'resolution': '4k',
    'gametype': 'AAA',
    'formFactor': 'ATX',
    'purpose': 'Table Top',
    'theme': ['Dark', 'RGB'],
    'question': {'Q1': None, 'Q2': None}
}

partPercentages = {
    500: {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    750:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1000:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1250:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1500:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1750:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2000:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2250:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2500:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2750:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3000:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3250:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3500:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3750:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4000:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4250:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4500:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4750:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    5000:
    {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'AC': None,
    'WC': None, 'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},}

cache = dict()

def main(JSON):
    ''' This function calls on all PC parts, using input from user's\
    JSON preferences to filter out different parts '''
    ''' The function also checks that suggested parts integrate correctly\
    with each other, before sending a response to the user '''
    global partPercentages
    price = JSON['Budget']
    percents = partPercentages[price]
    
    resolution = JSON['resolution']
    fps = JSON['fps']
    gameType = JSON['gameType']
    formFactor = JSON['formFactor']
    purpose = JSON['purpose']
    theme = JSON['theme']

    ''' Parts are chosen in a specific sequence,\
    as some depend on each other '''
    cpu = get_cpu(percents['CPU'], formFactor, purpose)
    gpu = get_gpu(percents['GPU'], resolution, fps, gameType, theme)
    mobo = get_mobo(percents['Mobo'], cpu, gpu)
    ram = get_ram()
    cooler = get_cooler()
    case = get_case()
    psu = get_psu()

    ''' Before the PC is returned, the algorithm
    first checks that all parts integrate correctly with each other, 
    by using a validator in the models.py '''
    if cooler['type'] == 'air':
        pc = computer(motherboard=mobo, aircooler=cooler,
            cpu=cpu, gpu=gpu, ram=ram, psu=psu, case=case)
    else:
        pc = computer(motherboard=mobo, watercooler=cooler,
            cpu=cpu, gpu=gpu, ram=ram, psu=psu, case=case)
    if pc.is_valid_computer is True:
        return {} # A dictionary containing all parts and its details
    else:
        pass

def get_cpu(budget, formFactor, purpose):
    pass

def get_gpu(budget, resolution, fps, gameType, theme):
    pass

def get_mobo(budget, cpu, gpu):
    pass

def get_ram(budget, formFactor):
    pass

def get_cooler(budget, formfactor, purpose, cpu, mobo):
    pass

def get_case(budget, formFactor, purpose, mobo, gpu, cooler):
    pass

def get_storage(budget, case):
    pass

def get_psu(budget, formfactor, watts):
    pass


