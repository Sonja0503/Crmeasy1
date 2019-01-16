# iz djanga smo importali formu
from django import forms
# iz modela smo importali clasu ItemStorage
from .models import ItemStorage


# klasa koja nasljeduje formu iz djanga
class ItemForm(forms.ModelForm):
    class Meta:
        # objekt koji ce provuci kroz formu
        model = ItemStorage
        # tuple s imenima polja za nasu formu
        fields = ('name', 'desc', 'item_type', )
        # iz django forme zadajemo polje koja ce se nalaziti u nasoj formi
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Name',
                                                  'class': 'form-control'}),
                   'dec': forms.TextInput(attrs={'placeholder': 'Enter a desc',
                                                 'class': 'form-control'}),
                   'item_type': forms.Select(attrs={'placeholder': 'a',
                                                    'class': 'form-control'}),


}