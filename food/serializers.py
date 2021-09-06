from rest_framework import serializers

from .models import Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'type', 'description', 'customer', 'created_at')
        model = Dish