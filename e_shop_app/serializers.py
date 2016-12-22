from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Модельный cериализатор категории товара"""

    class Meta:
        model = Category

        fields = '__all__'
