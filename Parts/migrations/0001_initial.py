# Generated by Django 4.0.8 on 2023-08-24 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aircooler',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('amazon_url', models.TextField(null=True)),
                ('newegg_url', models.TextField(null=True)),
                ('partRating', models.FloatField(blank=True, null=True)),
                ('amazon_price', models.FloatField(null=True)),
                ('newegg_price', models.FloatField(null=True)),
                ('previous_price', models.FloatField(default=0.0, null=True)),
                ('current_price', models.FloatField(blank=True, null=True)),
                ('lowest_Price_Link', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('socket', models.CharField(choices=[('AM4', 'AM4'), ('LGA 1700', 'LGA 1700'), ('LGA 1200', 'LGA 1200'), ('LGA 1151', 'LGA 1151'), ('All', 'AMD INTEL')], max_length=15)),
                ('size', models.CharField(choices=[('ATX', 'ATX'), ('MicroAtx', 'MicroAtx'), ('MiniItx', 'MiniItx')], max_length=10)),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('num_fans', models.PositiveIntegerField()),
                ('num_heatsinks', models.PositiveIntegerField()),
                ('color_name', models.CharField(default='Black', max_length=15)),
                ('color_hex', models.CharField(default='#RRGGBB', max_length=8)),
                ('rgb', models.BooleanField()),
                ('power_consumption', models.IntegerField(null=True)),
                ('theme', models.CharField(choices=[('dark', 'dark'), ('light', 'light')], max_length=10, verbose_name='Color Theme')),
                ('use_case', models.CharField(choices=[('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')], max_length=15)),
            ],
            options={
                'verbose_name': 'Aircooler',
                'verbose_name_plural': 'Aircoolers',
            },
        ),
        migrations.CreateModel(
            name='case',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('amazon_url', models.TextField(null=True)),
                ('newegg_url', models.TextField(null=True)),
                ('partRating', models.FloatField(blank=True, null=True)),
                ('amazon_price', models.FloatField(null=True)),
                ('newegg_price', models.FloatField(null=True)),
                ('previous_price', models.FloatField(default=0.0, null=True)),
                ('current_price', models.FloatField(blank=True, null=True)),
                ('lowest_Price_Link', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('mobo_support', models.IntegerField(choices=[('ATX', 'ATX'), ('Micro-ATX', 'Micro-ATX'), ('Mini-ITX', 'Mini-ITX')], null=True)),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('depth', models.FloatField()),
                ('max_gpu_length', models.FloatField(blank=True, null=True)),
                ('max_cpu_cooler_heigth', models.FloatField(blank=True, null=True)),
                ('rgb', models.BooleanField()),
                ('has_fans', models.BooleanField()),
                ('num_fans', models.PositiveIntegerField()),
                ('max_num_number', models.IntegerField(null=True)),
                ('max_fan_size', models.PositiveIntegerField(null=True)),
                ('io', models.TextField(null=True)),
                ('color_name', models.CharField(default='Black', max_length=15)),
                ('color_hex', models.CharField(default='#RRGGBB', max_length=8)),
                ('theme', models.CharField(choices=[('dark', 'dark'), ('light', 'light')], max_length=15, verbose_name='Color Theme')),
                ('use_case', models.CharField(choices=[('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')], max_length=15)),
            ],
            options={
                'verbose_name': 'Case',
                'verbose_name_plural': 'Cases',
            },
        ),
        migrations.CreateModel(
            name='manufacturer',
            fields=[
                ('ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('manufactures_cpu', models.BooleanField(blank=True, null=True, verbose_name='Makes CPU')),
                ('manufactures_gpu', models.BooleanField(blank=True, null=True, verbose_name='Makes GPU')),
                ('manufactures_motherboard', models.BooleanField(blank=True, null=True, verbose_name='Makes Motherboards')),
                ('manufactures_ram', models.BooleanField(blank=True, null=True, verbose_name='Makes RAM')),
                ('manufactures_ssd', models.BooleanField(blank=True, null=True, verbose_name='Makes SSD')),
                ('manufactures_hdd', models.BooleanField(blank=True, null=True, verbose_name='Makes HDD')),
                ('manufactures_psu', models.BooleanField(blank=True, null=True, verbose_name='Makes PSU')),
                ('manufactures_case', models.BooleanField(blank=True, null=True, verbose_name='Makes Cases')),
                ('manufactures_cooler', models.BooleanField(blank=True, null=True, verbose_name='Makes Coolers')),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.CreateModel(
            name='watercooler',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('amazon_url', models.TextField(null=True)),
                ('newegg_url', models.TextField(null=True)),
                ('partRating', models.FloatField(blank=True, null=True)),
                ('amazon_price', models.FloatField(null=True)),
                ('newegg_price', models.FloatField(null=True)),
                ('previous_price', models.FloatField(default=0.0, null=True)),
                ('current_price', models.FloatField(blank=True, null=True)),
                ('lowest_Price_Link', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('socket', models.IntegerField(choices=[(1, 'AM4'), (2, 'LGA 1700'), (3, 'LGA 1200'), (4, 'LGA 1151'), (5, 'LGA 1700 and LGA 1151'), (6, 'AM4 and LGA 1700 and LGA 1151')])),
                ('size', models.CharField(choices=[('Large', 'Large'), ('Average', 'Average'), ('Small', 'Small')], max_length=10)),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('num_fans', models.PositiveIntegerField()),
                ('color_name', models.CharField(default='Black', max_length=15)),
                ('color_hex', models.CharField(default='#RRGGBB', max_length=8)),
                ('rgb', models.BooleanField()),
                ('power_consumption', models.PositiveIntegerField(null=True)),
                ('theme', models.CharField(choices=[('dark', 'dark'), ('light', 'light')], max_length=15, verbose_name='Color Theme')),
                ('use_case', models.CharField(choices=[('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')], max_length=15)),
                ('manufacturer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='Parts.manufacturer')),
            ],
            options={
                'verbose_name': 'Watercooler',
                'verbose_name_plural': 'Watercoolers',
            },
        ),
        migrations.CreateModel(
            name='ssd',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('amazon_url', models.TextField(null=True)),
                ('newegg_url', models.TextField(null=True)),
                ('partRating', models.FloatField(blank=True, null=True)),
                ('amazon_price', models.FloatField(null=True)),
                ('newegg_price', models.FloatField(null=True)),
                ('previous_price', models.FloatField(default=0.0, null=True)),
                ('current_price', models.FloatField(blank=True, null=True)),
                ('lowest_Price_Link', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('capacity', models.PositiveIntegerField()),
                ('read_speed', models.PositiveIntegerField()),
                ('write_speed', models.PositiveIntegerField()),
                ('form_factor', models.CharField(choices=[('1.0', '1.0'), ('2.5', '2.5'), ('3.5', '3.5'), ('M.2', 'M.2'), ('mSATA', 'mSATA'), ('AIC', 'AIC')], max_length=20)),
                ('height', models.FloatField()),
                ('interface', models.CharField(choices=[('SATA 3', 'SATA 3'), ('Micro-SATA', 'Micro-SATA'), ('Mini-SATA', 'Mini-SATA'), ('Mini-PCIe', 'Mini-PCIe'), ('PCIe-Express 3.0', 'PCIe-Express 3.0'), ('PCIe-Express 3.1', 'PCIe-Express 3.1'), ('PCIe-Express 4.0', 'PCIe-Express 4.0'), ('PCIe-Express 4.0', 'PCIe-Express 4.0'), ('Thunderbolt 3', 'Thunderbolt 3')], help_text='What is the connectivity type, (eg: number of pins, cable type)', max_length=20)),
                ('power_consumption', models.PositiveIntegerField(null=True)),
                ('rgb', models.BooleanField()),
                ('use_case', models.CharField(choices=[('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')], max_length=15)),
                ('manufacturer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='Parts.manufacturer')),
            ],
            options={
                'verbose_name': 'SSD',
                'verbose_name_plural': 'SSDs',
            },
        ),
        migrations.CreateModel(
            name='ram',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('amazon_url', models.TextField(null=True)),
                ('newegg_url', models.TextField(null=True)),
                ('partRating', models.FloatField(blank=True, null=True)),
                ('amazon_price', models.FloatField(null=True)),
                ('newegg_price', models.FloatField(null=True)),
                ('previous_price', models.FloatField(default=0.0, null=True)),
                ('current_price', models.FloatField(blank=True, null=True)),
                ('lowest_Price_Link', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('capacity', models.PositiveIntegerField(choices=[(4, 4), (8, 8), (16, 16), (32, 32), (64, 64), (128, 128)])),
                ('divided_capacity', models.CharField(choices=[('4x2', '4x2'), ('4x4', '4x4'), ('8x2', '8x2'), ('8x4', '8x4'), ('16x2', '16x2'), ('16x4', '16x4'), ('32x2', '32x2'), ('32x4', '32x4')], help_text='How many sticks to make up total RAM capacity', max_length=10)),
                ('channels', models.CharField(choices=[('Single', 'Single'), ('Dual', 'Dual'), ('Four', 'Four')], max_length=20)),
                ('height', models.FloatField(help_text='In mm (milimeter', verbose_name='How tall')),
                ('speed', models.IntegerField()),
                ('type', models.CharField(choices=[('DDR4', 'DDR4'), ('DDR5', 'DDR5')], max_length=5)),
                ('pins', models.PositiveIntegerField()),
                ('xmp', models.BooleanField()),
                ('color_name', models.CharField(default='Black', max_length=15)),
                ('color_hex', models.CharField(default='#RRGGBB', max_length=8)),
                ('power_consumption', models.PositiveIntegerField(null=True)),
                ('rgb', models.BooleanField()),
                ('use_case', models.CharField(choices=[('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')], max_length=15)),
                ('manufacturer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='Parts.manufacturer')),
            ],
            options={
                'verbose_name': 'RAM',
                'verbose_name_plural': 'RAMs',
            },
        ),
        migrations.CreateModel(
            name='psu',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('amazon_url', models.TextField(null=True)),
                ('newegg_url', models.TextField(null=True)),
                ('partRating', models.FloatField(blank=True, null=True)),
                ('amazon_price', models.FloatField(null=True)),
                ('newegg_price', models.FloatField(null=True)),
                ('previous_price', models.FloatField(default=0.0, null=True)),
                ('current_price', models.FloatField(blank=True, null=True)),
                ('lowest_Price_Link', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('wattage', models.PositiveIntegerField()),
                ('rating', models.CharField(choices=[('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], max_length=10)),
                ('connection', models.CharField(choices=[('Full Modular', 'Full Modular'), ('Semi Modular', 'Semi Modular'), ('None Modular', 'None Modular')], max_length=15)),
                ('size', models.IntegerField(choices=[('ATX', 'ATX'), ('Micro-ATX', 'Micro-ATX'), ('Mini-ITX', 'Mini-ITX')])),
                ('color_name', models.CharField(default='Black', max_length=15)),
                ('color_hex', models.CharField(default='#RRGGBB', max_length=8)),
                ('use_case', models.CharField(choices=[('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')], max_length=15)),
                ('manufacturer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='Parts.manufacturer')),
            ],
            options={
                'verbose_name': 'PSU',
                'verbose_name_plural': 'PSUs',
            },
        ),
        migrations.CreateModel(
            name='motherboard',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('amazon_url', models.TextField(null=True)),
                ('newegg_url', models.TextField(null=True)),
                ('partRating', models.FloatField(blank=True, null=True)),
                ('amazon_price', models.FloatField(null=True)),
                ('newegg_price', models.FloatField(null=True)),
                ('previous_price', models.FloatField(default=0.0, null=True)),
                ('current_price', models.FloatField(blank=True, null=True)),
                ('lowest_Price_Link', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('socket', models.CharField(choices=[('AM5', 'AM5'), ('AM4', 'AM4'), ('LGA 1700', 'LGA 1700'), ('LGA 1200', 'LGA 1200'), ('LGA 1151', 'LGA 1151')], max_length=15, verbose_name='Socket support')),
                ('size', models.CharField(choices=[('ATX', 'ATX'), ('Micro-ATX', 'Micro-ATX'), ('Mini-ITX', 'Mini-ITX')], max_length=15, verbose_name='Size (form factor)')),
                ('ram_slots', models.IntegerField(blank=True, choices=[(4, 4), (2, 2)], null=True, verbose_name='How many ram slots')),
                ('ddr_5_support', models.BooleanField(verbose_name='Supports DDR5 RAM')),
                ('ddr_4_support', models.BooleanField(verbose_name='Supports DDR4 RAM')),
                ('pcie_5_support', models.BooleanField(verbose_name='Supports PCIe 5')),
                ('pcie_4_support', models.BooleanField(verbose_name='Supports PCIe 4')),
                ('wifi', models.BooleanField(help_text='Does it allow WIFI connectivity (without a cable)', verbose_name='Supports Wireless Connectivity')),
                ('wifi_6_support', models.BooleanField(verbose_name='Supports WIFI 6')),
                ('lan_support', models.BooleanField(verbose_name='Supports LAN Connectivity')),
                ('fan_headers', models.PositiveIntegerField(help_text='How many fan pins on the motherboards, basically how many fans can be directly connected \n Check motherboard description on official website for more help', verbose_name='Fan Headers count')),
                ('rgb', models.BooleanField(help_text="ONLY RGB LIGHT THAT'S PART OF THE MOBO", verbose_name='RGB Lighting')),
                ('rgb_headers', models.PositiveIntegerField(help_text='How many pins onboard can be used to power RGB in other components', verbose_name='RGB Headers count')),
                ('argb_headers', models.PositiveIntegerField()),
                ('has_hdmi', models.BooleanField()),
                ('hdmi_count', models.PositiveIntegerField()),
                ('has_displayport', models.BooleanField()),
                ('displayport_count', models.PositiveIntegerField()),
                ('has_usbc', models.BooleanField(verbose_name='Supports USB-C')),
                ('usbc_count', models.PositiveIntegerField(verbose_name='USB-C ports count')),
                ('usb3point2_support', models.BooleanField(verbose_name='USB3.2 support')),
                ('usb3point2_count', models.IntegerField(null=True, verbose_name='USB3.2 count')),
                ('usb_count', models.IntegerField(null=True, verbose_name='USB count')),
                ('mdot2_SSD_slots', models.PositiveIntegerField(verbose_name='Number of M.2 slots')),
                ('sata_slots', models.PositiveIntegerField(null=True, verbose_name='Number of SATA slots')),
                ('integrated_io_sheild', models.BooleanField(help_text='Does it have a built in cover on the rear ports', verbose_name='Integrated IO sheild')),
                ('theme', models.CharField(choices=[('dark', 'dark'), ('light', 'light')], max_length=15, verbose_name='Color Theme')),
                ('use_case', models.CharField(choices=[('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')], max_length=15)),
                ('manufacturer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='Parts.manufacturer')),
            ],
            options={
                'verbose_name': 'Motherboard',
                'verbose_name_plural': 'Motherboards',
            },
        ),
        migrations.CreateModel(
            name='hdd',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('amazon_url', models.TextField(null=True)),
                ('newegg_url', models.TextField(null=True)),
                ('partRating', models.FloatField(blank=True, null=True)),
                ('amazon_price', models.FloatField(null=True)),
                ('newegg_price', models.FloatField(null=True)),
                ('previous_price', models.FloatField(default=0.0, null=True)),
                ('current_price', models.FloatField(blank=True, null=True)),
                ('lowest_Price_Link', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('capacity', models.PositiveIntegerField()),
                ('cache', models.PositiveIntegerField()),
                ('speed', models.PositiveIntegerField(choices=[(3600, 3600), (4200, 4200), (5400, 5400), (7200, 7200), (1000, 1000)])),
                ('size', models.FloatField(choices=[(1, 1), (1.8, 1.8), (2.5, 2.5), (3.5, 3.5)], null=True)),
                ('connectivity', models.CharField(help_text='What is the connectivity type, (eg: number of pins, cable type)', max_length=20)),
                ('rgb', models.BooleanField()),
                ('power_consumption', models.PositiveIntegerField(null=True)),
                ('use_case', models.CharField(choices=[('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')], max_length=15)),
                ('manufacturer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='Parts.manufacturer')),
            ],
            options={
                'verbose_name': 'HDD',
                'verbose_name_plural': 'HDDs',
            },
        ),
        migrations.CreateModel(
            name='gpu',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('amazon_url', models.TextField(null=True)),
                ('newegg_url', models.TextField(null=True)),
                ('partRating', models.FloatField(blank=True, null=True)),
                ('amazon_price', models.FloatField(null=True)),
                ('newegg_price', models.FloatField(null=True)),
                ('previous_price', models.FloatField(default=0.0, null=True)),
                ('current_price', models.FloatField(blank=True, null=True)),
                ('lowest_Price_Link', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('type', models.CharField(choices=[('Nvidia GTX', 'Nvidia GTX'), ('Nvidia RTX', 'Nvidia RTX'), ('AMD Radeon', 'AMD Radeon')], max_length=15, verbose_name='Type')),
                ('atx', models.BooleanField(blank=True, null=True)),
                ('micro_atx', models.BooleanField(blank=True, null=True)),
                ('mini_itx', models.BooleanField(blank=True, null=True)),
                ('length', models.FloatField(help_text='*in inches')),
                ('height', models.FloatField(help_text='*in inches')),
                ('width', models.FloatField(help_text='*in inches')),
                ('fan_count', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)])),
                ('vram', models.PositiveIntegerField(verbose_name='Memory (VRAM)')),
                ('gddr_type', models.CharField(choices=[('GDDR6X', 'GDDR6X'), ('GDDR6', 'GDDR6'), ('GDDR5X', 'GDDR5X'), ('GDDR5', 'GDDR5')], max_length=10, verbose_name='GDDR')),
                ('cude_cores', models.IntegerField(blank=True, null=True)),
                ('stream_processors', models.IntegerField(blank=True, null=True)),
                ('base_clock', models.IntegerField()),
                ('boost_clock', models.IntegerField()),
                ('multimonitor_support', models.BooleanField()),
                ('monitor_count', models.PositiveIntegerField()),
                ('supported_resolution', models.CharField(choices=[('1K', '1K'), ('2K', '2K'), ('4K', '4K'), ('5K', '5K'), ('8K', '8K')], max_length=5, verbose_name='Maximum supported resolutions')),
                ('pcie_5_support', models.BooleanField(verbose_name='Supports PCIe 5')),
                ('pcie_4_support', models.BooleanField(verbose_name='Supports PCIe 4')),
                ('rgb', models.BooleanField(help_text="ONLY RGB LIGHT THAT'S PART OF THE MOBO", verbose_name='RGB Lighting')),
                ('pins_num', models.PositiveIntegerField(help_text='Number of pins to power the card', verbose_name='Pins required')),
                ('has_displayport', models.BooleanField()),
                ('displayport_count', models.PositiveIntegerField()),
                ('has_hdmi', models.BooleanField()),
                ('hdmi_count', models.PositiveIntegerField()),
                ('has_usbc', models.BooleanField(verbose_name='Supports USB-C')),
                ('usbc_count', models.PositiveIntegerField(verbose_name='USB-C ports count')),
                ('theme', models.CharField(choices=[('dark', 'dark'), ('light', 'light')], max_length=15, verbose_name='Color Theme')),
                ('power_consumption', models.PositiveIntegerField(null=True)),
                ('use_case', models.CharField(choices=[('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')], max_length=15)),
                ('manufacturer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='Parts.manufacturer')),
            ],
            options={
                'verbose_name': 'GPU',
                'verbose_name_plural': 'GPUs',
            },
        ),
        migrations.CreateModel(
            name='fan',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('amazon_url', models.TextField(null=True)),
                ('newegg_url', models.TextField(null=True)),
                ('partRating', models.FloatField(blank=True, null=True)),
                ('amazon_price', models.FloatField(null=True)),
                ('newegg_price', models.FloatField(null=True)),
                ('previous_price', models.FloatField(default=0.0, null=True)),
                ('current_price', models.FloatField(blank=True, null=True)),
                ('lowest_Price_Link', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('size', models.PositiveIntegerField(null=True)),
                ('lowest_rpm', models.PositiveIntegerField(help_text='The RPM value', null=True, verbose_name='Lowest Speed')),
                ('highest_rpm', models.PositiveIntegerField(help_text='The RPM value', null=True, verbose_name='Highest Speed')),
                ('rgb', models.BooleanField()),
                ('connection', models.PositiveIntegerField(null=True, verbose_name='Num of pins')),
                ('color_name', models.CharField(default='Black', max_length=15)),
                ('color_hex', models.CharField(default='#RRGGBB', max_length=8)),
                ('theme', models.CharField(choices=[('dark', 'dark'), ('light', 'light')], max_length=15, verbose_name='Color Theme')),
                ('use_case', models.CharField(choices=[('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')], max_length=15)),
                ('manufacturer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='Parts.manufacturer')),
            ],
            options={
                'verbose_name': 'Fan',
                'verbose_name_plural': 'Fans',
            },
        ),
        migrations.CreateModel(
            name='cpu',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('amazon_url', models.TextField(null=True)),
                ('newegg_url', models.TextField(null=True)),
                ('partRating', models.FloatField(blank=True, null=True)),
                ('amazon_price', models.FloatField(null=True)),
                ('newegg_price', models.FloatField(null=True)),
                ('previous_price', models.FloatField(default=0.0, null=True)),
                ('current_price', models.FloatField(blank=True, null=True)),
                ('lowest_Price_Link', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('cores', models.PositiveIntegerField()),
                ('threads', models.PositiveIntegerField()),
                ('base_speed', models.FloatField()),
                ('boost_speed', models.FloatField()),
                ('overclockable', models.BooleanField()),
                ('socket', models.CharField(choices=[('AM4', 'AM4'), ('LGA 1700', 'LGA 1700'), ('LGA 1200', 'LGA 1200')], max_length=15)),
                ('cooler', models.BooleanField(help_text='eg: amd ryzen 3600', verbose_name='Comes with cooler')),
                ('power_consumption', models.PositiveIntegerField(null=True)),
                ('integrated_graphics', models.BooleanField(null=True)),
                ('use_case', models.CharField(choices=[('Budget', 'Budget'), ('Mid-Range', 'Mid-Range'), ('High-end', 'High-end')], max_length=15)),
                ('manufacturer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='Parts.manufacturer')),
            ],
            options={
                'verbose_name': 'CPU',
                'verbose_name_plural': 'CPUs',
            },
        ),
        migrations.CreateModel(
            name='computer',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('aircooler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Parts.aircooler')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parts.case')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parts.cpu')),
                ('gpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parts.gpu')),
                ('hdd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hdd1', to='Parts.hdd')),
                ('motherboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parts.motherboard')),
                ('psu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parts.psu')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parts.ram')),
                ('ssd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ssd1', to='Parts.ssd')),
                ('watercooler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Parts.watercooler')),
            ],
            options={
                'verbose_name': 'Computer',
                'verbose_name_plural': 'Computers',
            },
        ),
        migrations.AddField(
            model_name='case',
            name='manufacturer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='Parts.manufacturer'),
        ),
        migrations.AddField(
            model_name='aircooler',
            name='manufacturer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='Parts.manufacturer'),
        ),
    ]
