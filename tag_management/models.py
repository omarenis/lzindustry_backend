from django.db.models import Model, FileField, FloatField, TextField, ImageField, BigIntegerField, ForeignKey, \
    SET_NULL, CharField, BooleanField, CASCADE

from rest_framework.serializers import ModelSerializer


class TagTemplate(Model):
    image = ImageField(null=False)
    number_tags = BigIntegerField(default=0)


class Device(Model):
    product = ForeignKey(to='stock_management.Product', on_delete=SET_NULL, null=True)
    promo = ForeignKey(to='stock_management.Promo', on_delete=SET_NULL, null=True)
    qr_code = FileField(upload_to='qr_codes')
    battery = FloatField()
    mac_address = TextField()
    price = FloatField()
    tag_template = ImageField(upload_to='tag_templates')
    store = ForeignKey(to='store_management.Store', null=False, on_delete=CASCADE)
    tva = FloatField(null=False, default=0.19)
    current_quantity = FloatField(null=False, default=1)

    def save(self, **kwargs):
        super().save()
        self.product.current_quantity += self.current_quantity
        self.product.save()
        return self


class GateWay(Model):
    store = ForeignKey(to='store_management.Store', on_delete=SET_NULL, null=True)
    mac_name = CharField(max_length=255)
    mac_address = CharField(max_length=255)
    is_online = BooleanField(null=False, default=False)
    model = TextField(null=False)
    wifi_firmware_version = CharField(max_length=255)
    bluetooth_firmware_version = CharField(max_length=255)


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class GateWaySerializer(ModelSerializer):
    class Meta:
        model = GateWay
        fields = '__all__'


class TagTemplateSerializer(ModelSerializer):
    class Meta:
        model = TagTemplate
        fields = '__all__'
