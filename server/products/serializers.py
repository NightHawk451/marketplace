# server/products/serializers.py

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'created_dt', 'updated_ts', 'uploaded_by')