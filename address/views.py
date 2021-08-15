from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.exceptions import NotFound
from core.utils import CheckAddress, Authentication
from users.models import User
from .serializers import AddressSerializer
from .models import Address


# Create your views here.
class AddressView(APIView):
    def get(self, request, address_id):
        payload = Authentication(request)
        user = User.objects.get(id=payload['id'])
        address = CheckAddress(Address, address_id, user)

        serializer = AddressSerializer(address)
        return Response(serializer.data)


    def put(self, request, address_id):
        payload = Authentication(request)
        user = User.objects.get(id=payload['id'])
        address = CheckAddress(Address, address_id, user)

        serializer = AddressSerializer(
        address,
        data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, address_id):
        payload = Authentication(request)
        user = User.objects.get(id=payload['id'])
        address = CheckAddress(Address, address_id, user)

        address.delete()
        return Response('address succsesfully deleted!')



class AddressesView(APIView):
    def get(self, request):
        payload = Authentication(request)
        user = User.objects.get(id=payload['id'])
        page_number = request.query_params.get('page', 1)
        page_size = request.query_params.get('size', 10)
        address = Address.objects.filter(author=user)
        paginator = Paginator(address, page_size)
        try:
            page = paginator.page(page_number)
        except:
            raise NotFound("empty page")

        serializer = AddressSerializer(page, many=True, context={'request':request})
        return Response({"total pages":str(paginator.num_pages),"page number":page_number,"page size":page_size,"result":serializer.data})

    def post(self, request):
        payload = Authentication(request)
        user = User.objects.get(id=payload['id'])

        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=user)
        return Response(serializer.data)

class PostalView(APIView):
    def get(self, request):
        payload = Authentication(request)
        user = User.objects.get(id=payload['id'])
        zips = Address.objects.filter(author=user).values_list('zip', flat=True).distinct()

        return Response(zips)
