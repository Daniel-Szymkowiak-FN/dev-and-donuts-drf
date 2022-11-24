# DRF
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Models
from .models import Shop
from .serializers import ShopSerializer


class ShopAPIView(APIView):
    allowed_methods = ["GET"]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """List all shops of one user"""
        shop_queryset = Shop.objects.filter(user=self.request.user)
        serializer = ShopSerializer(shop_queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
