# iz djanga importamo admina
from django.contrib import admin
# iz modela importamo klasu
from .models import ItemStorage


# klasa koja nasljeduje ModelAdmin iz admina
class ItemAdmin(admin.ModelAdmin):
    # tuple koji nam prikazuje imena u tablici u adminu
    list_display = ('id', 'name', 'desc', 'item_type')

# u postijecu admin django tablicu ubacujemo podatke iz nasih klasa
admin.site.register(ItemStorage, ItemAdmin)
