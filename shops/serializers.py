# DRF
from rest_framework import serializers

# Models
from authentication.serializers import UserSerializer
from .models import Shop, Donut


class ShopSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Shop
        fields = "__all__"
        # exclude = ["id"]


class DonutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donut
        fields = "__all__"
        # exclude = ["last_updated"]
