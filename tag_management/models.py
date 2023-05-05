from django.db.models import Model, FileField, FloatField, TextField, ImageField, BigIntegerField, ForeignKey,\
    SET_NULL, CharField, BooleanField


class TagTemplate(Model):
    image = ImageField(null=False)
    number_tags = BigIntegerField(default=0)


class Tag(Model):
    product = ForeignKey(to='stock_management.Product', on_delete=SET_NULL)
    template_tag = ForeignKey(to='TagTemplate', on_delete=SET_NULL)
    qr_code = FileField(upload_to='qr_codes')
    battery = FloatField()
    mac_address = TextField()
    price = FloatField()
    template = ImageField(upload_to='tag_templates')


class GateWay(Model):
    store = ForeignKey(to='store_management.Store', on_delete=SET_NULL, null=True)
    mac_name = CharField(max_length=255)
    mac_address = CharField(max_length=255)
    is_online = BooleanField(null=False, default=False)
    model = TextField(null=False)
    wifi_firmware_version = CharField()
    bluetooth_firmware_version = CharField()
