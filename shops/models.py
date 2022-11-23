# Django
from django.db import models
from django.utils.translation import gettext as _


class Shop(models.Model):
    user = models.ForeignKey(
        "authentication.User",
        related_name="shop_user",
        on_delete=models.RESTRICT,
    )
    name = models.CharField(max_length=255, blank=True, default="")
    added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + " - " + self.name

    def owner_display(self):
        try:
            return self.organisation.owner.email
        except Exception:
            return "-"

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Donut(models.Model):
    FROSTING__NONE = "none"
    FROSTING__VANILLA = "vanilla"
    FROSTING__CHOCOLATE = "chocolate"
    FROSTING__STRAWBERRY = "strawberry"
    FROSTING = [
        (FROSTING__NONE, _("none")),
        (FROSTING__VANILLA, _("vanilla")),
        (FROSTING__CHOCOLATE, _("chocolate")),
        (FROSTING__STRAWBERRY, _("strawberry")),
    ]
    shop = models.ForeignKey(
        "shops.Shop",
        related_name="donut_shop",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255, blank=True, default="")
    frosting = models.CharField(max_length=255, choices=FROSTING, default=FROSTING__NONE)
