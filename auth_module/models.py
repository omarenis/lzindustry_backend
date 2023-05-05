from django.db import models
from django.db.models import Model, BooleanField, OneToOneField, CASCADE
from django.contrib.auth.models import User


# Create your models here.
class Profile(Model):
    user = OneToOneField(to=User, on_delete=CASCADE)
    has_system_role = BooleanField(null=False)
    has_store_role = BooleanField(null=False)
