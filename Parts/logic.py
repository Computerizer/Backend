from .models import * #imports all component tables from database to be used in filtering 

# Below is an exmaple of a JSON request we will get from the tool's frontend
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

class algorithm:
    def __init__(self, JSON):
        self.budget = int(JSON['budget'])
        self.fps = int(JSON['fps'])
        self.resolution = int(JSON['resolution'][0])
        self.gameType = str(JSON['gameType'])
        self.formFactor = str(JSON['formFactor'])
        self.purpose = str(JSON['purpose'])
        self.theme = JSON['theme'][0]
        if JSON['theme'][1] == 'RGB':
            self.rgb = True
        else:
            self.rgb = False
    
    ''' Since the algorithm currently serves gamers only '''
    ''' The CPU and GPU should both have the largest share of the budget '''
    ''' Also because they are the most important component in a PC '''
    def getPercents(self, part):
        partPercentages = {
        500: {'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        1000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        1250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        1500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        1750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        2000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        2250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        2500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        2750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        3000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        3250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        3500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        3750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        4000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        4250:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        4500:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        4750:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},
        5000:{'CPU': None, 'GPU': None, 'RAM': None, 'MOBO': None, 'COOLER': None,
        'PSU': None, 'FAN': None, 'CASE': None, 'STORAGE': None},}
        percents = partPercentages[self.budget]
        return percents[part]

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    ''' Below are the functions that get the parts based on inputs from the main function '''
    ''' Basic documentation is provided as general guidance, however feel free to add additionals '''
    ''' filters or check as long as it makes the function give better suggestions for its part '''
    ''' For questions or bugs, please raise an issue here: https://github.com/Computerizer/FULL-STACK/issues '''
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

    def __getCpu(self):
        # All CPUs are firstly filtered by budget from the CPUs table
        # The formFactor and purpose paramters play a role in deciding which CPU to choose
        # This is because some CPUs emit too much heat, and consume so much power, hence
        # they can not be used in mini-ITX or console killer builds for example
        # So the rule will be to filter out CPUs based on a combination of budget 
        # and the other paramters, and you can use the formFactor and purpose fields 
        # in the CPU table to help, for example the i9 is both table top and work machine,
        # and its also for ATX builds.
        pass
    
    def __getGpu(self):
        # The GPU is a bit more complicated than the CPU
        # As there are many parameters involved 
        # 1) Performance as in resolution, FPS, gametype, and boostclock.
        # 2) Maximizing GPU performance utilization from motherboard,
        # for example if the mobo doesn't support PCIe5, there is no need to suggest a PCIe5 GPU
        # And for that you can use the (supported_resolution, boost_clock, etc) fields
        pass
    
    def __getRam(self):
        # Follow the same previous pattern, first filter by budget
        # Next filter any ram sets that exceed the maximum slot number on the mobo
        # Then check if the mobo and cpu support DDr5, if so then suggest a DDr5 ram set
        # If not then filter out anything that is DDr5 and keep the DDr4
        pass
    
    def __getMobo(self):
        # Choosing a motherboard is pretty simple 
        # Firstly filter by budget, then by theme.
        # Then we filter based on our CPU choice (CPU-socket field), AMD and Intel use different mobos
        # Finally we filter based on formFactor: ATX, Micro-ATX, or Mini-ITX
        pass
    
    def __getCooler(self):
        # Again filter anything outside the budget range 
        # Based on formFactor(ATX-Micro-Mini), purpose, budget, and the cpu type
        # choose either a water or air cooler (criteria can include intend of the pc
        # and how much heat the CPU releases, wich can be estimated by its name and wattage)
        # Finally filter out any coolers that aren't compatible with the motherboard/CPU
        pass
    
    def __getStorage(self):
        # Follow the same previous pattern, first filter by budget
        # An SSD must hold the main OS at least, and preferablly be as fast as possible
        # There for check for the fastest SSD sockets going down, and filter out as you go
        # You can do so by checking sockets on the motherboard, using relative fields 
        # At the end filter what's left based on the fastest speed and highest storage
        pass
    
    def __getCase(self):
        # Obviously, we filter by price/budget firstly 
        # Then we fitler based on the formfactor (ATX, micro, or mini)
        # Then we filter cases left to fit the maximum width of the gpu
        # We also make sure that the cooler fits in the case,
        # if its an aircooler then we check for height and clearance, 
        # if its a watercooler, then check that the radiator fits 
        pass
    
    def __getPsu(self):
        # Filter out by budget 
        # Then filter out based on formFactor (ATX, ITX, etc)
        # Then filter for the minimum required watts given in the parameter 
        # Finally go from the highest rating (Platinum) to lowest (Bronze), 
        # check if there is any psu from the higher ratings, keep it and remove all else
        pass

    def getComputer(self):
        cpu = self.__getCpu(self.getPercents('CPU'))
        mobo = self.__getMobo(self.getPercents('Mobo'), cpu)
        cooler = self.__getCooler(self.getPercents('COOLER'), cpu, mobo)
        gpu = self.__getGpu(self.getPercents('GPU'))
        case = self.__getCase(self.getPercents('CASE'), mobo, gpu, cooler)
        ram = self.__getRam(self.getPercents('RAM'), mobo, cpu)
        storage = self.__getStorage(self.getPercents('STORAGE'), case, mobo)
        watts = cpu['power_consumption'] + gpu['power_consumption'] + cooler['power_consumption']
        psu = self.__getPsu(self.getPercents('PSU'), case, watts)
        #Before returning the PC to the views, we should run some error checking and integration checking
        case = self.check(cpu, mobo, cooler, gpu, case, ram, storage, psu)
        if case is True:
            return{}
        else:
            pass

