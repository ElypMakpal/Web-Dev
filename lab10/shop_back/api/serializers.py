from   rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def validate(self, data):
        if data.get('count') == 0 or data.get('is_active') is False:
            raise serializers.ValidationError(
                "Error"
            )
        return data