# Iz Djanga importaj modele
from django.db import models

# Klasa moja nasljeduje model iz djanga
class ItemStorage(models.Model):
    # Varijabla koja je konstanta(ne moze joj se mjenjati vrijednost)
    ITEM_LIST = (
        (1, 'Rings'),
        (2, 'Necklace'),
        (3, 'Other'),
    )
    # Ime max duzina 20
    name = models.CharField(max_length=20)
    # Opis max duzine 100
    desc = models.TextField(max_length=100)
    # Polje koje daje izlistanje (u ovom slucaju gore navedenu konstantu)
    item_type = models.PositiveSmallIntegerField(choices=ITEM_LIST)
    # Dodaje datum kada je kreiran novi item
    created_on = models.DateField(auto_now_add=True)

    # meta definira podatak o klasi,ne utjece na radi klase
    class Meta:
        # ime klase (da nije dana ova varijabla,ime bi bilo item storage)
        verbose_name_plural = 'storage'
        # slozi od Z-A (da nema (-) bilo bi od A-Z)
        ordering = ('-name', )
        # ne dozvoljava kreiranje itema s istim imenom i type-om
        unique_together = ('name', 'item_type')

    # metoda koja vraca stringove
    def __unicode__(self):
        return u'{} {}'.format(self.name, self.item_type)

    @models.permalink
    def get_absolute_url(self):
        return 'item_detail', [self.id]

    @models.permalink
    def get_update_url(self):
        return 'item_update', [self.id]

    @models.permalink
    def get_delete_url(self):
        return 'item_delete', [self.id]


