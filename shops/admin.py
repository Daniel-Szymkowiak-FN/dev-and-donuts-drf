from django.contrib import admin
from .models import Shop

# Register your models here.
class DisplayShop(admin.ModelAdmin):
    """
    Configures the display of the User Admin Panel.
    """

    list_display = ("pk", "user", "name")
    search_fields = ("pk", "user__email", "name")
    readonly_fields = ("pk", "added", "last_updated")


admin.site.register(Shop, DisplayShop)
