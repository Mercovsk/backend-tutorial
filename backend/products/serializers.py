from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    bulk_order = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title', 'content', 'price', 'sale_price', 'bulk_order'
        ]

    def get_bulk_order(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.bulk_order_price()