"""
This file contains the classes that are coded in the live demo


Development:
1. Model - Donut
2. Serializer - Donut
3. API Endpoint - Donut
4. URLs
5. Admin.py

"""

# 1 ----------------

class Donut(models.Model):
    shop = models.ForeignKey(
        "shops.Shop",
        related_name="donut_shop",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255, blank=True, default="")
    frosting = models.CharField(
        max_length=255,
        choices=[
            ("none", "-"),
            ("vanilla", "Vanille"),
            ("chocolate", "Schokolade"),
            ("strawberry", "Erdbeere"),
        ],
        default="none",
    )
    last_updated = models.DateTimeField(auto_now=True)

# 2 ----------------

# import Donut

class DonutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donut
        fields = "__all__"
        # exclude = ["last_updated"]

3 ----------------

# import Donut
# import DonutSerializer

class DonutAPIView(APIView):
    allowed_methods = ["GET", "POST"]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """List all donuts of a user"""
        donut_queryset = Donut.objects.filter(shop__user=self.request.user)
        serializer = DonutSerializer(donut_queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        """Create a donut"""
        serializer = DonutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

# 4 ----------------

# import DonutAPIView

path("donut/", DonutAPIView.as_view(), name="donut"),

5 ----------------

# import Donut

# class DisplayDonut(admin.ModelAdmin):
    """
    Configures the display of the User Admin Panel.
    """

    list_display = ("pk", "shop", "name", "user_email")
    search_fields = ("pk", "shop__user__email", "name")
    readonly_fields = ("pk", "last_updated")

    def user_email(self, obj):
        try:
            return obj.shop.user.email
        except:
            return "-"

admin.site.register(Donut, DisplayDonut)

# --------------------------
