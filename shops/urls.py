# Django
from django.urls import path

# API Views
from shops.api import ShopAPIView

urlpatterns = [
    path("shop/", ShopAPIView.as_view(), name="shop"),
]
