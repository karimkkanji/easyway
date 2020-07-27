from django.contrib import admin
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
from .models import *
# Register your models here.
class userAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'email')

admin.site.register(user,userAdmin)
admin.site.register(hotel)
admin.site.register(rent_car)
admin.site.register(activities)
admin.site.register(packages)
