# DRF
from rest_framework import serializers

# Models
from authentication.serializers import UserSerializer
from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Shop
        fields = "__all__"
