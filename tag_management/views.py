from django.shortcuts import render

from common.views import ViewSet


# Create your views here.


class TagTemplateViewSet(ViewSet):

    def __init__(self, serializer_class, service, **kwargs):
        super().__init__(serializer_class, service, **kwargs)
