from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.exceptions import NotFound
from core.utils import CheckAddress, Authentication
from users.models import User
from django.db.models import Q
from .serializers import AddressSerializer
from .models import Address

def query(address, request):
    search = request.query_params.get('search', None)
    if search is not None:
        address = address.filter(Q(fullname__contains=search)|Q(company__contains=search)|Q(email__contains=search)|Q(number__contains=search)|Q(street__contains=search)|Q(area__contains=search)|Q(city__contains=search)|Q(state__contains=search)|Q(country__contains=search)|Q(zip__contains=search)|Q(fax__contains=search)|Q(website__contains=search)|Q(coutrycode__contains=search))

    return address


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
        return Response({'message':'address successfully deleted!'})



class AddressesView(APIView):
    def get(self, request):
        payload = Authentication(request)
        user = User.objects.get(id=payload['id'])
        page_number = request.query_params.get('page', 1)
        page_size = request.query_params.get('size', 10)
        address = Address.objects.filter(author=user)
        address = query(address, request)
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

    def delete(self, request):
        payload = Authentication(request)
        user = User.objects.get(id=payload['id'])

        address = Address.objects.filter(author=user)
        address = query(address, request)

        address.delete()
        return Response({'message':'multiple addresses successfully deleted!'})


class PostalView(APIView):
    def get(self, request):
        payload = Authentication(request)
        user = User.objects.get(id=payload['id'])
        zips = Address.objects.filter(author=user).values_list('zip', flat=True).distinct()

        return Response({"zips":zips})
