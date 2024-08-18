# faq/serializers.py

from rest_framework import serializers
from .models import StoreInfo

class StoreInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreInfo
        fields = ['id', 'store_name', 'store_hours', 'menu_prices', 'store_image']