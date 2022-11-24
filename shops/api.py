# DRF
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Models
from .models import Shop, Donut
from .serializers import ShopSerializer, DonutSerializer


class ShopAPIView(APIView):
    allowed_methods = ["GET"]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """List all shops of one user"""
        shop_queryset = Shop.objects.filter(user=self.request.user)
        serializer = ShopSerializer(shop_queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class DonutAPIView(APIView):
    allowed_methods = ["GET", "POST"]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """List all donuts of a user"""
        donut_queryset = Donut.objects.filter(name__startswith="Stra")
        serializer = DonutSerializer(donut_queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        """Create a donut"""
        serializer = DonutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
