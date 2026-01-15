from rest_framework import serializers
from .models import *
from profiles.models import *

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = ['image', 'order']

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    seller = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'article', 'price', 'description', 'phone', 'seller', 'tags', 'images']
    
    def get_name(self, obj):
        request = self.context.get("request")
        language = request.LANGUAGE_CODE
        names = {
            'ru' : obj.name_ru,
            'tk' : obj.name_tk,
        }

        return names[language]
    
    def get_description(self, obj):
        request = self.context.get("request")
        language = request.LANGUAGE_CODE
        descriptions = {
            'ru' : obj.description_ru,
            'tk' : obj.description_tk,
        }

        return descriptions[language]
    
    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]
    
    def get_seller(self, obj):
        return obj.seller.username
    
    def get_images(self, obj):
        request = self.context.get("request")
        return [request.build_absolute_uri(img.image.url) for img in obj.images.all()]

class TagSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'products']