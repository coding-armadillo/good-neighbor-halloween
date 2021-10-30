from django.contrib import admin

from . import models

admin.site.register(models.Address, models.AddressAdmin)

admin.site.site_header = "good-neighbor-halloween administration"
