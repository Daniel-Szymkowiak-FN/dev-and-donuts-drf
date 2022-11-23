# Django
from django.urls import path

# API Views
from shops.api import ShopAPIView, DonutAPIView

urlpatterns = [
    path("shop/", ShopAPIView.as_view(), name="shop"),
    path("donut/", DonutAPIView.as_view(), name="donut"),
]
