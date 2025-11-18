from django.contrib import admin

from .models import Owner, Pet, CardiacData

admin.site.register(Owner)
admin.site.register(Pet)
admin.site.register(CardiacData)