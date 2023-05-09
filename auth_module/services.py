from auth_module.models import Profile, User
from common.services import Service, Repository
from django.db import transaction


class ProfileService(Service):

    def __init__(self, repository: Repository = Repository(model=User)):
        super().__init__(repository, fields={
            'first_name': {'type': 'string', 'required': True},
            'last_name': {'type': 'string', 'required': True},
            'email': {'type': 'string', 'required': True},
            'username': {'type': 'string', 'required': True},
            'password': {'type': 'string', 'required': True},
            'profile': {'type': 'one_to_one', 'required': True}
        })

    def create(self, data: dict):
        profile = data.pop('profile')
        user = User(**data)
        with transaction.atomic():
            profile = Profile(**profile)
            profile.user = user
            user.save()
            profile.save()
        return user


class UserPermissionService(Service):
    def __init__(self, repository: Repository, fields: dict):
        super().__init__(repository, fields)
