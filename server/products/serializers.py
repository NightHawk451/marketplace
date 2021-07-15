# server/products/serializers.py

from rest_framework import serializers
from .models import Product, Images


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("image",)


class ProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'created_dt', 'updated_ts', 'uploaded_by')