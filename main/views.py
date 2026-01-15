from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import *
from products.serializers import *
from profiles.models import *
from profiles.serializers import *

@api_view(['GET'])
def index(request):
    return Response({"message": "Hi"})

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_tag_products(request):
    tag = Tag.objects.get(name=request.data.get("tag"))
    if tag == None:
        return Response({"detail": "There no user"}, status=400)
    serializer = TagSerializer(tag, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_search_products(request):
    search = request.data.get("search")
    products = Product.objects.filter(Q(name_ru__icontains=search) | Q(name_tk__icontains=search))
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_sellers_products(request):
    serializer = PhoneSerializer(data=request.data)
    if serializer.is_valid():
        phone = serializer.validated_data['phone']
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return Response({"detail": "There no user"}, status=400)
        products = Product.objects.filter(seller=user.id)
        serializer2 = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer2.data)
    return Response(serializer.errors, status=400)
