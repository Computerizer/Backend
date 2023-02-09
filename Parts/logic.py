from .models import * #imports all component tables from database to be used in filtering 

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
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    1750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    2750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    3750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    4750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},
    5000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
    'PSU': None, 'FAN': None, 'CASE': None, 'SSD': None, 'HDD': None},}

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
    mobo = get_mobo(percents['Mobo'], cpu, formFactor, theme)
    cooler = get_cooler(percents['COOLER'], formFactor, cpu, mobo)
    gpu = get_gpu(percents['GPU'], resolution, fps, gameType, theme)
    case = get_case(percents['CASE'], formFactor, purpose, mobo, gpu, cooler)
    ram = get_ram(percents['RAM'], formFactor)
    ssd = get_ssd(percents['SSD'], case, mobo)
    hdd = get_hdd(percents['HDD'], case)
    watts = cpu['power_consumption'] + gpu['power_consumption'] + cooler['power_consumption']
    psu = get_psu(percents['PSU'], case, watts)

    ''' Before the PC is returned, the algorithm
    first checks that all parts integrate correctly with each other, 
    by using the validator in the computer table in models.py '''
    if cooler['type'] == 'air':
        pc = computer(motherboard=mobo, aircooler=cooler,
            cpu=cpu, gpu=gpu, ram=ram, case=case, ssd=ssd, hdd=hdd, psu=psu)
    else:
        pc = computer(motherboard=mobo, watercooler=cooler,
            cpu=cpu, gpu=gpu, ram=ram, case=case, ssd=ssd, hdd=hdd, psu=psu)
    if pc.is_valid_computer is True:
        return {} # A dictionary containing all parts and its details
    else:
        pass

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
''' Below are the functions that get the parts based on inputs from the main function '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def get_cpu(budget, formFactor, purpose):
    ''' Below is the explanation of how this function is going to work '''
    # All CPUs are firstly filtered by budget from the CPUs table
    # The formFactor and purpose paramters play a role in deciding which CPU to choose
    # This is because some CPUs emit too much heat, and consume so much power, hence
    # they can not be used in mini-ITX or console killer builds for example
    # So the rule will be to filter out CPUs based on a combination of budget 
    # and the other paramters, and you can use the formFactor and purpose fields 
    # in the CPU table to help, for example the i9 is both table top and work machine,
    # and its also for ATX builds.
    pass


def get_mobo(budget, cpu, formFactor, theme):
    ''' Below is the explanation of how this function is going to work '''
    # Choosing a motherboard is pretty simple 
    # Firstly filter by budget, then by theme.
    # Then we filter based on our CPU choice (CPU-socket field), AMD and Intel use different mobos
    # Finally we filter based on formFactor: ATX, Micro-ATX, or Mini-ITX
    pass


def get_gpu(budget, resolution, fps, gameType, theme):
    ''' Below is the explanation of how this function is going to work '''
    # The GPU is a bit more complicated than the CPU
    # As there are many parameters involved 
    # 1) Performance as in resolution, FPS, gametype, and boostclock.
    # 2) Maximizing GPU performance utilization from motherboard,
    # for example if the mobo doesn't support PCIe5, there is no need to suggest a PCIe5 GPU
    # And for that you can use the (supported_resolution, boost_clock, )
    # in the CPU table to help, for example the i9 is both table top and work machine,
    # and its also for ATX builds.
    pass


def get_case(budget, formFactor, purpose, mobo, gpu, cooler):
    ''' Below is the explanation of how this function is going to work '''
    pass


def get_ram(budget, formFactor):
    ''' Below is the explanation of how this function is going to work '''
    pass


def get_cooler(budget, formfactor, purpose, cpu, mobo):
    ''' Below is the explanation of how this function is going to work '''
    pass


def get_ssd(budget, case, mobo):
    ''' Below is the explanation of how this function is going to work '''
    pass


def get_hdd(budget, case):
    ''' Below is the explanation of how this function is going to work '''
    pass


def get_psu(budget, formfactor, watts):
    ''' Below is the explanation of how this function is going to work '''
    pass

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

