from django.shortcuts import render

from common.views import ViewSet
from tag_management.models import TagTemplateSerializer, DeviceSerializer, GateWaySerializer
from tag_management.services import TagTemplateService, DeviceService, GateWayService

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
