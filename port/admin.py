from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import AaPort

# Register your models here.
admin.site.register(AaPort)

class AaPortAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }

