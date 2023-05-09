from django.db import models
from django.db.models import Model, BooleanField, OneToOneField, CASCADE
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


# Create your models here.
class Profile(Model):
    user = OneToOneField(to=User, on_delete=CASCADE)
    has_system_role = BooleanField(null=False)
    has_store_role = BooleanField(null=False)


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'profile']
