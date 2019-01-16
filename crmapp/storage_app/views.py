from django.views.generic import ListView
from .models import ItemStorage
from .forms import ItemForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# klasa koja nasljeduje klasu iz djanga
class ItemList(ListView):
    # ubacujemo nas model ItemStorage
    model = ItemStorage
    # html koji se veze na ovu listu
    template_name = 'item_storage/item_list.html'
    # ime koje cemo ubaciti u for petlju
    context_object_name = 'storage'


# metoda koja zahtjeva request(GET ili POST)
def item_new(request):
    # ako je item kriran
    if request.POST:
        # u formu ubacujemo kreirani item
        form = ItemForm(request.POST)
        # ako je forma zadovoljena/ispravna
        if form.is_valid():
            # snimimo formu
            form.save()
            # prebaci na item list (name URL-a od liste)
            redirect_url = reverse('item_list')
            # djangova klasa koja zove nas redirect_url(item list)
            return HttpResponseRedirect(redirect_url)
    # ako item nije uspjesno kreiran
    else:
        # ponovi formu za kreiranje novog itema
        form = ItemForm()
    # dictionary-pomocu kljuca 'form' ubacujemo ga u html
    variables = {'form': form, }
    # html koji vezemo za ovu formu
    template = 'item_storage/storage_item_form.html'
    # vraca kombinirani predlozak POST-a,template-a i dictionary-a
    return render(request, template, variables)


# metoda koja zahtjeva request,id ostaje prazan i automatski se uzima vec definirani id
def item_cru(request, id=None):
    # iz nase klase ItemStorege dohvati id od objekta
    item = ItemStorage.objects.get(id=id)
    # ako je zahtjev kreiran
    if request.POST:
        # u formu ubaci kreirani item pod id kiji smo ranije dohvatili
        form = ItemForm(request.POST, instance=item)
        # ako je forma validna
        if form.is_valid():
            # snimi formu
            form.save()
            # prebaci na item list
            redirect_url = reverse('item_list')
            # vrati item_list
            return HttpResponseRedirect(redirect_url)
    # ako zahtijev nije kreiran
    else:
        # u formu ubaci dohvaceni id bez promjene
        form = ItemForm(instance=item)
    # dictionary- pomocu kljuca 'form' i 'item' povezujemo ga u template-u
    variables = {'form': form,
                 'item': item}
    # HTML s kojim povezujemo nasu edit formu
    template = 'item_storage/storage_item_form.html'
    # vraca kombinirani predlozak POST-a,template-a i dictionary-a
    return render(request, template, variables)


# klasa koja nasljeduje djangovu klasu
class ItemDelete(DeleteView):
    # u model ubacujemo nas model
    model = ItemStorage
    # ime template-a koji povezujemo s nasom klasom
    template_name = 'object_confirm_delete.html'

    # djangova metoda pomocu koje povezujemo neki univerzalni template
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Item'})
        return kwargs

    # matoda koja dohvaca objekt po pk
    def get_object(self, queryset=None):
        obj = super(ItemDelete, self).get_object()
        return obj
    # metoda koja prebacuje na URL 'item_list'
    def get_success_url(self):
        return reverse('item_list')

    # delete ce se dogoditi samo ako je user logiran
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemDelete, self).dispatch(*args, **kwargs)












