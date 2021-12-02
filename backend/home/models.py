from django.conf import settings
from django.db import models


class Auto(models.Model):
    "Generated Model"
    brand = models.CharField(
        max_length=256,
    )
    fourwheeldrive = models.BooleanField(
        null=True,
        blank=True,
    )
