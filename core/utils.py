from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import NotFound
from django.conf import settings
import jwt

def Authentication(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    return payload

def CheckAddress(Address, address_id, user):
    try:
        address = Address.objects.get(id=address_id, author=user)
    except:
        raise NotFound('An address with this id does not exist.')

    return address
