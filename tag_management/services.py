from common.repositories import Repository
from common.services import Service
from tag_management.models import Device, GateWay, TagTemplate

DEVICE_FIELDS = {
    'product': {'type': 'foreign_key', 'required': True},
    'promo': {'type': 'foreign_key', 'required': True},
    'qr_code': {'type': 'file', 'required': True},
    'battery': {'type': 'foreign_key', 'required': True},
    'mac_address': {'type': 'text', 'required': True},
    'price': {'type': 'float', 'required': True},
    'tag_template': {'type': 'foreign_key', 'required': True},
    'store': {'type': 'foreign_key', 'required': True},
    'tva': {'type': 'float', 'required': True},
    'current_quantity': {'type': 'float', 'required': True}
}


TAG_TEMPLATE_FIELDS = {
    'image': {'type': 'file', 'required': True},
    'number_tags': {'type': 'int', 'required': False}
}

GATEWAY_FIELDS = {
    'store': {'type': 'foreign_key', 'required': True},
    'mac_name': {'type': 'text', 'required': True, 'max_length': 255},

    'mac_address': {'type': 'text', 'required': True, 'max_length': 255},
    'is_online': {'type': 'boolean', 'required': True},
    'model': {'type': 'text', 'required': True, 'max_length': 255},
    'wifi_firmware_version': {'type': 'text', 'required': True, 'max_length': 255},
    'bluetooth_firmware_version': {'type': 'text', 'required': True, 'max_length': 255},
}


class DeviceService(Service):
    def __init__(self):
        super().__init__(repository=Repository(model=Device), fields=DEVICE_FIELDS)


class GateWayService(Service):

    def __init__(self):
        super().__init__(repository=Repository(model=GateWay), fields=GATEWAY_FIELDS)


class TagTemplateService(Service):
    def __init__(self):
        super().__init__(repository=Repository(model=TagTemplate), fields=TAG_TEMPLATE_FIELDS)
