from rest_framework import serializers
from .models import *

class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12)
