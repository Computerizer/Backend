<<<<<<< HEAD
from turtle import width
from unicodedata import name
from django.test import TestCase
from .models import manufacturer, cpu, aircooler, watercooler, gpu, ram, hdd, ssd, motherboard, psu, fan, case

# Create your tests here.
# This testcase will be an example of a pc build with all parts compatibilty 

class PcTestCase(TestCase):

    def setUp(self):

        """Below are the MANUFACTURERS used in the TestCase"""
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        AMD   = manufacturer.objects.create(ID='AMD', name='AMD', manufactures_cpu=True, manufactures_gpu=True)
        INTEL = manufacturer.objects.create(ID='INT', name='Intel', manufactures_cpu=True, manufactures_gpu=True)
        ASUS = manufacturer.objects.create(ID='ASS', name='Asus', manufactures_gpu=True, manufactures_motherboard=True, manufactures_cooler=True, manufactures_psu=True)
        Corsair = manufacturer.objects.create(ID='COR', name='Corsair', manufactures_cooler=True, manufactures_psu=True)
        MSI = manufacturer.objects.create(ID='MSI', name='MSI', manufactures_gpu=True, manufactures_motherboard=True, manufactures_cooler=True, )
        Gskill = manufacturer.objects.create(ID='GSKL', name='Gskill', manufactures_ram=True, manufactures_ssd=True)
        SAMSUNG = manufacturer.objects.create(ID='SAM', name='SAMSUNG', manufactures_ram=True, manufactures_ssd=True)
        Seagate = manufacturer.objects.create(ID='SG', name='SeaGate', manufactures_hdd=True, manufactures_ssd=True)
        CoolerMaster = manufacturer.objects.create(ID='CM', name='CoolerMaster', manufactures_cooler=True)
        NZXT = manufacturer.objects.create(ID='NZXT', name='NZXT', manufactures_cooler=True, manufactures_case=True)
        Thermaltake = manufacturer.objects.create(ID='TT', name='Thermaltake', manufactures_cooler=True, manufactures_case=True, manufactures_psu=True)
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

        """Below are the CPUS used in the TestCase"""
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        Ryzen_5600x = cpu.objects.create(
            ID='AMDR5600X', 
            name='AMD Ryzen 5 5600X - Ryzen 5 5000 Series Vermeer (Zen 3) 6-Core 3.7 GHz Socket AM4 65W Desktop Processor',
            manufacturer=AMD, 
            model_Name='Ryzen 5600x', 
            cores=6, 
            threads=12, 
            speed=4.6, 
            overclockable=True, 
            socket='AM4',
            cooler=True, 
            power_Consumption=65, 
            integrated_graphics=False, 
            current_price=193.89)

        Core_i9 = cpu.objects.create(
            ID='INTELCI9K', 
            name='Intel Core i9-12900K - Core i9 12th Gen Alder Lake 16-Core (8P+8E) 3.2 GHz LGA 1700 125W Intel UHD Graphics 770 Desktop Processor',
            manufacturer=INTEL, 
            model_Name='Core i9-12900K', 
            cores=16, 
            threads=24, 
            speed=5.2, 
            overclockable=True, 
            socket='LGA 1700',
            cooler=False, 
            power_Consumption=125, 
            integrated_graphics=False, 
            current_price=499.99)
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        
        """Below are the GPUS used in the TestCase"""
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        RTX_3050 = gpu.objects.create(
            ID                   ='NVRTX3050',
            manufacturer         =MSI,
            name                 ='MSI Ventus GeForce RTX 3050 8GB GDDR6 PCI Express 4.0 Video Card RTX 3050 Ventus 2X 8G OC',
            type                 ='Nvidia RTX',
            size                 ='ATX',
            length               =9.25,
            height               =4.88,
            width                =2.0,
            fan_count            =3,
            vram                 =8,
            gddr_type            ='GDDR6',
            cude_cores           =2560,
            base_clock           =1550,
            boost_clock          =1807,
            multimonitor_support =True,
            monitor_count        =4,
            supported_resolution ='8K',
            pcie_5_support       =False,
            pcie_4_support       =True, 
            rgb                  =False, 
            pins_num             =8, 
            has_displayport      =True,
            displayport_count    =3,
            has_hdmi             =True, 
            hdmi_count           =1,
            has_usbc             =False, 
            usbc_count           =0, 
            theme                ='dark', 
            power_consumption    =130,
            use_case             ='Mid-Range',
            current_price        =304.99
        )

        RX_6600 = gpu.objects.create(
            ID                   ='AMDRX6600',
            manufacturer         =ASUS,
            name                 ='ASUS Dual Radeon RX 6600 8GB GDDR6 PCI Express 4.0 Video Card DUAL-RX6600-8G',
            type                 ='AMD Radeon',
            atx                  =True,
            micro_atx            =True,
            mini_atx             =False,
            length               =9.60,
            height               =5.30,
            width                =2.5,
            fan_count            =2,
            vram                 =8,
            gddr_type            ='GDDR6',
            stream_processors    =1792,
            base_clock           =1550,
            boost_clock          =2491,
            multimonitor_support =True,
            monitor_count        =4,
            supported_resolution ='8K',
            pcie_5_support       =False,
            pcie_4_support       =True, 
            rgb                  =False, 
            pins_num             =8, 
            has_displayport      =True,
            displayport_count    =3,
            has_hdmi             =True, 
            hdmi_count           =1,
            has_usbc             =False, 
            usbc_count           =0, 
            theme                ='dark', 
            power_consumption    =132,
            use_case             ='Mid-Range',
            current_price        =249.99,
            )
        
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

        """Below are the RAMs used in the TestCase"""
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        TridentZ = ram.objects.create(
            ID                ='GSKLTR1632002',
            manufacturer      =Gskill,
            name              ='G.SKILL TridentZ RGB Series 16GB (2 x 8GB) 288-Pin PC RAM DDR4 3200 (PC4 25600)',
            capacity          =16,
            divided_capacity  ='8x2', 
            channels          ='Dual',
            height            =44,
            speed             =3200,
            type              ='DDR4',
            pins              =288,
            xmp               =True, 
            color_name        ='Black', 
            color_hex         ='FFFFFF',
            power_consumption =8,
            rgb               =True,
            use_case          ='Mid-Range', 
            current_price     =67.99,
            )

        Ripjaws = ram.objects.create(
            ID                ='GSKLRI3256002',
            manufacturer      =Gskill,
            name              ='G.SKILL Ripjaws S5 Series 32GB (2 x 16GB) DDR5 5600',
            capacity          =32,
            divided_capacity  ='16x2', 
            channels          ='Dual',
            height            =33,
            speed             =5600,
            type              ='DDR5',
            pins              =288,
            xmp               =True, 
            color_name        ='White', 
            color_hex         ='000000',
            power_consumption =16,
            rgb               =False,
            use_case          ='High-end', 
            current_price     =149.99,
            )
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

        """Below are the Aircoolers used in the TestCase"""
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        Hyper212 = aircooler.objects.create(
            ID                ='CMHY212IA',
            manufacturer      =CoolerMaster,
            name              ='Cooler Master Hyper 212 RGB Black Edition CPU Air Cooler',
            socket            ='All',
            size              ='Average',
            height            = 159.0,
            width             = 120.0,
            num_fans          = 2,
            num_heatsinks     = 1,
            color_name        ='Black', 
            color_hex         ='FFFFFF',
            power_consumption =8,
            rgb               =True,
            use_case          ='Budget', 
            current_price     =49.60,
            )
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

        """Below are the Watercoolers used in the TestCase"""
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        KrakenZ73 = watercooler.objects.create(
            ID                ='NZXTKRZ73360',
            manufacturer      =NZXT,
            name              ='NZXT Kraken Z73 360mm Liquid Cooler with LCD Display - Black',
            socket            ='All',
            size              ='Large',
            length            =394.0,
            width             =121.0,
            num_fans          =3, 
            color_name        ='Black', 
            color_hex         ='FFFFFF',
            power_consumption =25,
            rgb               =True,
            use_case          ='High-end', 
            current_price     =299.99,
            )
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

        """Below are the Motherboards used in the TestCase"""
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        MSImag = motherboard.objects.create(
            ID                   ='MSIMAZ690TOMAHAWKATX',
            manufacturer         =MSI,
            name                 ='MSI MAG Z690 TOMAHAWK WIFI DDR4 LGA 1700 ATX Intel Motherboard',
            socket               ='LGA 1700',
            size                 ='ATX',
            ram_slots            =4,
            ddr_5_support        =False, 
            ddr_4_support        =True,
            pcie_5_support       =True, 
            pcie_4_support       =True, 
            wifi                 =True, 
            wifi_6_support       =True,
            lan_support          =True, 
            fan_headers          =6,
            rgb                  =False, 
            rgb_headers          =3,
            argb_headers         =1,
            has_hdmi             =True, 
            hdmi_count           =1,
            has_displayport      =True, 
            displayport_count    =1,
            has_usbc             =True, 
            usbc_count           =1, 
            usb3point2_support   =True, 
            mdot2_SSD_slots      =4, 
            integrated_io_sheild =True, 
            theme                ='Dark', 
            use_case             ='Mid-Range',  
            current_price        =259.99,
        )

        AsusROG = motherboard.objects.create(
            ID                   ='ASSCRVIIIAM4',
            manufacturer         =ASUS,
            name                 ='ASUS ROG Crosshair VIII Dark Hero AM4 AMD X570S',
            socket               ='AM4',
            size                 ='ATX',
            ram_slots            =4,
            ddr_5_support        =False, 
            ddr_4_support        =True,
            pcie_5_support       =False, 
            pcie_4_support       =True, 
            wifi                 =True, 
            wifi_6_support       =True,
            lan_support          =True, 
            fan_headers          =6,
            rgb                  =True, 
            rgb_headers          =3,
            argb_headers         =1,
            has_hdmi             =False, 
            hdmi_count           =0,
            has_displayport      =False, 
            displayport_count    =0,
            has_usbc             =True, 
            usbc_count           =1, 
            usb3point2_support   =True, 
            usb3point2_count     =7,
            usb_count            =11,
            mdot2_SSD_slots      =3, 
            sata_slots           =8, 
            integrated_io_sheild =True, 
            theme                ='Dark', 
            use_case             ='High-end',  
            current_price        =459.99,
        )      
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

        """Below are the HDDs and SSDs used in the TestCase"""
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        SeagateHDD = hdd.objects.create(
            ID                ='SGB4TB540035',
            manufacturer      =Seagate,
            name              ='Seagate BarraCuda ST4000DM004 4TB 5400 RPM 256MB Cache SATA 6.0Gb/s 3.5',
            capacity          =4000,
            cache             =256,
            speed             =5400,
            size              =3.5,
            connectivity      ='SATA',
            rgb               =False,
            power_consumption =25, 
            use_case          ='Budget', 
            current_price     =67.99,
        )

        Ironwolf = hdd.objects.create(
            ID                ='SGIW8TB720035',
            manufacturer      =Seagate,
            name              ='Seagate IronWolf Pro 8TB NAS Hard Drive 7200 RPM',
            capacity          =8000,
            cache             =256,
            speed             =7200,
            size              =3.5,
            connectivity      ='SATA',
            rgb               =False,
            power_consumption =35, 
            use_case          ='High-end', 
            current_price     =229.99,
        )

        SamsungEVO = ssd.objects.create(
            ID                ='SAM970EVM22TB',
            manufacturer      =SAMSUNG,
            name              ='SAMSUNG 970 EVO PLUS M.2 2280 2TB PCIe Gen 3.0 x4',
            capacity          =2000,
            read_speed        =3500,
            write_speed       =3300, 
            form_factor       ='M.2', 
            height            =2.38, 
            interface         ='PCIe-Express 3.0', 
            power_consumption =30, 
            rgb               =False,
            use_case          ='High-end', 
            current_price     =229.99,
        )
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""


        """Below are the PSUs used in the TestCase"""
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        Thermaltakepsu = psu.objects.create(
            ID                ='TTBM2550BATX',
            manufacturer      =Thermaltake,
            name              ='SAMSUNG 970 EVO PLUS M.2 2280 2TB PCIe Gen 3.0 x4',
            wattage           =550,
            rating            ='Bronze',
            connection        ='None Modular',
            size              ='ATX',
            color_name        ='Black',
            color_hex         ='FFFFF', 
            rgb               =True,
            use_case          ='Budget', 
            current_price     =39.99,
        )

        Corsairpsu = psu.objects.create(
            ID                ='CorsairRM1000ATX ',
            manufacturer      =Corsair,
            name              ='CORSAIR RMx Series (2021) RM1000x CP-9020201-NA 1000 W ATX12V',
            wattage           =1000,
            rating            ='Bronze',
            connection        ='Full Modular',
            size              ='ATX',
            color_name        ='Black',
            color_hex         ='FFFFF', 
            rgb               =False,
            use_case          ='High-end', 
            current_price     =189.99,
        )
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""


        """Below are the Fans used in the TestCase"""
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        NZXThighfan = psu.objects.create(
            ID                    ='NZXTAER2140',
            manufacturer          =NZXT,
            name                  ='NZXT AER RGB 2 - 140mm - RGB LED - Fluid Dynamic Bearing - PWM Fan for Hue 2 - Single',
            size                  =140,
            lowest_rpm            =500, 
            highest_rpm           =1500, 
            rgb                   =True,
            connection            =4,
            color_name            ='Black', 
            color_hex             ='FFFFF', 
            theme                 ='Dark', 
            use_case              ='High-end',
            current_price         =40.0,
        )

        NZXTlowfan = psu.objects.create(
            ID                    ='NZXTAERF120',
            manufacturer          =NZXT,
            name                  ='NZXT Aer F120P Black - High Performance Airflow Fans - Single',
            size                  =120,
            lowest_rpm            =500, 
            highest_rpm           =1500, 
            rgb                   =False,
            connection            =4,
            color_name            ='Black', 
            color_hex             ='FFFFF', 
            theme                 ='Dark', 
            use_case              ='Budget',
            current_price         =13.2,
        )
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""


        """Below are the Cases used in the TestCase"""
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
        NZXTlowfan = psu.objects.create(
            ID                    ='NZXTH510MTB',
            manufacturer          =NZXT,
            name                  ='NZXT H510 - Compact ATX Mid-Tower PC Gaming Case',
            mobo_support          =3,
            height                =17.13,
            width                 =8.27,
            depth                 =16.85,
            max_gpu_length        =381,
            max_cpu_cooler_heigth =165,
            rgb                   =False,
            has_fans              =True, 
            num_fans              =2, 
            max_num_number        =5,
            max_fan_size          =140, 
            io                    ='1 x USB 3.0 Type-A / 1 x USB 3.1 Gen 2 Type-C / 1x Headset audio Jack', 
            color_name            ='Black', 
            color_hex             ='FFFFF', 
            theme                 ='Dark', 
            use_case              ='Mid-Range',
            current_price         =87.99,
        )
        """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

        pass


    def test_intel_pc():
        pass

    def test_amd_pc():
        pass

    def test_atx_pc():
        pass

    def test_miniatx_pc():
        pass

    def test_wrong_pc():
        pass
=======
from django.test import TestCase

# Create your tests here.
>>>>>>> New-Frontend
