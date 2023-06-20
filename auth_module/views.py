from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from auth_module.models import UserSerializer, User
from auth_module.services import ProfileService
from common.views import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class ProfileViewSet(ViewSet):

    def __init__(self, serializer_class=UserSerializer, service=ProfileService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


@api_view(['POST'])
def login(request, *args, **kwargs):
    if request.data.get('username') is None:
        return Response(data={'message': 'username required'}, status=HTTP_400_BAD_REQUEST)
    if request.data.get('password') is None:
        return Response(data={'message': 'password required'}, status=HTTP_400_BAD_REQUEST)

    user_service = ProfileService()
    try:
        user = user_service.find_one_by({'username': request.data.get('username')})
        if user.check_password(request.data.get('password')):
            token = RefreshToken.for_user(user)
            data = {
                'userId': user.id,
                'refresh': str(token),
                'access': str(token.access_token),
                'is_superuser': user.is_superuser
            }
            if user.is_superuser is False and user.profile is not None:
                data['has_system_role'] = user.profile.has_system_role
                data['has_store_role'] = user.profile.has_store_role
            return Response(data=data, status=HTTP_200_OK)
    except User.DoesNotExist:
        return Response(data={'message': 'user not found'}, status=HTTP_404_NOT_FOUND)
