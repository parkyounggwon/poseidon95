from django.contrib import admin
from .models import AaShip

# Register your models here.

admin.site.register(AaShip)

# @admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ('ship_name','deadweight','built','ship_date','ship_port')
    list_filter = ('deadweight','built','ship_date','ship_port')
  # search_fields = ('ship_name')
  # prepopulated_fields = {'slug':('ship_name',)}


# admin.site.register(Ship, ShipAdmin)
