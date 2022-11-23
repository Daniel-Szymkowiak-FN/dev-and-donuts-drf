# DRF
from rest_framework import serializers

# Models
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "date_joined", "last_login"]
