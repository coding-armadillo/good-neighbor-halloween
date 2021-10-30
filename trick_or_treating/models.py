from django.contrib import admin
from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=200, unique=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    label = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.label or self.name


class AddressAdmin(admin.ModelAdmin):
    exclude = (
        "latitude",
        "longitude",
    )
