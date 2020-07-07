from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import *
# Register your models here.
admin.site.register(customers)
admin.site.register(hotel)
admin.site.register(rent_car)
admin.site.register(activities)

class hotelAdmin(admin.ModelAdmin):
	  formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }

class rent_carAdmin(admin.ModelAdmin):
	  formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }

class activitiesAdmin(admin.ModelAdmin):
	  formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }
