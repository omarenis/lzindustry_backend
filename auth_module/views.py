from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
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
            return Response(data={

            })
    except User.DoesNotExist:
        return Response(data={'message': 'user not found'}, status=HTTP_404_NOT_FOUND)
