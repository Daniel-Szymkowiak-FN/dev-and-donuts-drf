# Django
from django.db import models


class Shop(models.Model):
    user = models.ForeignKey(
        "authentication.User",
        related_name="shop_user",
        on_delete=models.RESTRICT,
    )
    name = models.CharField(max_length=255, blank=True, default="")
    added = models.DateTimeField(auto_now_add=True)

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
