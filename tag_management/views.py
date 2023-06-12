from common.views import ViewSet
from tag_management.models import TagTemplateSerializer, DeviceSerializer, GateWaySerializer
from tag_management.services import TagTemplateService, DeviceService, GateWayService
from django.urls import path

# Create your views here.


class TagTemplateViewSet(ViewSet):

    def __init__(self, serializer_class=TagTemplateSerializer, service=TagTemplateService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


class DeviceViewSet(ViewSet):

    def __init__(self, serializer_class=DeviceSerializer, service=DeviceService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


class GateWayViewSet(ViewSet):

    def __init__(self, serializer_class=GateWaySerializer, service=GateWayService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


gateways, gateway = GateWayViewSet.get_urls()
tag_templates, tag_template = TagTemplateViewSet.get_urls()
devices, device = DeviceViewSet.get_urls()
urlpatterns = [
    path('tag_templates', tag_templates),
    path('tag_templates/<int:pk>', tag_template),
    path('gateways/<int:pk>', gateway),
    path('gateways', gateways),
    path('devices', devices),
    path('devices/<int:pk>', device)
]
