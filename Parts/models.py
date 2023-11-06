from django.db import models
from django.contrib.postgres import *
from datetime import datetime, timedelta
from django.utils import timezone
from django.core import serializers
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse

class manufacturer(models.Model):
    ID                         = models.CharField(primary_key=True, null=False, blank=False, max_length=10)
    name                       = models.CharField(max_length=50, null=True, blank=True)
    manufactures_cpu           = models.BooleanField(verbose_name='Makes CPU', null=True, blank=True)
    manufactures_gpu           = models.BooleanField(verbose_name='Makes GPU', null=True, blank=True)
    manufactures_motherboard   = models.BooleanField(verbose_name='Makes Motherboards', null=True, blank=True)
    manufactures_ram           = models.BooleanField(verbose_name='Makes RAM', null=True, blank=True)
    manufactures_ssd           = models.BooleanField(verbose_name='Makes SSD', null=True, blank=True)
    manufactures_hdd           = models.BooleanField(verbose_name='Makes HDD', null=True, blank=True)
    manufactures_psu           = models.BooleanField(verbose_name='Makes PSU', null=True, blank=True)
    manufactures_case          = models.BooleanField(verbose_name='Makes Cases', null=True, blank=True)
    manufactures_cooler        = models.BooleanField(verbose_name='Makes Coolers', null=True, blank=True)
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name ='Manufacturer'
        verbose_name_plural ='Manufacturers'
        app_label = 'Parts'

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class commoninfo(models.Model):
    ID                  = models.CharField(primary_key=True, max_length=15)
    manufacturer        = models.ForeignKey('manufacturer', related_name="%(class)s_related", on_delete=models.CASCADE)
    name                = models.CharField(max_length=150)
    relativeSize        = models.CharField(choices=(('S', 'S'), ('M', 'M'), ("L", "L")), null=True, max_length=1)
    data_added          = models.DateField(auto_now_add=True, null=True)
    amazon_url          = models.TextField(null=True, blank=True)
    newegg_url          = models.TextField(null=True, blank=True)
    #bestbuy_url        = models.TextField(null=True)
    partRating          = models.FloatField(blank=True, null=True)
    amazon_price        = models.FloatField(null=True, blank=True)
    newegg_price        = models.FloatField(null=True, blank=True)
    #bestbuy_price      = models.FloatField(null=True)
    previous_price      = models.FloatField(null=True, default=0.0)
    current_price       = models.FloatField(null=True, blank=True)
    lowest_Price_Link   = models.URLField(null=True, blank=True)
    last_modified       = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        app_label = 'Parts'


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class cpu(commoninfo):
    Sockets = (
        ('AM4', 'AM4'),
        ('LGA 1700', 'LGA 1700'),
        ('LGA 1200', 'LGA 1200')
    )
    cores               = models.PositiveIntegerField()
    threads             = models.PositiveIntegerField()
    base_clock          = models.FloatField()
    boost_clock         = models.FloatField()
    overclockable       = models.BooleanField()
    socket              = models.CharField(choices=Sockets, max_length=15)
    cooler              = models.BooleanField(help_text='eg: amd ryzen 3600', verbose_name='Comes with cooler')
    power_consumption   = models.PositiveIntegerField(null=True)
    integrated_graphics = models.BooleanField(null=True)
    use_case            = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

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
    socket            = models.CharField(choices=sockets, max_length=15)
    size              = models.CharField(choices=sizes, max_length=10)
    height            = models.FloatField()
    length             = models.FloatField()
    num_fans          = models.PositiveIntegerField()
    num_heatsinks     = models.PositiveIntegerField()
    color_name        = models.CharField(default='Black', max_length=15) #Write the color name corresponding to the Hex value below
    color_hex         = models.CharField(default='#RRGGBB', max_length=8) #Write the color value as a hex string
    rgb               = models.BooleanField()
    power_consumption = models.IntegerField(null=True)
    theme             = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), verbose_name='Color Theme', max_length=10)
    use_case          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

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

    socket            = models.CharField(choices=sockets, max_length=20)
    length            = models.FloatField()
    num_fans          = models.PositiveIntegerField()
    color_name        = models.CharField(default='Black', max_length=15) #Write the color name corresponding to the Hex value below
    color_hex         = models.CharField(default='#RRGGBB', max_length=8) #Write the color value as a hex string
    rgb               = models.BooleanField()
    power_consumption = models.PositiveIntegerField(null=True)
    theme             = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), verbose_name='Color Theme', max_length=15)
    use_case          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name ='Watercooler'
        verbose_name_plural ='Watercoolers'

    def is_valid_watercooler(self):
        pass


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class gpu(commoninfo):
    type                 = models.CharField(choices=(('GTX', 'GTX'), ('RTX', 'RTX'), ('Radeon', 'Radeon')), max_length=6)
    length               = models.FloatField(help_text='*in mm - (120, 240, 360, etc)')
    width                = models.FloatField(help_text='*slot width (1, 1.5, 2, 2.5, etc)', null=True)
    fan_count            = models.IntegerField(choices=((1, 1), (2, 2), (3, 3)))
    vram                 = models.PositiveIntegerField(verbose_name='Memory (VRAM)')
    gddr_type            = models.CharField(choices=(("GDDR6X", "GDDR6X"), ('GDDR6', 'GDDR6'), ('GDDR5X', 'GDDR5X'), ('GDDR5', 'GDDR5')), max_length=10)
    cores                = models.IntegerField(null=True, blank=True)
    base_clock           = models.IntegerField()
    boost_clock          = models.IntegerField()
    supported_resolution = models.IntegerField(choices=((1000, 1000), (2000, 2000), (4000, 4000), (5000, 5000), (8000, 8000)), max_length=5)
    pcie_5               = models.BooleanField(null=True) #  gen of either pcie or ddr, then
    rgb                  = models.BooleanField()
    pin_num              = models.PositiveIntegerField(verbose_name='Pins required', help_text='Number of pins to power the card', null=True)
    displayport_count    = models.PositiveIntegerField()
    hdmi_count           = models.PositiveIntegerField()
    usbc_count           = models.PositiveIntegerField(verbose_name='USB-C ports count', null=True)
    theme                = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), max_length=6)
    power_consumption    = models.PositiveIntegerField(null=True)
    use_case             = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

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
    socket               = models.CharField(choices=Sockets, max_length=15, verbose_name='Socket support')
    size                 = models.CharField(choices=sizes, max_length=15, verbose_name='Size (form factor)')
    ram_slots            = models.IntegerField(choices=((4, 4), (2, 2)), verbose_name='How many ram slots', null=True)
    ddr_5_support        = models.BooleanField(verbose_name='Supports DDR5 RAM')
    ddr_4_support        = models.BooleanField(verbose_name='Supports DDR4 RAM')
    pcie_version         = models.BooleanField(verbose_name='Which Pcie verison (type only 5 or4)', null=True)
    wifi                 = models.BooleanField(help_text='Does it allow WIFI connectivity (without a cable)')
    wifi_6_support       = models.BooleanField(verbose_name='Supports WIFI 6')
    lan_support          = models.BooleanField(verbose_name='Supports LAN Connectivity')
    #fan_headers         = models.PositiveIntegerField()
    rgb                  = models.BooleanField(help_text="ONLY RGB LIGHT THAT'S PART OF THE MOBO")
    #rgb_headers         = models.PositiveIntegerField()
    #argb_headers        = models.PositiveIntegerField()
    hdmi_count           = models.PositiveIntegerField()
    displayport_count    = models.PositiveIntegerField()
    usbc_count           = models.PositiveIntegerField(verbose_name='USB-C ports count')
    usb3point2_count     = models.IntegerField(verbose_name='USB3.2 count', null=True)
    usb_count            = models.IntegerField(verbose_name='USB count', null=True)
    mdot2_SSD_slots      = models.PositiveIntegerField(verbose_name='Number of M.2 slots')
    integrated_io_sheild = models.BooleanField(help_text='Does it have a built in cover on io')
    theme                = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), max_length=6)
    use_case             = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

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
    capacity          = models.PositiveIntegerField(choices=ram_capacity)
    divided_capacity  = models.CharField(choices=(('4x2', '4x2'),('4x4', '4x4'),('8x2', '8x2'),('8x4', '8x4'),('16x2', '16x2'),('16x4', '16x4'),('32x2', '32x2'),('32x4', '32x4'),), help_text='How many sticks to make up total RAM capacity', max_length=10)
    channels          = models.CharField(choices=number_of_channels, max_length=20)
    speed             = models.IntegerField()
    type              = models.CharField(choices=ddr_type, max_length=5)
    pins              = models.PositiveIntegerField()
    xmp               = models.BooleanField()
    color_name        = models.CharField(default='Black', max_length=15)
    color_hex         = models.CharField(default='#RRGGBB', max_length=8)
    power_consumption = models.PositiveIntegerField(null=True)
    rgb               = models.BooleanField()
    use_case          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

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

    capacity          = models.PositiveIntegerField() #in gb, tb values will be altered on the frontend
    speed             = models.PositiveIntegerField(choices=rpm, verbose_name="Speed (rpm)") #in GhZ
    sata              = models.FloatField(choices=sata_connection, verbose_name='SATA Version', null=True, max_length=3)
    size              = models.FloatField(choices=size, null=True)
    rgb               = models.BooleanField()
    power_consumption = models.PositiveIntegerField(null=True)
    use_case          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name ='HDD'
        verbose_name_plural ='HDDs'

    def is_valid_hdd(self):
        pass

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class ssd(commoninfo):
    capacity          = models.PositiveIntegerField() #in gb, tb values will be altered on the frontend
    read_speed        = models.PositiveIntegerField() #in MbPs
    write_speed       = models.PositiveIntegerField() #in MbPs
    mdot2             = models.BooleanField(verbose_name='M.2 Support', null=True)
    sata              = models.BooleanField(verbose_name='SATA Support', null=True)
    pcie_generation   = models.PositiveIntegerField(verbose_name='PCIe Generation (3, 3.1, or 4)', null=True)
    power_consumption = models.PositiveIntegerField(null=True)
    rgb               = models.BooleanField(null=True)
    use_case          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

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
    wattage           = models.PositiveIntegerField()
    rating            = models.CharField(choices=ratings, max_length=10)
    connection        = models.CharField(choices=connectivity, max_length=15)
    size              = models.CharField(choices=mobo_size, max_length=10)
    color_name        = models.CharField(default='Black', max_length=15) #Write the color name corresponding to the Hex value below
    color_hex         = models.CharField(default='#RRGGBB', max_length=8) #Write the color value as a hex string
    use_case          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)
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
    lowest_rpm            = models.PositiveIntegerField(null=True, verbose_name='Lowest Speed', help_text='The RPM value')
    highest_rpm           = models.PositiveIntegerField(null=True, verbose_name='Highest Speed', help_text='The RPM value')
    rgb                   = models.BooleanField()
    connection            = models.PositiveIntegerField(verbose_name='Num of pins', null=True)
    color_name            = models.CharField(default='Black', max_length=15) #Write the color name corresponding to the Hex value below
    color_hex             = models.CharField(default='#RRGGBB', max_length=8) #Write the color value as a hex string
    theme                 = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), verbose_name='Color Theme', max_length=15)
    use_case              = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)
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
    mobo_support          = models.CharField(choices=(('ATX', 'ATX'), ('Micro-ATX', 'Micro-ATX'), ('Mini-ITX', 'MiniI-TX')), max_length=10)
    max_gpu_length        = models.FloatField(null=True, blank=True)
    max_radiator_size     = models.FloatField(null=True, blank=True)
    rgb                   = models.BooleanField()
    has_fans              = models.BooleanField()
    num_fans              = models.PositiveIntegerField()
    max_num_number        = models.IntegerField(null=True)
    max_fan_size          = models.PositiveIntegerField(null=True)
    io                    = models.TextField(null=True)
    color_name            = models.CharField(default='Black', max_length=15)
    color_hex             = models.CharField(default='#RRGGBB', max_length=8)
    theme                 = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), verbose_name='Color Theme', max_length=15)
    use_case              = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)
    def __str__(self):
        return f"{self.name} ({self.ID})"

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'

    def is_valid_case(self):
        pass



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
        self.dateOfUpdate = self.currentDate - timedelta(days=self.DAYS_ALLOWED) # Last day allowed for part use


    ''' Since the algorithm currently serves gamers only '''
    ''' The CPU and GPU should both have the largest share of the budget '''
    ''' Also because they are the most important component in a PC '''

    def getPercents(self, part):
        #Percents in the order: CPU - GPU - MOBO - RAM - STORAGE - COOLER - PSU - CASE
        #The part parameter is to be send as an argument from the calling function(eg:0 is CPU, 2 if RAM)
        # Ensure budget equals to 100
        partPercentages = [19, 30, 16, 6, 6, 8, 7, 8]
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

    # Yusuf
    def getCpu(self, budgetPercentage):
        budget = (self.budget * budgetPercentage) // 100
        budgetLowerBound = budget - ((budget*15)//100)
        budgetUpperBound = budget + ((budget*15)//100)

        Cpu = cpu.objects.filter(newegg_price=71.0)
        

        #highest_rating = Cpu.order_by('-partRating', '-base_clock')
        #lowest_price = Cpu.order_by('current_price')
        #lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
        #return lowPrice_and_highRating
        return Cpu

    # Omar
    def __getGpu(self, budgetPercentage):
        budget = (self.budget * budgetPercentage)// 100
        HighestPrice = budget + ((budget * 15) // 100)
        LowestPrice = budget - ((budget * 15) // 100)
        Gpu = gpu.objects.filter(
            current_price__gte = LowestPrice).filter(
            current_price__lte=HighestPrice).filter(
            rgb=self.rgb).exclude(
            rating__lte=4.0).exclude(
            last_modified__lt=self.dateOfUpdate)

        highest_rating = Gpu.objects.order_by('-rating', '-base_clock')
        lowest_price = Gpu.objects.order_by('current_price')
        lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
        return lowPrice_and_highRating

    def __getRam(self, budgetPercentage, MOBO, CPU):
        budget = (self.budget * budgetPercentage)// 100
        HighestPrice = budget + ((budget * 15) // 100)
        LowestPrice = budget - ((budget * 15) // 100)
        ram_sets = MOBO.ram_slots

        #Todo Filter ram sets that exceed the maximum slot number on the mobo
        rams = ram.objects.filter(
            current_price__gte = LowestPrice).filter(
            current_price__lte=HighestPrice).exclude(
            rating__lte=4.0).exclude(
            last_modified__lt=self.dateOfUpdate)
        if MOBO.ddr_5_support:
            rams = rams.filter(type='DDR5')
        else:
            rams = rams.filter(type='DDR4')

        highest_rating = rams.objects.order_by('-rating')[:5]
        lowest_price = rams.objects.order_by('current_price')[:5]
        lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
        return lowPrice_and_highRating

    def __getMobo(self, budgetPercentage, CPU):
        budget = (self.budget * budgetPercentage) // 100
        budgetLowerBound = budget - ((budget*15)//100)
        budgetUpperBound = budget + ((budget*15)//100)
        cpuSocket = CPU.socket
        mobo = motherboard.objects.filter(
            socket=cpuSocket).filter(
            current_price__range=(budgetLowerBound, budgetUpperBound)).filter(
            size=self.formFactor).filter(
            rgb=self.rgb).filter(
            theme=self.theme).exclude(
            rating__lte=4.0).exclude(
            last_modified__lt=self.dateOfUpdate)

        # highest_rating = mobo.objects.order_by('-rating')[:5]
        # lowest_price = mobo.objects.order_by('current_price')[:5]
        # lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
        return mobo

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
            current_price__gte=budgetLowerBound).filter(
            current_price__lte=budgetUpperBound).filter(
            size = self.formFactor).filter(
            socket = CPU.socket).exclude(
            rating__lte=4.0).exclude(
            last_modified__lt=self.dateOfUpdate)

        highest_rating = cooler.objects.order_by('-rating')
        lowest_price = cooler.objects.order_by('current_price')
        lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
        return lowPrice_and_highRating

    def __getStorage(self, budgetPercentage, CASE, MOBO):
        budget = (self.budget * budgetPercentage) // 100 # Calculating budget from given percentage
        budgetLowerBound = budget - ((budget*15)//100)
        budgetUpperBound = budget + ((budget*15)//100)

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
                current_price__gte=float(ssd_price - ((ssd_price*15)//100))).filter(
                current_price__lte=float(ssd_price + ((ssd_price*15)//100))).filter(
                rgb=self.rgb).exclude(
                rating__lte=4.0).exclude(
                last_modified__lt=self.dateOfUpdate)
            
        elif ssd_count > 0  and hdd_count > 0:
            SSD = ssd.objects.filter(
                current_price__gte=float(ssd_price - ((ssd_price*15)//100))).filter(
                current_price__lte=float(ssd_price + ((ssd_price*15)//100))).filter(
                rgb=self.rgb).exclude(
                rating__lte=4.0).exclude(
                last_modified__lt=self.dateOfUpdate)
            
            HDD = hdd.objects.filter(
                current_price__gte=float(hdd_price - ((hdd_price*15)//100))).filter(
                current_price__lte=float(hdd_price + ((hdd_price*15)//100))).filter(
                rgb=self.rgb).exclude(
                rating__lte=4.0).exclude(
                last_modified__lt=self.dateOfUpdate)
        
        if HDD.count() == 0:
            highest_rating = SSD.objects.order_by('-rating')[:5]
            lowest_price = SSD.objects.order_by('current_price')[:5]
            lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
            return lowPrice_and_highRating
        else:
            highest_rating_ssd = SSD.objects.order_by('-rating')[:5]
            lowest_price_ssd = SSD.objects.order_by('current_price')[:5]
            lowPrice_and_highRating_ssd = highest_rating_ssd.intersection(lowest_price_ssd).first()
            highest_rating_hdd = HDD.objects.order_by('-rating')[:5]
            lowest_price_hdd = HDD.objects.order_by('current_price')[:5]
            lowPrice_and_highRating_hdd = highest_rating_hdd.intersection(lowest_price_hdd).first()
            return [lowPrice_and_highRating_ssd, lowPrice_and_highRating_hdd]

    def __getCase(self, budgetPercentage, MOBO, GPU, COOLER):
        # gpu large = case large (only use of relative size)
        # make sure cooler length = case depth
        budget = (self.budget * budgetPercentage) // 100 
        budgetLowerBound = budget - ((budget*15)//100)
        budgetUpperBound = budget + ((budget*15)//100)

        Case = case.objects.filter(
            current_price__gte=budgetLowerBound).filter(
            current_price__lte=budgetUpperBound).filter(
            size=self.formFactor).filter(
            length__gt=GPU.length).exclude(
            last_modified__lt=self.dateOfUpdate)

        highest_rating = Case.objects.order_by('-rating')
        lowest_price = Case.objects.order_by('current_price')
        lowPrice_and_highRating = highest_rating.intersection(lowest_price).first()
        return lowPrice_and_highRating    

    def __getPsu(self, budgetPercentage, CASE, WATTS):
        budget = (self.budget * budgetPercentage)// 100
        HighestPrice = budget + ((budget * 15) // 100)
        LowestPrice = budget - ((budget * 15) // 100)
        Size = self.JSON['formFactor'][0]
        Psu = psu.objects.filter(
            current_price__gte = LowestPrice).filter(
            current_price__lte=HighestPrice).filter(
            size = Size).filter(
            wattage__gte = WATTS).exclude(
            rating__lte=4.0).exclude(
            last_modified__lt=self.dateOfUpdate)

        highest_rating = Psu.objects.order_by('-ratings').order_by('-rating')[:5]
        lowest_price = Psu.objects.order_by('current_price')[:5]
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
            watts = cpu['power_consumption'] + gpu['power_consumption'] + cooler['power_consumption']
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
