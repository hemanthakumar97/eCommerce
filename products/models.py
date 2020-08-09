from django.db import models


# class TechnicalDeatails(models.Model):

class Seller(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    asin = models.CharField(max_length=20)
    bsr = models.CharField(max_length=255)
    doa = models.DateField()

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.category

class Mobile(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=255, default="Android", blank=True, null=True)
    rom = models.CharField(max_length=5, blank=True, null=True)
    ram = models.CharField(max_length=5, blank=True, null=True)
    processor = models.CharField(max_length=50, blank=True, null=True)
    battery = models.CharField(max_length=50, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    item_dim = models.CharField(max_length=255, blank=True, null=True)
    item_weight = models.CharField(max_length=255, blank=True, null=True)
    item_model_no = models.CharField(max_length=255, blank=True, null=True)
    wireless_com_tech = models.CharField(max_length=255, blank=True, null=True)
    connectivity_tech = models.CharField(max_length=255, blank=True, null=True)
    speacial_features = models.CharField(max_length=255, default="Included")
    display_tech = models.CharField(max_length=255, blank=True, null=True)
    camera = models.CharField(max_length=255, blank=True, null=True)
    form_factor = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    battery_rating = models.CharField(max_length=255, blank=True, null=True)
    whats_in_box = models.CharField(max_length=255, blank=True, null=True)
    warrenty = models.CharField(max_length=255, default="1 Year", blank=True, null=True)
    
    def __str__(self):
        return self.title


class Laptop(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    series = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    item_height = models.CharField(max_length=255, blank=True, null=True)
    item_width = models.CharField(max_length=255, blank=True, null=True)
    item_weight = models.CharField(max_length=255, blank=True, null=True)
    screen_size = models.CharField(max_length=255, blank=True, null=True)
    maximum_display_res = models.CharField(max_length=255, blank=True, null=True)
    product_dimension = models.CharField(max_length=255, blank=True, null=True)
    batteries = models.CharField(max_length=255, default="Included")
    item_model_no = models.CharField(max_length=255, blank=True, null=True)
    processor_brand = models.CharField(max_length=255, blank=True, null=True)
    processor_type = models.CharField(max_length=255, blank=True, null=True)
    ram_size = models.CharField(max_length=255, blank=True, null=True)
    memory_technology = models.CharField(max_length=255, blank=True, null=True)
    hdd_technology = models.CharField(max_length=255, blank=True, null=True)
    hdd_size = models.CharField(max_length=255, blank=True, null=True)
    ssd_size = models.CharField(max_length=255, blank=True, null=True)
    speaker_discription = models.CharField(max_length=255, blank=True, null=True)
    graphic_processor = models.CharField(max_length=255, blank=True, null=True)
    graphic_card_size = models.CharField(max_length=255, blank=True, null=True)
    connectivity_type = models.CharField(max_length=255, blank=True, null=True)
    no_of_usb2_ports = models.CharField(max_length=255, blank=True, null=True)
    no_of_usb3_ports = models.CharField(max_length=255, blank=True, null=True)
    no_of_hdmi_ports = models.CharField(max_length=255, blank=True, null=True)
    no_of_audio_out_ports = models.CharField(max_length=255, blank=True, null=True)
    no_of_microphone_ports = models.CharField(max_length=255, blank=True, null=True)
    power_source = models.CharField(max_length=255, default="Battery Powered", blank=True, null=True)
    os = models.CharField(max_length=255, default="Windows 10 Home", blank=True, null=True)
    avg_battery_standby = models.CharField(max_length=255, blank=True, null=True)
    avg_battery_life = models.CharField(max_length=255, blank=True, null=True)
    lithium_energy_battery_content = models.CharField(max_length=255, blank=True, null=True)
    included_components = models.CharField(max_length=255, default="Laptop, Battery, AC Adapter, User Guide, Manuals", blank=True, null=True)
    warrenty = models.CharField(max_length=255, default="1 Year", blank=True, null=True)
    
    def __str__(self):
        return self.title

class Sensor(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    item_weight = models.CharField(max_length=50, blank=True, null=True)
    product_dim = models.CharField(max_length=50, blank=True, null=True)
    part_no = models.CharField(max_length=50, blank=True, null=True)
    battery = models.CharField(max_length=50, blank=True, null=True)
    audio_focus = models.CharField(max_length=50, blank=True, null=True)
    programmable_btn = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    hardware_interface = models.CharField(max_length=50, blank=True, null=True)
    voltage = models.CharField(max_length=50, blank=True, null=True)
    color_screen = models.CharField(max_length=50, blank=True, null=True)
    screen_size = models.CharField(max_length=50, blank=True, null=True)
    compabitable_devises = models.CharField(max_length=50, blank=True, null=True)
    property_1 = models.TextField(blank=True, null=True)
    property_2 = models.TextField(blank=True, null=True)
    property_3 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class ElectronicComponent(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    item_weight = models.CharField(max_length=50, blank=True, null=True)
    product_dim = models.CharField(max_length=50, blank=True, null=True)
    part_no = models.CharField(max_length=50, blank=True, null=True)
    battery = models.CharField(max_length=50, blank=True, null=True)
    audi_focus = models.CharField(max_length=50, blank=True, null=True)
    programmable_btn = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    hardware_interface = models.CharField(max_length=50, blank=True, null=True)
    voltage = models.CharField(max_length=50, blank=True, null=True)
    color_screen = models.CharField(max_length=50, blank=True, null=True)
    screen_size = models.CharField(max_length=50, blank=True, null=True)
    compabitable_devises = models.CharField(max_length=50, blank=True, null=True)
    property_1 = models.TextField(blank=True, null=True)
    property_2 = models.TextField(blank=True, null=True)
    property_3 = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    main_image = models.ImageField(upload_to='producs/', blank=True, null=True)
    image_1 = models.ImageField(upload_to='producs/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='producs/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='producs/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='producs/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='producs/', blank=True, null=True)
    image_6 = models.ImageField(upload_to='producs/', blank=True, null=True)
    image_7 = models.ImageField(upload_to='producs/', blank=True, null=True)
    image_8 = models.ImageField(upload_to='producs/', blank=True, null=True)
    mrp = models.IntegerField()
    deal_price = models.IntegerField()
    rating = models.IntegerField()
    is_nocost = models.BooleanField(default=False)
    feature_1 = models.CharField(max_length=255, blank=True, null=True)
    feature_2 = models.CharField(max_length=255, blank=True, null=True)
    feature_3 = models.CharField(max_length=255, blank=True, null=True)
    feature_4 = models.CharField(max_length=255, blank=True, null=True)
    feature_5 = models.CharField(max_length=255, blank=True, null=True)
    feature_6 = models.CharField(max_length=255, blank=True, null=True)
    feature_7 = models.CharField(max_length=255, blank=True, null=True)
    feature_8 = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    pro_banner_1 = models.ImageField(upload_to='producs/', blank=True, null=True)
    pro_banner_2 = models.ImageField(upload_to='producs/', blank=True, null=True)
    pro_banner_3 = models.ImageField(upload_to='producs/', blank=True, null=True)
    pro_banner_4 = models.ImageField(upload_to='producs/', blank=True, null=True)
    pro_banner_5 = models.ImageField(upload_to='producs/', blank=True, null=True)
    pro_banner_6 = models.ImageField(upload_to='producs/', blank=True, null=True)
    pro_banner_7 = models.ImageField(upload_to='producs/', blank=True, null=True)
    pro_banner_8 = models.ImageField(upload_to='producs/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, blank=True, null=True)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, blank=True, null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, blank=True, null=True)
    electronic_component = models.ForeignKey(ElectronicComponent, on_delete=models.CASCADE, blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.title

