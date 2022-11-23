from django.contrib import admin
from .models import User

# Register your models here.
class DisplayUser(admin.ModelAdmin):
    """
    Configures the display of the User Admin Panel.
    """

    list_display = ("pk", "email", "last_name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("pk", "first_name", "last_name", "email")
    readonly_fields = ("pk", "last_login")


admin.site.register(User, DisplayUser)
