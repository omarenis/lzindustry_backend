from django.db import models
from django.db.models import Model, BooleanField, OneToOneField, CASCADE, CharField
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


# Create your models here.
class Profile(Model):
    user = OneToOneField(to=User, on_delete=CASCADE)
    has_system_role = BooleanField(null=False)
    has_store_role = BooleanField(null=False)
    telephone = CharField(max_length=255, null=False)


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'last_login', 'date_joined', 'id', 'profile']
