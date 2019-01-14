# iz djanga ubacujemo admin
from django.contrib import admin
# iz modela iz accounts foldera ubacujemo classu Account
from .models import Account


# classa koja je nasljedila ModelAdmin klasu
class AccountAdmin(admin.ModelAdmin):
    # tuple
    list_display = ('name', 'uuid', 'city', 'owner')


# povlaci informacije iz Account klase koje prikazuje kroz tuple iz AcountAdmin klase
admin.site.register(Account, AccountAdmin)
