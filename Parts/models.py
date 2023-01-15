from django.db import models
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class manufacturer(models.Model):
    manufacturers = (
        ('ASrock', 'ASrock'),
        ('AMD', 'AMD'),
        ('Intel', 'Intel'),
        ('Aorus', 'Aorus'),
        ('Asus', 'Asus'),
        ('Colorful', 'Colorful'),
        ('Cooler Master', 'Cooler Master'),
        ('Corsair', 'Corsair'),
        ('Crucial', 'Crucial'),
        ('EVGA', 'EVGA'),
        ('Gigabyte', 'Gigabyte'),
        ('Gskill', 'Gskill'),
        ('Lian Li', 'Lian Li'),
        ('MSI', 'MSI'), 
        ('Noctua', 'Noctua'),
        ('Nvidia', 'Nvidia'),
        ('NZXT', 'NZXT'),
        ('PNY', 'PNY'),
        ('PowerColor', 'PowerColor'),
        ('Razer', 'Razer'),
        ('Sapphire', 'Sapphire'),
        ('SAMSUNG', 'SAMSUNG'),
        ('Silicon Power', 'Silicon Power'),
        ('TeamGroup', 'TeamGroup'),
        ('Thermaltake', 'Thermaltake'),
        ('Vcolor', 'Vcolor'),
        ('XFX', 'XFX'),
        ('XPG', 'XPG'),
        ('Zotac', 'Zotac'),
        ('Seagate', 'Seagate'),
        ('Western Digital', 'Western Digital'),
        ('Zotac', 'Zotac'),
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

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class commoninfo(models.Model):
    ID                  = models.CharField(primary_key=True, max_length=15)
    manufacturer        = models.ForeignKey('manufacturer',  related_name="%(class)s_related", on_delete=models.CASCADE, default='')
    name                = models.CharField(max_length=200)
    data_added          = models.DateField(auto_now_add=True, null=True)
    amazon_url          = models.URLField(null=True)
    newegg_url          = models.URLField(null=True)
    bestbuy_url         = models.URLField(null=True)
    current_price       = models.FloatField(null=True, blank=True)
    lowest_Price_Link   = models.URLField(null=True, blank=True)

    class Meta:
        abstract = True

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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
        ('DDR3', 'DDR3'),
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
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class computer(models.Model):
    ID            = models.CharField(primary_key=True, max_length=20)
    motherboard   = models.ForeignKey(motherboard, on_delete= models.CASCADE)
    aircooler     = models.ForeignKey(aircooler, null=True, blank=True, on_delete= models.CASCADE)
    watercooler   = models.ForeignKey(watercooler, null=True, blank=True, on_delete= models.CASCADE)
    cpu           = models.ForeignKey(cpu, on_delete= models.CASCADE)
    gpu           = models.ForeignKey(gpu, on_delete= models.CASCADE)
    ram           = models.ForeignKey(ram, on_delete= models.CASCADE)
    ssd1          = models.ForeignKey(ssd, null=True, blank=True, on_delete= models.CASCADE, related_name='ssd1')
    ssd2          = models.ForeignKey(ssd, null=True, blank=True, on_delete= models.CASCADE, related_name='ssd2')
    hdd1          = models.ForeignKey(hdd, null=True, blank=True, on_delete= models.CASCADE, related_name='hdd1')
    hdd2          = models.ForeignKey(hdd, null=True, blank=True, on_delete= models.CASCADE, related_name='hdd')
    psu           = models.ForeignKey(psu, on_delete= models.CASCADE)
    fan1          = models.ForeignKey(fan, null=True, blank=True, on_delete= models.CASCADE, related_name='fan1')
    fan2          = models.ForeignKey(fan, null=True, blank=True, on_delete= models.CASCADE, related_name='fan2')
    fan3          = models.ForeignKey(fan, null=True, blank=True, on_delete= models.CASCADE, related_name='fan3')
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

        
    
