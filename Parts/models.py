from django.db import models
from django.contrib.postgres import *
from datetime import datetime
from django.utils import timezone

class manufacturer(models.Model):
    manufacturers = (
        ('asrock', 'asrock'),
        ('amd', 'amd'),
        ('intel', 'intel'),
        ('aorus', 'aorus'),
        ('asus', 'asus'),
        ('colorful', 'colorful'),
        ('coolermaster', 'coolermaster'),
        ('corsair', 'corsair'),
        ('crucial', 'crucial'),
        ('evga', 'evga'),
        ('gigabyte', 'gigabyte'),
        ('gskill', 'gskill'),
        ('lianli', 'lianli'),
        ('msi', 'msi'), 
        ('noctua', 'noctua'),
        ('nvidia', 'nvidia'),
        ('nzxt', 'nzxt'),
        ('pny', 'pny'),
        ('powercolor', 'powercolor'),
        ('razer', 'razer'),
        ('sapphire', 'sapphire'),
        ('samsung', 'samsung'),
        ('siliconpower', 'siliconpower'),
        ('teamGroup', 'teamGroup'),
        ('thermaltake', 'thermaltake'),
        ('vcolor', 'vcolor'),
        ('xfx', 'xfx'),
        ('xpg', 'xpg'),
        ('zotac', 'zotac'),
        ('seagate', 'seagate'),
        ('westerndigital', 'westerndigital'),
        ('zotac', 'zotac'),
    )
    ID   = models.CharField(primary_key=True, null=False, blank=False, max_length=10)
    name = models.CharField(max_length=50, null=True, blank=True)
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
    manufacturer        = models.ForeignKey('manufacturer',  related_name="%(class)s_related", on_delete=models.CASCADE, default='')
    name                = models.CharField(max_length=200)
    data_added          = models.DateField(auto_now_add=True, null=True)
    amazon_url          = models.JSONField(null=True)
    newegg_url          = models.JSONField(null=True)
    bestbuy_url         = models.JSONField(null=True)
    rating              = models.FloatField(null=True)
    amazon_price        = models.FloatField(null=True)
    newegg_price        = models.FloatField(null=True)
    bestbuy_price       = models.FloatField(null=True)
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
    model_name          = models.CharField(max_length=20)
    cores               = models.PositiveIntegerField()
    threads             = models.PositiveIntegerField()
    speed               = models.FloatField()
    overclockable       = models.BooleanField()
    socket              = models.CharField(choices=Sockets, max_length=15)
    cooler              = models.BooleanField(help_text='eg: amd ryzen 3600', verbose_name='Comes with cooler')
    power_consumption   = models.PositiveIntegerField(null=True)
    integrated_graphics = models.BooleanField()
    use_case            = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

    def __str__(self):
        return f"{self.Model_name} ({self.ID})"

    class Meta:
        verbose_name ='CPU'
        verbose_name_plural ='CPUs'

    def is_valid_cpu(self):
        condition = True
        manufacturer = self.manufacturer
        if manufacturer.manufactures_cpu == False:
            print('This manufacturer does not make cpus')
            condition = False
        if self.threads > self.cores:
            condition = False
        if (manufacturer.name.lower() == 'intel') and (self.cooler == True):
            condition = False
        return condition

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class aircooler(commoninfo):
    sockets = [
        ('AM4', 'AM4'),
        ('LGA 1700', 'LGA 1700'),
        ('LGA 1200', 'LGA 1200'),
        ('LGA 1151', 'LGA 1151'),
        ('All', 'AMD INTEL'),
    ]

    sizes = (
        ('Large', 'Large'),
        ('Average', 'Average'),
        ('Small', 'Small')
    )
    socket            = models.CharField(choices=sockets, max_length=15)
    size              = models.CharField(choices=sizes, max_length=10)
    height            = models.FloatField()
    width             = models.FloatField()
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
        condition = True
        manufacturer = self.manufacturer
        if manufacturer.manufactures_cooler == False:
            print('This manufacturer does not make coolers')
            condition = False
        if (self.price < 50.0) and (self.use_case == 'High-end'):
            condition = False
        if (self.color_name.lower() == 'black') and (self.theme == 'light'):
            condition = False
        return condition

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class watercooler(commoninfo):
    sockets = (
        (1, 'AM4'),
        (2, 'LGA 1700'),
        (3, 'LGA 1200'),
        (4, 'LGA 1151'),
        (5, 'LGA 1700 and LGA 1151'),
        (6, 'AM4 and LGA 1700 and LGA 1151'),
    )

    sizes = (
        ('Large', 'Large'),
        ('Average', 'Average'),
        ('Small', 'Small')
    )
    socket            = models.IntegerField(choices=sockets)
    size              = models.CharField(choices=sizes, max_length=10)
    length            = models.FloatField()
    width             = models.FloatField()
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
        condition = True
        manufacturer = self.manufacturer
        if manufacturer.manufactures_cpu == False:
            print('This manufacturer does not make cpus')
            condition = False
        if self.threads > self.cores:
            condition = False
        if (manufacturer.name.lower() == 'intel') and (self.cooler == True):
            condition = False
        return condition

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class gpu(commoninfo):
    type                 = models.CharField(choices=(('Nvidia GTX','Nvidia GTX'), ('Nvidia RTX','Nvidia RTX'), ('AMD Radeon', 'AMD Radeon')), max_length=15, verbose_name='Type')
    atx                  = models.BooleanField(null=True, blank=True)
    micro_atx            = models.BooleanField(null=True, blank=True)
    mini_itx             = models.BooleanField(null=True, blank=True)
    length               = models.FloatField(help_text='*in inches')
    height               = models.FloatField(help_text='*in inches')
    width                = models.FloatField(help_text='*in inches')
    fan_count            = models.IntegerField(choices=((0, 0), (1, 1), (2, 2), (3, 3)))
    vram                 = models.PositiveIntegerField(verbose_name='Memory (VRAM)')
    gddr_type            = models.CharField(choices=(("GDDR6X", "GDDR6X"), ('GDDR6', 'GDDR6'), ('GDDR5X', 'GDDR5X'), ('GDDR5', 'GDDR5')), verbose_name='GDDR', max_length=10)
    cude_cores           = models.IntegerField(null=True, blank=True)
    stream_processors    = models.IntegerField(null=True, blank=True)
    base_clock           = models.IntegerField() #in MHz
    boost_clock          = models.IntegerField() #in MHz
    multimonitor_support = models.BooleanField()
    monitor_count        = models.PositiveIntegerField() 
    supported_resolution = models.CharField(verbose_name='Maximum supported resolutions', choices=(('1K', '1K'), ('2K', '2K'), ('4K', '4K'), ('5K', '5K'), ('8K', '8K')), max_length=5)
    pcie_5_support       = models.BooleanField(verbose_name='Supports PCIe 5') #  gen of either pcie or ddr, then 
    pcie_4_support       = models.BooleanField(verbose_name='Supports PCIe 4') #  it automatically supports gen 4
    rgb                  = models.BooleanField(verbose_name='RGB Lighting', help_text="ONLY RGB LIGHT THAT'S PART OF THE MOBO")
    pins_num             = models.PositiveIntegerField(verbose_name='Pins required', help_text='Number of pins to power the card')
    has_displayport      = models.BooleanField()
    displayport_count    = models.PositiveIntegerField()
    has_hdmi             = models.BooleanField()
    hdmi_count           = models.PositiveIntegerField()
    has_usbc             = models.BooleanField(verbose_name='Supports USB-C')
    usbc_count           = models.PositiveIntegerField(verbose_name='USB-C ports count')
    theme                = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), verbose_name='Color Theme', max_length=15)
    power_consumption    = models.PositiveIntegerField(null=True) #In watts
    use_case             = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name ='GPU'
        verbose_name_plural ='GPUs'

    def is_valid_gpu(self):
        condition = True
        if (self.has_hdmi == True and self.hdmi_count > 0) and (self.has_displayport == True and self.displayport_count > 0) and \
        (self.has_usbc == True and self.usbc_count > 0) and (self.base_clock < self.boost_clock) and (self.pcie_4_support == True and self.pcie_5_support == True):
            condition = True
        return condition

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class motherboard(commoninfo):

    Sockets = (
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
    ram_slots            = models.IntegerField(choices=((4,4), (2,2)), verbose_name='How many ram slots',null=True, blank=True)
    ddr_5_support        = models.BooleanField(verbose_name='Supports DDR5 RAM') # please note:
    ddr_4_support        = models.BooleanField(verbose_name='Supports DDR4 RAM') #  - if a mobo supports a 5th 
    pcie_5_support       = models.BooleanField(verbose_name='Supports PCIe 5') #  gen of either pcie or ddr, then 
    pcie_4_support       = models.BooleanField(verbose_name='Supports PCIe 4') #  it automatically supports gen 4
    wifi                 = models.BooleanField(help_text='Does it allow WIFI connectivity (without a cable)', verbose_name='Supports Wireless Connectivity')
    wifi_6_support       = models.BooleanField(verbose_name='Supports WIFI 6')
    lan_support          = models.BooleanField(verbose_name='Supports LAN Connectivity')
    fan_headers          = models.PositiveIntegerField(help_text='How many fan pins on the motherboards, basically how many fans can be directly connected \n Check motherboard description on official website for more help', verbose_name='Fan Headers count')
    rgb                  = models.BooleanField(verbose_name='RGB Lighting', help_text="ONLY RGB LIGHT THAT'S PART OF THE MOBO")
    rgb_headers          = models.PositiveIntegerField(verbose_name='RGB Headers count', help_text='How many pins onboard can be used to power RGB in other components')
    argb_headers         = models.PositiveIntegerField()
    has_hdmi             = models.BooleanField()
    hdmi_count           = models.PositiveIntegerField()
    has_displayport      = models.BooleanField()
    displayport_count    = models.PositiveIntegerField()
    has_usbc             = models.BooleanField(verbose_name='Supports USB-C')
    usbc_count           = models.PositiveIntegerField(verbose_name='USB-C ports count')
    usb3point2_support   = models.BooleanField(verbose_name='USB3.2 support')
    usb3point2_count     = models.IntegerField(verbose_name='USB3.2 count', null=True)
    usb_count            = models.IntegerField(verbose_name='USB count', null=True)
    mdot2_SSD_slots      = models.PositiveIntegerField(verbose_name='Number of M.2 slots')
    sata_slots           = models.PositiveIntegerField(verbose_name='Number of SATA slots', null=True)
    integrated_io_sheild = models.BooleanField(help_text='Does it have a built in cover on the rear ports', verbose_name='Integrated IO sheild')
    theme                = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), verbose_name='Color Theme', max_length=15)
    use_case             = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name ='Motherboard'
        verbose_name_plural ='Motherboards'

    def is_valid_motherboard(self):
        condition = True
        if (self.wifi == False and self.wifi_6_support == True) or (self.has_hdmi == False and self.hdmi_count > 0) or (self.has_displayport == False and self.displayport_count > 0) or (self.has_usbc == False and self.usbc_count > 0):
            condition = False
        return condition

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
    height            = models.FloatField(verbose_name="How tall", help_text='In mm (milimeter')
    speed             = models.IntegerField() 
    type              = models.CharField(choices=ddr_type, max_length=5)
    pins              = models.PositiveIntegerField()
    xmp               = models.BooleanField()
    color_name        = models.CharField(default='Black', max_length=15) #Write the color name corresponding to the Hex value below 
    color_hex         = models.CharField(default='#RRGGBB', max_length=8) #Write the color value as a hex string
    power_consumption = models.PositiveIntegerField(null=True)
    rgb               = models.BooleanField()
    use_case          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name ='RAM'
        verbose_name_plural ='RAMs'

    def is_valid_ram(self):
        condition = True
        manufacturer = self.manufacturer
        if manufacturer.manufactures_cpu == False:
            print('This manufacturer does not make cpus')
            condition = False
        if self.threads > self.cores:
            condition = False
        if (manufacturer.name.lower() == 'intel') and (self.cooler == True):
            condition = False
        return condition

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class hdd(commoninfo):
    rpm = (
        (3600, 3600),
        (4200, 4200),
        (5400, 5400),
        (7200, 7200),
        (1000, 1000)
    )

    sata = (
        (1.0, 1.0),
        (1.5, 1.5),
        (3.0, 3.0),
        (6.0, 6.0),
    )

    cache = (
        (64, 64),
        (128, 128),
        (256, 256),
        (512, 512),
    ) #in megabytes

    size = (
        (1, 1),
        (1.8, 1.8),
        (2.5, 2.5),
        (3.5, 3.5),
    ) #in inches
    capacity          = models.PositiveIntegerField() #in gb, tb values will be altered on the frontend 
    cache             = models.PositiveIntegerField() #in mb, tb values will be altered on the frontend 
    speed             = models.PositiveIntegerField(choices=rpm) #in GhZ
    size              = models.FloatField(choices=size, null=True) #in GhZ
    connectivity      = models.CharField(help_text='What is the connectivity type, (eg: number of pins, cable type)', max_length=20)
    rgb               = models.BooleanField()
    power_consumption = models.PositiveIntegerField(null=True)
    use_case          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name ='HDD'
        verbose_name_plural ='HDDs'

    def is_valid_hdd(self):
        condition = True
        manufacturer = self.manufacturer
        if manufacturer.manufactures_cpu == False:
            print('This manufacturer does not make cpus')
            condition = False
        if self.threads > self.cores:
            condition = False
        if (manufacturer.name.lower() == 'intel') and (self.cooler == True):
            condition = False
        return condition

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    

class ssd(commoninfo):
    connectivity = (
        ('SATA 3', 'SATA 3'),
        ('Micro-SATA', 'Micro-SATA'),
        ('Mini-SATA', 'Mini-SATA'),
        ('Mini-PCIe', 'Mini-PCIe'),
        ('PCIe-Express 3.0', 'PCIe-Express 3.0'),
        ('PCIe-Express 3.1', 'PCIe-Express 3.1'),
        ('PCIe-Express 4.0', 'PCIe-Express 4.0'),
        ('PCIe-Express 4.0', 'PCIe-Express 4.0'),
        ('Thunderbolt 3', 'Thunderbolt 3'),
    )

    size = (
        ('1.0', '1.0'),
        ('2.5', '2.5'),
        ('3.5', '3.5'),
        ('M.2', 'M.2'),
        ('mSATA', 'mSATA'),
        ('AIC', 'AIC'),
    ) #in inches
    capacity          = models.PositiveIntegerField() #in gb, tb values will be altered on the frontend 
    read_speed        = models.PositiveIntegerField() #in MbPs
    write_speed       = models.PositiveIntegerField() #in MbPs
    form_factor       = models.CharField(choices=size, max_length=20)
    height            = models.FloatField()
    interface         = models.CharField(choices=connectivity, help_text='What is the connectivity type, (eg: number of pins, cable type)', max_length=20)
    power_consumption = models.PositiveIntegerField(null=True)
    rgb               = models.BooleanField()
    use_case          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name ='SSD'
        verbose_name_plural ='SSDs'

    def is_valid_ssd(self):
        condition = True
        manufacturer = self.manufacturer
        if manufacturer.manufactures_cpu == False:
            print('This manufacturer does not make cpus')
            condition = False
        if self.threads > self.cores:
            condition = False
        if (manufacturer.name.lower() == 'intel') and (self.cooler == True):
            condition = False
        return condition

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
        (1, 'ATX only'),
        (2, 'Micro-ATX'),
        (3, 'ATX and Micro-ITX'),
        (4, 'Micro-ATX and Mini-ITX'),
        (4, 'Mini-ITX only'),
    )
    wattage           = models.PositiveIntegerField()
    rating            = models.CharField(choices=ratings, max_length=10)
    connection        = models.CharField(choices=connectivity, max_length=15)
    size              = models.IntegerField(choices=mobo_size)
    color_name        = models.CharField(default='Black', max_length=15) #Write the color name corresponding to the Hex value below 
    color_hex         = models.CharField(default='#RRGGBB', max_length=8) #Write the color value as a hex string 
    rgb               = models.BooleanField()
    use_case          = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)
    def __str__(self):
        return f"{self.ID}: {self.name}"
    
    class Meta:
        verbose_name ='PSU'
        verbose_name_plural ='PSUs'

    def is_valid_psu(self):
        condition = True
        manufacturer = self.manufacturer
        if manufacturer.manufactures_cpu == False:
            print('This manufacturer does not make cpus')
            condition = False
        if self.threads > self.cores:
            condition = False
        if (manufacturer.name.lower() == 'intel') and (self.cooler == True):
            condition = False
        return condition

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
    mobo_size = (
        (1, 'ATX only'),
        (2, 'Micro-ATX'),
        (3, 'ATX and Micro-ITX'),
        (4, 'Micro-ATX and Mini-ITX'),
        (4, 'Mini-ITX only'),
    )
    mobo_support          = models.IntegerField(choices=mobo_size, null=True)
    height                = models.FloatField()
    width                 = models.FloatField()
    depth                 = models.FloatField()
    max_gpu_length        = models.FloatField(null=True, blank=True)
    max_cpu_cooler_heigth = models.FloatField(null=True, blank=True)
    rgb                   = models.BooleanField()
    has_fans              = models.BooleanField()
    num_fans              = models.PositiveIntegerField()
    max_num_number        = models.IntegerField(null=True)
    max_fan_size          = models.PositiveIntegerField(null=True)
    io                    = models.TextField(null=True)
    color_name            = models.CharField(default='Black', max_length=15) #Write the color name corresponding to the Hex value below 
    color_hex             = models.CharField(default='#RRGGBB', max_length=8) #Write the color value as a hex string  
    theme                 = models.CharField(choices=(('dark', 'dark'), ('light', 'light')), verbose_name='Color Theme', max_length=15)
    use_case              = models.CharField(choices=(('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')), max_length=15)    
    def __str__(self):
        return f"{self.name} ({self.ID})"

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'

    def is_valid_case(self):
        condition = True
        if self.has_fans == False and self.num_fans > 0:
            condition = False
        return condition

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class computer(models.Model):
    ID            = models.CharField(primary_key=True, max_length=20)
    motherboard   = models.ForeignKey(motherboard, on_delete= models.CASCADE)
    aircooler     = models.ForeignKey(aircooler, null=True, blank=True, on_delete= models.CASCADE)
    watercooler   = models.ForeignKey(watercooler, null=True, blank=True, on_delete= models.CASCADE)
    cpu           = models.ForeignKey(cpu, on_delete= models.CASCADE)
    gpu           = models.ForeignKey(gpu, on_delete= models.CASCADE)
    ram           = models.ForeignKey(ram, on_delete= models.CASCADE)
    ssd           = models.ForeignKey(ssd, null=True, blank=True, on_delete= models.CASCADE, related_name='ssd1')
    hdd           = models.ForeignKey(hdd, null=True, blank=True, on_delete= models.CASCADE, related_name='hdd1')
    psu           = models.ForeignKey(psu, on_delete= models.CASCADE)
    case          = models.ForeignKey(case, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.ID}"

    class Meta:
        verbose_name = 'Computer'
        verbose_name_plural = 'Computers'

    def is_valid_computer(self):
        condition = True 
        if gpu.length > case.length:
            condition = False

        if aircooler.height > case.depth:
            condition = False

        if cpu.socket != motherboard.socket:
            condition = False

        ram_capacity = ['4x4', '8x4', '16x4', '32x4']
        for i in ram_capacity:
            if (ram.ram_capacity == i) and (motherboard.ram_slots == 2):
                condition = False

        if (case.size == 'Mini-ITX') and (motherboard.size == 'ATX' or 'Micro-ATX'):
            condition= False

        return condition
    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#                                       ALGORITHM                                       #
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Developement to be done on Jupyter Notebooks 
class algorithm:
    def __init__(self, JSON):
        self.budget = int(JSON['budget'])
        self.fps = int(JSON['fps'])
        self.resolution = int(JSON['resolution'])
        self.gametype = str(JSON['gametype'])
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
        #Percents in the order: CPU - GPU - MOBO - RAM - STORAGE - COOLER - PSU - CASE
        #The part parameter is to be send as an argument from the calling function(eg:0 is CPU, 2 if RAM)
        partPercentages = {
        500: [16, 33, 21, 5, 4, 4, 7, 10],
        750: [21, 37, 22, 4, 4, 4, 3, 5],
        1000:[21, 37, 16, 5, 5, 8, 7, 7],
        1250:[17, 38, 15, 5, 5, 6, 8, 6],
        1500:[19, 35, 13, 6, 6, 9, 6, 6],
        1750:[16, 48, 12, 3, 4, 8, 5, 5],
        2000:[0, 0, 0, 0, 0, 0, 0, 0],
        2250:[0, 0, 0, 0, 0, 0, 0, 0],
        2500:[0, 0, 0, 0, 0, 0, 0, 0],
        2750:[0, 0, 0, 0, 0, 0, 0, 0],
        3000:[0, 0, 0, 0, 0, 0, 0, 0],
        3250:[0, 0, 0, 0, 0, 0, 0, 0],
        3500:[0, 0, 0, 0, 0, 0, 0, 0],
        3750:[0, 0, 0, 0, 0, 0, 0, 0],
        4000:[0, 0, 0, 0, 0, 0, 0, 0],
        }
        percents = partPercentages[self.budget]
        return percents[part]

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
    def __getCpu(self, budgetPercentage):
        # All CPUs are firstly filtered by budget from the CPUs table
        # The formFactor and purpose paramters play a role in deciding which CPU to choose
        # This is because some CPUs emit too much heat, and consume so much power, hence
        # they can not be used in mini-ITX or console killer builds for example
        # So the rule will be to filter out CPUs based on a combination of budget 
        # and the other paramters, and you can use the formFactor and purpose fields 
        # in the CPU table to help, for example the i9 is both table top and work machine,
        # and its also for ATX builds.
        pass
    
    # Omar
    def __getGpu(self, budgetPercentage):
        # The GPU is a bit more complicated than the CPU
        # As there are many parameters involved 
        # 1) Performance as in resolution, FPS, gametype, and boostclock.
        # 2) Maximizing GPU performance utilization from motherboard,
        # for example if the mobo doesn't support PCIe5, there is no need to suggest a PCIe5 GPU
        # And for that you can use the (supported_resolution, boost_clock, etc) fields
        pass
    
    # Omar
    def __getRam(self, budgetPercentage, MOBO, CPU):
        # Follow the same previous pattern, first filter by budget
        # Next filter any ram sets that exceed the maximum slot number on the mobo
        # Then check if the mobo and cpu support DDr5, if so then suggest a DDr5 ram set
        # If not then filter out anything that is DDr5 and keep the DDr4
        pass
    
    # Emad
    def __getMobo(self, budgetPercentage, CPU):
        # Choosing a motherboard is pretty simple 
        # Firstly filter by budget, then by theme.
        # Then we filter based on our CPU choice (CPU-socket field), AMD and Intel use different mobos
        # Finally we filter based on formFactor: ATX, Micro-ATX, or Mini-ITX
        budget = (self.budget * budgetPercentage) // 100 # Calculating budget from given percentage
        budgetLowerBound = budget - ((budget*15)//100)
        budgetUpperBound = budget + ((budget*15)//100)
        cpuSocket = CPU.socket # String val, either: AM4, LGA1700, LGA1200
        currentDate = datetime.today()
        dateOfUpdate = currentDate - timedelta(days=4) #Older than 4 days ago from today
        mobo = cpu.objects.filter(
            socket=cpuSocket).filter(
            current_price__gte=budgetLowerBound).filter(
            current_price__lte=budgetUpperBound).filter(
            size=self.formFactor).filter(
            rgb=self.rgb).filter(
            theme=self.theme).exclue(
            rating__lte=4.0).exclude(
            last_modified__lt=dateOfUpdate)

        highest_rating = mobo.objects.order_by('-rating')[:3]
        lowest_price = mobo.objects.order_by('current_price')[:3]
        lowPrice_and_highRating = highest_rating.intersection(lowest_price)
        return lowPrice_and_highRating
        
    # Yusuf
    def __getCooler(self, budgetPercentage, CPU, MOBO):
        # Again filter anything outside the budget range 
        # Based on formFactor(ATX-Micro-Mini), purpose, budget, and the cpu type
        # choose either a water or air cooler (criteria can include intend of the pc
        # and how much heat the CPU releases, wich can be estimated by its name and wattage)
        # Finally filter out any coolers that aren't compatible with the motherboard/CPU
        pass
    
    # Emad
    def __getStorage(self, budgetPercentage, CASE, MOBO):
        # Follow the same previous pattern, first filter by budget
        # An SSD must hold the main OS at least, and preferablly be as fast as possible
        # There for check for the fastest SSD sockets going down, and filter out as you go
        # You can do so by checking sockets on the motherboard, using relative fields 
        # At the end filter what's left based on the fastest speed and highest storage
        pass
    
    # Yusuf
    def __getCase(self, budgetPercentage, MOBO, GPU, COOLER):
        # Obviously, we filter by price/budget firstly 
        # Then we fitler based on the formfactor (ATX, micro, or mini)
        # Then we filter cases left to fit the maximum width of the gpu
        # We also make sure that the cooler fits in the case,
        # if its an aircooler then we check for height and clearance, 
        # if its a watercooler, then check that the radiator fits 
        pass
    
    # Omar
    def __getPsu(self, budgetPercentage, CASE, WATTS):
        # Filter out by budget 
        # Then filter out based on formFactor (ATX, ITX, etc)
        # Then filter for the minimum required watts given in the parameter 
        # Finally go from the highest rating (Platinum) to lowest (Bronze), 
        # check if there is any psu from the higher ratings, keep it and remove all else
        pass

    def getComputer(self):    
        cpu = self.__getCpu(self.getPercents(0))
        mobo = self.__getMobo(self.getPercents(2), cpu)
        cooler = self.__getCooler(self.getPercents(5), cpu, mobo)
        gpu = self.__getGpu(self.getPercents(1))
        case = self.__getCase(self.getPercents(7), mobo, gpu, cooler)
        ram = self.__getRam(self.getPercents(3), mobo, cpu)
        storage = self.__getStorage(self.getPercents(4), case, mobo)
        watts = cpu['power_consumption'] + gpu['power_consumption'] + cooler['power_consumption']
        psu = self.__getPsu(self.getPercents(6), case, watts)
        
        #Before returning the PC to the views, we should run some error checking and integration checking
        condition = False
        if mobo.socket == cpu.socket:
            if case.width > gpu.length:
                if cooler.height < case.depth:
                    condition = True
        else:
            condition = False 
            
        if condition is True:
            return[cpu, mobo, cooler, gpu, case, ram, storage, psu]
        else:
            raise LookupError
        

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