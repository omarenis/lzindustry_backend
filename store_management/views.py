from django.urls import path

from common.repositories import Repository
from common.services import Service
from common.views import ViewSet
from store_management.models import StoreSerializer, Store

STORE_FIELDS = {
    'image': {'type': 'file', 'required': True},
    'is_active': {'type': 'boolean', 'required': False, 'default': True},
    'manager': {'type': 'foreign_key', 'required': True},
    'name': {'type': 'text', 'required': True},
    'localisation': {'type': 'foreign_key', 'required': True},
    'address': {'type': 'text', 'required': True}
}


# Create your views here.
class StoreViewSet(ViewSet):

    def __init__(self, serializer_class=StoreSerializer, service=Service(repository=Repository(model=Store),
                                                                         fields=STORE_FIELDS), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


store, stores = StoreViewSet.get_urls()

urlpatterns = [
    path('stores', stores),
    path('stores/<int:pk>', store)
]
