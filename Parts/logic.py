from .models import * #imports all components from database to be used in filtering 

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

''' Since the algorithm currently serves gamers only '''
''' The CPU and GPU should both have the largest share of the budget '''
''' Also because they are the most important component in a PC '''
partPercentages = {
    500: {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    1000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    1250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    1500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    1750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    2000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    2250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    2500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    2750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    3000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    3250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    3500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    3750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    4000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    4250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    4500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    4750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},
    5000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None,},}

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
    # percents[<part-name>] grabs the budget for that specifc part
    cpu = get_cpu(percents['CPU'], formFactor, purpose)
    gpu = get_gpu(percents['GPU'], resolution, fps, gameType, theme)
    mobo = get_mobo(percents['Mobo'], cpu, gpu)
    ram = get_ram(percents['RAM'], formFactor)
    cooler = get_cooler(percents['COOLER'], formFactor, cpu, mobo)
    case = get_case(percents['CASE'], formFactor, purpose, mobo, gpu, cooler)
    storage = get_storage(percents['STORAGE'], case)
    watts = cpu['Power Consumption'] + gpu['Power Consumption'] + cooler['Power Consumption']
    psu = get_psu(percents['PSU'], case, watts)

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

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
''' Below are the functions that get the parts based on inputs from the main function '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

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

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

