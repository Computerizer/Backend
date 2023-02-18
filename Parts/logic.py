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

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
''' Since the algorithm currently serves gamers only '''
''' The CPU and GPU should both have the largest share of the budget '''
''' Also because they are the most important component in a PC '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

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

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
''' Below are the functions that get the parts based on inputs from the main function '''
''' Basic documentation is provided as general guidance, however feel free to add additionals '''
''' filters or check as long as it makes the function give better suggestions for its part '''
''' For questions or bugs, please raise an issue here: https://github.com/Computerizer/FULL-STACK/issues '''
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


def get_gpu(budget, fromfactor, resolution, fps, gameType, theme):
    ''' Below is the explanation of how this function is going to work '''
    # The GPU is a bit more complicated than the CPU
    # As there are many parameters involved 
    # 1) Performance as in resolution, FPS, gametype, and boostclock.
    # 2) Maximizing GPU performance utilization from motherboard,
    # for example if the mobo doesn't support PCIe5, there is no need to suggest a PCIe5 GPU
    # And for that you can use the (supported_resolution, boost_clock, etc) fields
    pass


def get_cooler(budget, formfactor, purpose, cpu, mobo):
    ''' Below is the explanation of how this function is going to work '''
    # Again filter anything outside the budget range 
    # Based on formFactor(ATX-Micro-Mini), purpose, budget, and the cpu type
    # choose either a water or air cooler (criteria can include intend of the pc
    # and how much heat the CPU releases, wich can be estimated by its name and wattage)
    # Finally filter out any coolers that aren't compatible with the motherboard/CPU
    pass


def get_case(budget, formFactor, purpose, mobo, gpu, cooler):
    ''' Below is the explanation of how this function is going to work '''
    # Obviously, we filter by price/budget firstly 
    # Then we fitler based on the formfactor (ATX, micro, or mini)
    # Then we filter cases left to fit the maximum width of the gpu
    # We also make sure that the cooler fits in the case,
    # if its an aircooler then we check for height and clearance, 
    # if its a watercooler, then check that the radiator fits 
    pass


def get_ram(budget, mobo, cpu):
    ''' Below is the explanation of how this function is going to work '''
    # Follow the same previous pattern, first filter by budget
    # Next filter any ram sets that exceed the maximum slot number on the mobo
    # Then check if the mobo and cpu support DDr5, if so then suggest a DDr5 ram set
    # If not then filter out anything that is DDr5 and keep the DDr4
    pass


def get_ssd(budget, case, mobo):
    ''' Below is the explanation of how this function is going to work '''
    # Follow the same previous pattern, first filter by budget
    # An SSD must hold the main OS at least, and preferablly be as fast as possible
    # There for check for the fastest SSD sockets going down, and filter out as you go
    # You can do so by checking sockets on the motherboard, using relative fields 
    # At the end filter what's left based on the fastest speed and highest storage
    pass


def get_hdd(budget, case, gameType):
    ''' Below is the explanation of how this function is going to work '''
    # Again, filter by budget
    # Generally, AAA games require more storage as they are larger in storage 
    # For HDDs, prioritize storage over speed 
    # Also check that their are available disk storage space in the case
    pass


def get_psu(budget, formfactor, watts):
    ''' Below is the explanation of how this function is going to work '''
    # Filter out by budget 
    # Then filter out based on formFactor (ATX, ITX, etc)
    # Then filter for the minimum required watts given in the parameter 
    # Finally go from the highest rating (Platinum) to lowest (Bronze), 
    # check if there is any psu from the higher ratings, keep it and remove all else
    pass


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


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
    gpu = get_gpu(percents['GPU'], formFactor, resolution, fps, gameType, theme)
    case = get_case(percents['CASE'], formFactor, purpose, mobo, gpu, cooler)
    ram = get_ram(percents['RAM'], mobo, cpu)
    ssd = get_ssd(percents['SSD'], case, mobo)
    hdd = get_hdd(percents['HDD'], case, gameType)
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


