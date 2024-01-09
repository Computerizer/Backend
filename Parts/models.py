from django.db import models
from django.contrib.postgres import *
from datetime import datetime, timedelta
from django.utils import timezone
from django.core import serializers
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.serializers import ModelSerializer, Serializer


class manufacturer(models.Model):
    ID            = models.CharField(primary_key=True, null=False, blank=False, max_length=10)
    name          = models.CharField(max_length=50, null=True, blank=True)
    cpu           = models.BooleanField(verbose_name='Makes CPU', null=True, blank=True)
    gpu           = models.BooleanField(verbose_name='Makes GPU', null=True, blank=True)
    motherboard   = models.BooleanField(verbose_name='Makes Motherboards', null=True, blank=True)
    ram           = models.BooleanField(verbose_name='Makes RAM', null=True, blank=True)
    ssd           = models.BooleanField(verbose_name='Makes SSD', null=True, blank=True)
    hdd           = models.BooleanField(verbose_name='Makes HDD', null=True, blank=True)
    psu           = models.BooleanField(verbose_name='Makes PSU', null=True, blank=True)
    case          = models.BooleanField(verbose_name='Makes Cases', null=True, blank=True)
    cooler        = models.BooleanField(verbose_name='Makes Coolers', null=True, blank=True)
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name ='Manufacturer'
        verbose_name_plural ='Manufacturers'
        app_label = 'Parts'

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class commoninfo(models.Model):
    ID                 = models.CharField(primary_key=True, max_length=15)
    manufacturer       = models.ForeignKey('manufacturer', related_name="%(class)s_related", on_delete=models.CASCADE)
    name               = models.CharField(max_length=150)
    relativeSize       = models.CharField(choices=(('S', 'S'), ('M', 'M'), ("L", "L")), null=True, max_length=1)
    dateAdded          = models.DateField(auto_now_add=True, null=True)
    amazonUrl          = models.TextField(null=True, blank=True)
    neweggUrl          = models.TextField(null=True, blank=True)
    #bestbuy_url       = models.TextField(null=True)
    partRating         = models.FloatField(blank=True, null=True)
    amazonPrice        = models.FloatField(null=True, blank=True)
    neweggPrice        = models.FloatField(null=True, blank=True)
    #bestbuy_price     = models.FloatField(null=True)
    previousPrice      = models.FloatField(null=True, default=0.0)
    currentPrice       = models.FloatField(null=True, blank=True)
    lowestPriceUrl     = models.URLField(null=True, blank=True)
    lastModified       = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        app_label = 'Parts'

    def getPossibleSizes(self):
        # this method can be used in queries(a small gpu can fit in a large case, but small != large) you can check if the size of the gpu in case possible sizes
        sizes = ['S', "M", "L"]
        size = self.relativeSize

        return sizes[0:sizes.index(size)+1]

    def fitInSize(self):
        # this method gives you all the sizes a specfic part can fit in (small gpu can fit in [large, medium, small] cases)
        sizes = ['S', "M", "L"]
        size = self.relativeSize

        return sizes[sizes.index(size):]


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class cpu(commoninfo):
    Sockets = (
        ('AM4', 'AM4'),
        ('LGA 1700', 'LGA 1700'),
        ('LGA 1200', 'LGA 1200')
    )
    cores               = models.PositiveIntegerField(null=True)
    threads             = models.PositiveIntegerField(null=True)
    baseClock           = models.FloatField(null=True)
    boostClock          = models.FloatField(null=True)
    overclockable       = models.BooleanField(null=True)
    socket              = models.CharField(choices=Sockets, max_length=15, null=True)
    cooler              = models.BooleanField(help_text='eg: amd ryzen 3600', verbose_name='Comes with cooler', null=True)
    powerConsumption    = models.PositiveIntegerField(null=True)
    integratedGraphics  = models.BooleanField(null=True)
    useCase             = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15, null=True)

    def __str__(self):
        return f"{self.name} ({self.ID})"

    class Meta:
        verbose_name ='CPU'
        verbose_name_plural ='CPUs'

    def is_valid_cpu(self):
        pass


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class aircooler(commoninfo):
    sockets = [
        ('AM5', 'AM5'),
        ('AM4', 'AM4'),
        ('LGA 1700', 'LGA 1700'),
        ('LGA 1200', 'LGA 1200'),
        ('LGA 1151', 'LGA 1151'),
        ('AMD Intel', 'AMD INTEL'),
    ]

    sizes = (
        ('ATX', 'ATX'),
        ('MicroAtx', 'MicroAtx'),
        ('MiniItx', 'MiniItx')
    )
    socket            = models.CharField(choices=sockets, max_length=15, null=True)
    size              = models.CharField(choices=sizes, max_length=10, null=True)
    height            = models.FloatField(null=True)
    length             = models.FloatField(null=True)
    numFans          = models.PositiveIntegerField(null=True)
    heatsinksNum     = models.PositiveIntegerField(null=True)
    colorName        = models.CharField(default='Black', max_length=15, null=True) #Write the color name corresponding to the Hex value below
    colorHex         = models.CharField(default='#RRGGBB', max_length=8, null=True) #Write the color value as a hex string
    rgb               = models.BooleanField(null=True)
    powerConsumption = models.IntegerField(null=True)
    theme             = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), verbose_name='Color Theme', max_length=10, null=True)
    useCase          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name ='Aircooler'
        verbose_name_plural ='Aircoolers'

    def is_valid_aircooler(self):
        pass


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class watercooler(commoninfo):
    sockets = (
        ('AM5', 'AM5'),
        ('AM4', 'AM4'),
        ('LGA 1700', 'LGA 1700'),
        ('LGA 1200', 'LGA 1200'),
        ('LGA 1151', 'LGA 1151'),
        ('AMD and Intel', 'AMD and Intel')
        )

    socket            = models.CharField(choices=sockets, max_length=20, null=True)
    length            = models.FloatField(null=True)
    numFans          = models.PositiveIntegerField(null=True)
    colorName        = models.CharField(default='Black', max_length=15, null=True) #Write the color name corresponding to the Hex value below
    colorHex         = models.CharField(default='#RRGGBB', max_length=8, null=True) #Write the color value as a hex string
    rgb               = models.BooleanField(null=True)
    powerConsumption = models.PositiveIntegerField(null=True)
    theme             = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), verbose_name='Color Theme', max_length=15, null=True)
    useCase          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name ='Watercooler'
        verbose_name_plural ='Watercoolers'

    def is_valid_watercooler(self):
        pass


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class gpu(commoninfo):
    type                 = models.CharField(choices=(('GTX', 'GTX'), ('RTX', 'RTX'), ('Radeon', 'Radeon')), max_length=6, null=True)
    length               = models.FloatField(help_text='*in mm - (120, 240, 360, etc)', null=True)
    width                = models.FloatField(help_text='*slot width (1, 1.5, 2, 2.5, etc)', null=True)
    fanCount             = models.IntegerField(choices=((1, 1), (2, 2), (3, 3)), null=True)
    vram                 = models.PositiveIntegerField(verbose_name='Memory (VRAM)', null=True)
    gddrType             = models.CharField(choices=(("GDDR6X", "GDDR6X"), ('GDDR6', 'GDDR6'), ('GDDR5X', 'GDDR5X'), ('GDDR5', 'GDDR5')), max_length=10, null=True)
    cores                = models.IntegerField(null=True, blank=True)
    baseClock            = models.IntegerField(null=True)
    boostClock           = models.IntegerField(null=True)
    supportedResolution  = models.IntegerField(choices=((1000, 1000), (2000, 2000), (4000, 4000), (5000, 5000), (8000, 8000)), max_length=5, null=True)
    pcie5                = models.BooleanField(null=True) #  gen of either pcie or ddr, then
    rgb                  = models.BooleanField(null=True)
    pinNum               = models.PositiveIntegerField(verbose_name='Pins required', help_text='Number of pins to power the card', null=True)
    displayportCount     = models.PositiveIntegerField(null=True)
    hdmiCount            = models.PositiveIntegerField(null=True)
    usbcCount            = models.PositiveIntegerField(verbose_name='USB-C ports count', null=True)
    theme                = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), max_length=6, null=True)
    powerConsumption     = models.PositiveIntegerField(null=True)
    useCase              = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPUs'

    def is_valid_gpu(self):
        pass
    

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class motherboard(commoninfo):
    Sockets = (
        ('AM5', 'AM5'),
        ('AM4', 'AM4'),
        ('LGA 1700', 'LGA 1700'),
        ('LGA 1200', 'LGA 1200'),
        ('LGA 1151', 'LGA 1151'),
    )

    sizes = (
        ('ATX', 'ATX'),
        ('Micro-ATX', 'Micro-ATX'),
        ('Mini-ITX', 'Mini-ITX'),
    )
    socket               = models.CharField(choices=Sockets, max_length=15, help_text='Socket support', null=True)
    size                 = models.CharField(choices=sizes, max_length=15, help_text='Size (form factor)', null=True)
    ramSlots             = models.IntegerField(choices=((4, 4), (2, 2)), help_text='How many ram slots onboard (usually 4 unless miniItx)', default=4)
    ddr5                 = models.BooleanField(help_text='Supports DDR5 RAM', default=False, null=True)
    pcie5                = models.BooleanField(help_text='If pcie 4 then false, if pcie 5 then true', default=False, null=True)
    wifi                 = models.BooleanField(help_text='Does it allow WIFI connectivity (without a cable)', default=False, null=True)
    wifi6                = models.BooleanField(help_text='Supports WIFI 6', default=False, null=True)
    lan                  = models.BooleanField(help_text='Supports cable lan connectivity', default=True, null=True)
    #fan_headers         = models.PositiveIntegerField()
    #rgb_headers         = models.PositiveIntegerField()
    #argb_headers        = models.PositiveIntegerField()
    hdmiCount            = models.PositiveIntegerField(null=True)
    displayport          = models.PositiveIntegerField(null=True)
    usbcCount            = models.PositiveIntegerField(help_text='USB-C ports count', default=1, null=True)
    usbCount             = models.PositiveIntegerField(help_text='USB count', default=2, null=True)
    mdot2                = models.PositiveIntegerField(help_text='Number of M.2 slots', default=1, null=True)
    rgb                  = models.BooleanField(help_text="rgb lights onboard, not headers", null=True)
    ioSheild             = models.BooleanField(help_text='Does it have a built in cover on io (usually found on high end mobos)', default=False, null=True)
    theme                = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), max_length=6, default='dark', null=True)
    useCase              = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15, default='Mid-Range', null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name ='Motherboard'
        verbose_name_plural ='Motherboards'

    def is_valid_motherboard(self):
        pass

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class ram(commoninfo):
    number_of_channels = (
        ('Single', 'Single'),
        ('Dual', 'Dual'),
        ('Four', 'Four')
    )

    ram_capacity = (
        (4, 4),
        (8, 8),
        (16, 16),
        (32, 32),
        (64, 64),
        (128, 128)
    )

    ddr_type = (
        ('DDR4', 'DDR4'),
        ('DDR5', 'DDR5')
    )
    capacity          = models.PositiveIntegerField(choices=ram_capacity, null=True)
    dividedCapacity   = models.CharField(choices=(('4x2', '4x2'),('4x4', '4x4'),('8x2', '8x2'),('8x4', '8x4'),('16x2', '16x2'),('16x4', '16x4'),('32x2', '32x2'),('32x4', '32x4'),), null=True, max_length=10)
    channels          = models.CharField(choices=number_of_channels, max_length=20, null=True)
    speed             = models.IntegerField(null=True)
    type              = models.CharField(choices=ddr_type, max_length=5, null=True)
    pins              = models.PositiveIntegerField(null=True)
    xmp               = models.BooleanField(null=True)
    colorName         = models.CharField(default='Black', max_length=15, null=True)
    colorHex          = models.CharField(default='#RRGGBB', max_length=8, null=True)
    powerConsumption  = models.PositiveIntegerField(null=True)
    rgb               = models.BooleanField(default=True, null=True)
    useCase           = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name ='RAM'
        verbose_name_plural ='RAMs'

    def is_valid_ram(self):
        pass

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class hdd(commoninfo):
    rpm = (
        (3600, 3600),
        (4200, 4200),
        (5400, 5400),
        (7200, 7200),
    )

    sata_connection = (
        (1.0, 1.0),
        (1.5, 1.5),
        (3.0, 3.0),
        (6.0, 6.0),
    )

    size = (
        (1.8, 1.8),
        (2.5, 2.5),
        (3.5, 3.5)
    )

    capacity          = models.PositiveIntegerField(null=True) #in gb, tb values will be altered on the frontend
    speed             = models.PositiveIntegerField(choices=rpm, verbose_name="Speed (rpm)", null=True) #in GhZ
    sata              = models.FloatField(choices=sata_connection, verbose_name='SATA Version', null=True, max_length=3)
    size              = models.FloatField(choices=size, default=3.5, verbose_name='Size (inches)', null=True)
    rgb               = models.BooleanField(default=False, null=True)
    powerConsumption  = models.PositiveIntegerField(default=30)
    useCase           = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15, null=True)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name ='HDD'
        verbose_name_plural ='HDDs'

    def is_valid_hdd(self):
        pass

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class ssd(commoninfo):
    capacity          = models.PositiveIntegerField(null=True) #in gb, tb values will be altered on the frontend
    readSpeed         = models.PositiveIntegerField(null=True) #in MbPs
    writeSpeed        = models.PositiveIntegerField(null=True) #in MbPs
    mdot2             = models.BooleanField(verbose_name='M.2 Support', default=True)
    sata              = models.BooleanField(verbose_name='SATA Support', default=False)
    pcieGen           = models.PositiveIntegerField(verbose_name='PCIe Generation (3, 3.1, or 4)', default=4)
    powerConsumption  = models.PositiveIntegerField(default=20)
    rgb               = models.BooleanField(default=False)
    useCase           = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15, default='Mid-Range', null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name ='SSD'
        verbose_name_plural ='SSDs'

    def is_valid_ssd(self):
        pass

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class psu(commoninfo):
    ratings = (
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum')
    )

    connectivity = (
        ('Full Modular', 'Full Modular'),
        ('Semi Modular', 'Semi Modular'),
        ('None Modular', 'None Modular'),
    )

    mobo_size = (
        ('ATX', 'ATX'),
        ('Micro-ATX', 'Micro-ATX'),
        ('Mini-ITX', 'Mini-ITX')
    )
    wattage           = models.PositiveIntegerField(null=True)
    rating            = models.CharField(choices=ratings, max_length=10, default='Bronze', null=True)
    connection        = models.CharField(choices=connectivity, max_length=15, default='None Modular', null=True)
    size              = models.CharField(choices=mobo_size, max_length=10, default='ATX', null=True)
    colorName         = models.CharField(default='Black', max_length=15, null=True) #Write the color name corresponding to the Hex value below
    colorHex          = models.CharField(default='#RRGGBB', max_length=8, null=True) #Write the color value as a hex string
    useCase           = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15, null=True)
    def __str__(self):
        return f"{self.ID}: {self.name}"

    class Meta:
        verbose_name ='PSU'
        verbose_name_plural ='PSUs'

    def is_valid_psu(self):
        pass

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class fan(commoninfo):
    size                  = models.PositiveIntegerField(null=True)
    lowestRpm             = models.PositiveIntegerField(null=True, verbose_name='Lowest Speed', help_text='The RPM value')
    highestRpm            = models.PositiveIntegerField(null=True, verbose_name='Highest Speed', help_text='The RPM value')
    rgb                   = models.BooleanField(null=True)
    connection            = models.PositiveIntegerField(verbose_name='Num of pins', null=True)
    colorName             = models.CharField(default='Black', max_length=15, null=True) #Write the color name corresponding to the Hex value below
    colorHex              = models.CharField(default='#RRGGBB', max_length=8, null=True) #Write the color value as a hex string
    theme                 = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), verbose_name='Color Theme', max_length=15, null=True)
    useCase               = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15, default='Mid-Range', null=True)
    def __str__(self):
        return f"{self.name} ({self.ID})"

    class Meta:
            verbose_name ='Fan'
            verbose_name_plural ='Fans'

    def is_valid_fan(self):
        pass

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class case(commoninfo):
    #height                = models.FloatField()
    #width                 = models.FloatField()
    #length                = models.FloatField()
    moboSupport         = models.CharField(choices=(('ATX', 'ATX'), ('Micro-ATX', 'Micro-ATX'), ('Mini-ITX', 'MiniI-TX')), max_length=10, default='ATX', null=True)
    maxGpuLength        = models.FloatField(default=280, null=True)
    maxRadiatorSize     = models.FloatField(default=360, null=True)
    rgb                 = models.BooleanField(null=True)
    hasFans             = models.BooleanField(null=True)
    numFans             = models.PositiveIntegerField(null=True)
    maxFanNumber        = models.IntegerField(null=True)
    maxFanSize          = models.PositiveIntegerField(null=True)
    io                  = models.TextField(null=True)
    colorName           = models.CharField(default='Black', max_length=15, null=True)
    colorHex            = models.CharField(default='#RRGGBB', max_length=8, null=True)
    theme               = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), verbose_name='Color Theme', max_length=15, default='dark', null=True)
    useCase             = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15, default='Mid-Range', null=True)
    def __str__(self):
        return f"{self.name} ({self.ID})"

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'

    def is_valid_case(self):
        pass



############################################
#       Serializers for specific parts     #
############################################
class cpuSerializer(ModelSerializer):
    class Meta:
        model = cpu
        fields = '__all__'

class gpuSerializer(ModelSerializer):
    class Meta:
        model = gpu
        fields = '__all__'

class ramSerializer(ModelSerializer):
    class Meta:
        model = ram
        fields = '__all__'

class ssdSerializer(ModelSerializer):
    class Meta:
        model = ssd
        fields = '__all__'

class hddSerializer(ModelSerializer):
    class Meta:
        model = hdd
        fields = '__all__'

class watercoolerSerializer(ModelSerializer):
    class Meta:
        model = watercooler
        fields = '__all__'

class aircoolerSerializer(ModelSerializer):
    class Meta:
        model = aircooler
        fields = '__all__'

class moboSerializer(ModelSerializer):
    class Meta:
        model = motherboard
        fields = '__all__'

class psuSerializer(ModelSerializer):
    class Meta:
        model = psu
        fields = '__all__'

class fanSerializer(ModelSerializer):
    class Meta:
        model = fan
        fields = '__all__'

class caseSerializer(ModelSerializer):
    class Meta:
        model = case
        fields = '__all__'

############################################
############################################


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#                                       ALGORITHM                                       #
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class algorithm:
    def __init__(self, JSON):
        self.budget = JSON['budget']
        self.fps = int(JSON['fps'])
        self.resolution = (JSON['resolution'])
        self.gameType = str(JSON['gameType'])
        self.formFactor = str(JSON['formFactor'])
        self.purpose = str(JSON['purpose'])
        self.theme = JSON['theme']
        self.rgb = JSON['rgb']
        self.DAYS_ALLOWED = 4  # Number of days allowed to use a part before updating its data using scraper
        self.currentDate = datetime.today()
        self.dateOfUpdate = self.currentDate - timedelta(days=self.DAYS_ALLOWED)  # Last day allowed for part use
        self.extra = 0  # Extra budget to be used for other parts if there is saved money from other parts
        # extra variable to be distributed to other parts

    ''' Since the algorithm currently serves gamers only '''
    ''' The CPU and GPU should both have the largest share of the budget '''
    ''' Also because they are the most important component in a PC '''

    def getPercents(self, part):
        #Percents in the order: CPU - GPU - MOBO - RAM - STORAGE - COOLER - PSU - CASE
        #The part parameter is to be send as an argument from the calling function(eg:0 is CPU, 2 if RAM)
        # Ensure budget equals to 100
        partPercentages = [15, 35, 10, 8, 8, 9, 8, 7]
        return partPercentages[part]

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
    ''' Below are the functions that get the parts based on inputs from the main function '''
    ''' Basic documentation is provided as general guidance, however feel free to add additionals '''
    ''' filters or check as long as it makes the function give better suggestions for its part '''
    ''' For questions or bugs, please raise an issue here: https://github.com/Computerizer/FULL-STACK/issues '''
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

    # If several parts remain, sort by highest rating.
    # If there are parts with the same rating, suggest lowest price 
    # If part's specific budget is 200$, create a range of 10% above and below (so range 180 - 220) 

    def getCpu(self, budgetPercentage):
        budget = self.budget * (budgetPercentage / 100)
        Cpu = cpu.objects.filter(currentPrice__lt=budget)

        highest_rating = Cpu.order_by('-powerConsumption', '-threads').first()
        cpu_Price = highest_rating.currentPrice

        extra = budget - cpu_Price
        if extra > 0:
            self.extra += extra

        # return cpuSerializer(highest_rating, many=False).data
        return highest_rating


    def getGpu(self, budgetPercentage):
        budget = self.budget * (budgetPercentage / 100)

        if self.extra > 0:
            budget += self.extra
            self.extra = 0

        Gpu = gpu.objects.filter(
            currentPrice__lte = budget)
        
        if self.theme.lower() == 'dark':
            Gpu = Gpu.filter(theme = 'dark')
        else:
            Gpu = Gpu.filter(theme = 'light')
        
        if self.formFactor == 'microItx':
            Gpu = Gpu.filter(
                fanCount__lte = 2)
        elif self.formFactor == 'miniItx':
            Gpu = Gpu.filter(
                fanCount__lte = 1)

        highest_rating = Gpu.order_by('-vram', '-boostClock ').first()
        return highest_rating


    def __getRam(self, budgetPercentage, MOBO, CPU):
        # use extra budget from gpu
        budget = (self.budget * budgetPercentage)// 100
        HighestPrice = budget + ((budget * 15) // 100)
        LowestPrice = budget - ((budget * 15) // 100)
        ram_sets = MOBO.ram_slots

        #Todo Filter ram sets that exceed the maximum slot number on the mobo
        rams = ram.objects.filter(
            currentPrice__gte = LowestPrice).filter(
            currentPrice__lte=HighestPrice).exclude(
            rating__lte=4.0).exclude(
            lastModified__lt=self.dateOfUpdate)
        if MOBO.ddr_5_support:
            rams = rams.filter(type='DDR5')
        else:
            rams = rams.filter(type='DDR4')

        highest_rating = rams.objects.order_by('-rating')[:5]
        lowest_price = rams.objects.order_by('currentPrice')[:5]
        lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
        return lowPrice_and_highRating

    def getMobo(self, budgetPercentage, CPU):
        # budget = (self.budget * budgetPercentage) // 100
        # budgetLowerBound = budget - ((budget*15)//100)
        # budgetUpperBound = budget + ((budget*15)//100)
        # cpuSocket = CPU.socket
        # mobo = motherboard.objects.filter(
        #     socket=cpuSocket).filter(
        #     currentPrice__range=(budgetLowerBound, budgetUpperBound)).filter(
        #     size=self.formFactor).filter(
        #     rgb=self.rgb).filter(
        #     theme=self.theme).exclude(
        #     rating__lte=4.0).exclude(
        #     lastModified__lt=self.dateOfUpdate)
        budget = self.budget * (budgetPercentage / 100)
        mobo = motherboard.objects.filter(currentPrice__lt=budget, socket = CPU.socket, size = self.formFactor, rgb = self.rgb, theme = self.theme, lastModified__lt=self.dateOfUpdate)

        highest_rating = mobo.order_by('-currentPrice').first()
        mobo_Price = highest_rating.currentPrice

        extra = budget - mobo_Price
        if extra > 0:
            self.extra += extra

        return moboSerializer(highest_rating, many=False).data
        # highest_rating = mobo.objects.order_by('-rating')[:5]
        # lowest_price = mobo.objects.order_by('currentPrice')[:5]
        # lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
        # return mobo

    # Yusuf
    def __getCooler(self, budgetPercentage, CPU, MOBO):
        # Again filter anything outside the budget range 
        # Based on formFactor(ATX-Micro-Mini), purpose, budget, and the cpu type
        # choose either a water or air cooler (criteria can include intend of the pc
        # and how much heat the CPU releases, wich can be estimated by its name and wattage)
        # Finally filter out any coolers that aren't compatible with the motherboard/CPU
        budget = (self.budget * budgetPercentage) // 100
        budgetLowerBound = budget - ((budget*15)//100)
        budgetUpperBound = budget + ((budget*15)//100)

        # currently only using aircoolers
        # Ask user if he prefers air or water cooling
        cooler = aircooler.objects.filter(
            currentPrice__gte=budgetLowerBound).filter(
            currentPrice__lte=budgetUpperBound).filter(
            size = self.formFactor).filter(
            socket = CPU.socket).exclude(
            rating__lte=4.0).exclude(
            lastModified__lt=self.dateOfUpdate)

        highest_rating = cooler.objects.order_by('-rating')
        lowest_price = cooler.objects.order_by('currentPrice')
        lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
        return lowPrice_and_highRating

    def __getStorage(self, budgetPercentage, CASE, MOBO):
        # use extra budget from ram
        budget = (self.budget * budgetPercentage) // 100 # Calculating budget from given percentage

        ssd_count = 0
        hdd_count = 0
        ssd_price = 0
        hdd_price = 0
        if (self.formFactor == 'MiniItx') or (self.purpose == 'ConsoleKiller'):
            ssd_count = 1
            ssd_price = budget
        else:
            ssd_count = 1
            hdd_count = 1
            ssd_price = budget * 0.7
            hdd_price = budget - ssd_price

        if ssd_count > 0 and hdd_count == 0:
            SSD = ssd.objects.filter(
                currentPrice__gte=float(ssd_price - ((ssd_price*15)//100))).filter(
                currentPrice__lte=float(ssd_price + ((ssd_price*15)//100))).filter(
                rgb=self.rgb).exclude(
                rating__lte=4.0).exclude(
                lastModified__lt=self.dateOfUpdate)
            
        elif ssd_count > 0  and hdd_count > 0:
            SSD = ssd.objects.filter(
                currentPrice__gte=float(ssd_price - ((ssd_price*15)//100))).filter(
                currentPrice__lte=float(ssd_price + ((ssd_price*15)//100))).filter(
                rgb=self.rgb).exclude(
                rating__lte=4.0).exclude(
                lastModified__lt=self.dateOfUpdate)
            
            HDD = hdd.objects.filter(
                currentPrice__gte=float(hdd_price - ((hdd_price*15)//100))).filter(
                currentPrice__lte=float(hdd_price + ((hdd_price*15)//100))).filter(
                rgb=self.rgb).exclude(
                rating__lte=4.0).exclude(
                lastModified__lt=self.dateOfUpdate)
        
        if HDD.count() == 0:
            highest_rating = SSD.objects.order_by('-rating')[:5]
            lowest_price = SSD.objects.order_by('currentPrice')[:5]
            lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
            return lowPrice_and_highRating
        else:
            highest_rating_ssd = SSD.objects.order_by('-rating')[:5]
            lowest_price_ssd = SSD.objects.order_by('currentPrice')[:5]
            lowPrice_and_highRating_ssd = highest_rating_ssd.intersection(lowest_price_ssd).first()
            highest_rating_hdd = HDD.objects.order_by('-rating')[:5]
            lowest_price_hdd = HDD.objects.order_by('currentPrice')[:5]
            lowPrice_and_highRating_hdd = highest_rating_hdd.intersection(lowest_price_hdd).first()
            return [lowPrice_and_highRating_ssd, lowPrice_and_highRating_hdd]


    def getCase(self, budgetPercentage, GPU):
        # gpu large = case large (only use of relative size)
        # make sure cooler length = case depth
        budget = self.budget * (budgetPercentage / 100)
        Case = case.objects.filter(currentPrice__lt=budget, relativeSize__in = GPU.fitInSize())
        #Case = Case.exclude(lastModified__lt=self.dateOfUpdate)

        highest_rating = Case.order_by('-currentPrice').first()
        case_Price = highest_rating.currentPrice

        extra = budget - case_Price
        if extra > 0:
            self.extra += extra

        return caseSerializer(highest_rating, many=False).data


    def __getPsu(self, budgetPercentage, CASE, WATTS):
        budget = (self.budget * budgetPercentage)// 100
        HighestPrice = budget + ((budget * 15) // 100)
        LowestPrice = budget - ((budget * 15) // 100)
        Size = self.JSON['formFactor'][0]
        Psu = psu.objects.filter(
            currentPrice__gte = LowestPrice).filter(
            currentPrice__lte=HighestPrice).filter(
            size = Size).filter(
            wattage__gte = WATTS).exclude(
            rating__lte=4.0).exclude(
            lastModified__lt=self.dateOfUpdate)

        highest_rating = Psu.objects.order_by('-ratings').order_by('-rating')[:5]
        lowest_price = Psu.objects.order_by('currentPrice')[:5]
        lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
        return lowPrice_and_highRating


    def getComputer(self):
        try:
            cpu = self.__getCpu(self.getPercents(0))
        except Exception:
            print('CPU ERROR')
            print(Exception)
            #or get static part

        try:
            mobo = self.__getMobo(self.getPercents(2), cpu)
        except Exception:
            print('MOBO ERROR')
            print(Exception)
            #or get static part

        try:
            cooler = self.__getCooler(self.getPercents(5), cpu, mobo)
        except Exception:
            print('COOLER ERROR')
            print(Exception)
            #or get static part

        try:
            gpu = self.__getGpu(self.getPercents(1))
        except Exception:
            print('GPU ERROR')
            print(Exception)
            #or get static part

        try:
            case = self.__getCase(self.getPercents(7), mobo, gpu, cooler)
        except Exception:
            print('CASE ERROR')
            print(Exception)
            #or get static part

        try:
            ram = self.__getRam(self.getPercents(3), mobo, cpu)
        except Exception:
            print('RAM ERROR')
            print(Exception)
            #or get static part

        try:
            storage = self.__getStorage(self.getPercents(4), case, mobo)
        except Exception:
            print('STORAGE ERROR')
            print(Exception)
            #or get static part

        try:
            watts = cpu['powerConsumption'] + gpu['powerConsumption'] + cooler['powerConsumption']
        except Exception:
            print('ERROR CALCULATING WATTS')
            print('Check other parts errors...')
            print(Exception)
            #or get static part

        try:
            psu = self.__getPsu(self.getPercents(6), case, watts)
        except Exception:
            print('PSU ERROR')
            print(Exception)
            #or get static part

        # Before returning the PC to the views, we should run some error checking and integration checking
        try:
            return[cpu, mobo, cooler, gpu, case, ram, storage, psu]
        except Exception as error:
            return error


# Below is an exmaple of a JSON request we will get from the tool's frontend
jsonExample1 = {
    'budget': 4000,
    'fps': 144,
    'resolution': '4k',
    'gameType': 'AAA',
    'formFactor': 'ATX',
    'purpose': 'Table Top',
    'theme': 'Dark',
    'RGB': True
    }