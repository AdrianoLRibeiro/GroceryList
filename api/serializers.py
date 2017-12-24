from rest_framework import serializers
from .models import Department, Product, Product_Pss, Brand, Item, Market, Purchase
from django.shortcuts import get_object_or_404

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('description', )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('description', )

class ProductSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField(many=False)
    brand = serializers.StringRelatedField(many=False)
    class Meta:
        model = Product
        fields = ('description', 'brand', 'department')

class ProductPssSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=False)
    class Meta:
        model = Product_Pss
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=False)
    class Meta:
        model = Purchase
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=False)
    purchase = serializers.StringRelatedField(many=False)
    class Meta:
        model = Item
        fields = '__all__'

class MarketSerializer(serializers.ModelSerializer):
    purchase = serializers.StringRelatedField(many=False)
    class Meta:
        model = Market
        fields = '__all__'
