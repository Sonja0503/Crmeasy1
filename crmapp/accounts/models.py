# iz djanga smo ucitali file model
from django.db import models
# iz djanga smo ucitali klasu User
from django.contrib.auth.models import User
# iz djanga smo ucitali metodu reverse
from django.core.urlresolvers import reverse
# ubacujemo uuid
from shortuuidfield import ShortUUIDField


# klasa Account nasljeduje klasu Model
class Account(models.Model):
    # polje unikatni id
    uuid = ShortUUIDField(unique=True)
    # polje ime, dozvoljena duzina 80 znakova
    name = models.CharField(max_length=80)
    # polje description, nije obavezno za ispuniti
    desc = models.TextField(blank=True)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    phone = models.CharField(max_length=20)
    # polje owner veze se na usera,uzima id iz usera
    owner = models.ForeignKey(User)
    # polje za kreiranje datuma
    created_on = models.DateField(auto_now_add=True)

    # Obicna klasa definira ponasanje objekta,Meta klasa definira ponasanje klase
    class Meta:
        # ime DB tablice gdje su spremljeni podatci iz klase Account
        verbose_name_plural = 'accounts'

    # Instanc metoda koja uvijek vraca string zapis , self oznacava objekt na kojeg se instanca vrsi
    def __str__(self):
        # vraca owner i name polje iz klase Account
        return "{} {}".format(self.owner, self.name)

    # Instanc metoda koja daje uredeni URL zapis za neki objekt
    def get_absolute_url(self):
        return reverse('account_detail', args=(self.uuid,))

    def get_update_url(self):
        return reverse('account_update', args=(self.uuid,))

    def get_delete_url(self):
        return reverse('account_delete', args=(self.uuid,))
