from django.contrib import admin
from .models import Shop, Donut

# Register your models here.
class DisplayShop(admin.ModelAdmin):
    """
    Configures the display of the User Admin Panel.
    """

    list_display = ("pk", "user", "name")
    search_fields = ("pk", "user__email", "name")
    readonly_fields = ("pk", "added")


class DisplayDonut(admin.ModelAdmin):
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


admin.site.register(Shop, DisplayShop)
admin.site.register(Donut, DisplayDonut)
