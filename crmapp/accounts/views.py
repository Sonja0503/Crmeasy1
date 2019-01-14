from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import AccountForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Account
from django.shortcuts import get_object_or_404
from crmapp.contacts.models import Contact

# Klasa koja nasljeduje ListView klasu
class AccountList(ListView):
    # varijabli model dajemo vrijednosti klase Account koju smo importali iz models.py
    model = Account
    # paginaciju ogranicavamo na 3, znaci da ce se 3 acounta prikazivati na stranici
    paginate_by = 3
    # html koji vezemo
    template_name = 'accounts/account_list.html'
    # ime liste , u html-u ga provlacimo kroz for petlju
    context_object_name = 'accounts'

    # Instanc metoda koja daje zbirku podataka iz DB,i stvara filtere na temelju zadanih parametara
    # SEARCH
    def get_queryset(self):
        # ako nije definirana vrijednost prebacuje na except blok
        try:
            # putanja URL sadrzi 'account' (iza upitnika u URL-u mora biti account)
            a = self.request.GET.get('account',)
        # ako URL ne sadrzi account, prikazuje errore kao ljepse napisane poruke ili u ovom slucaju vraca na prazno polje
        except KeyError:
            a = None
        # ako je a pronadeno:
        if a:
            # instanca na klasu Account kojoj je dodan filter
            # filter omogucuje mala/velika slova, trazi ownera iz Accounta(user)
            account_list = Account.objects.filter(name__icontains=a, owner=self.request.user)

        # ako je a prazno polje:
        else:
            # filter za trazenje ownera
            account_list = Account.objects.filter(owner=self.request.user)

        # vrati instancu, popis accounta
        return account_list

    # Instanc metoda koja zahtjeva request argument + druge argumente
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # Koristimo super kada ne znamo kako se zove parent klasa
        return super(AccountList, self).dispatch(*args, **kwargs)

# Jedino autenticni user moze pristupiti stranici
@login_required()
def account_detail(request, uuid):
    # ako duzina argumenta sonja nije jednaka 22(22 je duzina uuid-a):
    if len(uuid) != 22:
        # instanca na klasu Account gdje dohvaca id iz accounta
        account = Account.objects.get(id=uuid)
        print(account.owner)
        print(Account.objects.get(id=uuid))
        # ako owner id nije jednak useru vrati error
        if account.owner != request.user:
            return HttpResponseForbidden()

    # ako je duzina 22 instanca bla dohvaca uuid
    else:
        bla = Account.objects.get(uuid=uuid)
        # ako owner uuid nije jednak useru vrati error
        if bla.owner != request.user:
            return HttpResponseForbidden()
    # instanca na klasu Contact gdje je account kljuc na tablicu user
    # filtriraj objekte po id ili uuid(ovisi jel bio if ili else)
    contacts = Contact.objects.filter(account=bla)
    # dictionary koje cemo koristiti u kreiranju URL-a
    variables = {'account': bla, 'contacts': contacts}
    # vrati zahtijev usera(po id-u ili uuid-u), HTML zapis o detaljima i kontakte koji pripadaju tom useru
    return render(request, 'accounts/account_detail.html', variables)


@login_required()
def account_cru(request, uuid=None):
    # ako je uuid
    if uuid:
        # dohvati Account ili ako uuid ne postoji vrati gresku
        account = get_object_or_404(Account, uuid=uuid)
        # ako owner nije jednak useru varti gresku
        if account.owner != request.user:
            return HttpResponseForbidden()
    else:
        account = Account(owner=request.user)

    # ako se kreira novi user
    if request.POST:
        # instanca na AccountForm, gdje kreiramo novi account
        form = AccountForm(request.POST, instance=account)
        # ako je forma validna snimt cemo ju i vratiti detalje o tom accountu
        if form.is_valid():
            form.save()
            redirect_url = reverse('account_detail', args=(account.uuid,))
            return HttpResponseRedirect(redirect_url)
    # ako se ne kreira novi account, forma ostaje ista
    else:
        form = AccountForm(instance=account)
    # dic s kojim stvaramo URL
    variables = {'form': form, 'account': account}
    # ako je kreiranje uspjesno stranica se ne mora refreshati nego nas odma baca na item_form gdje mozemo editirati account
    if request.is_ajax():
        template = 'accounts/account_item_form.html'
    # ako kreiranje novog accounta nije uspijesno, vraca nas na account_cru gdje je forma za kreiranje novog accounta
    else:
        template = 'accounts/account_cru.html'
    # vraca userov zahtijev, odredeni template (ovisno jel kreiran novi ili vec postojeci user) i accounte koji
    # pripadaju novo kreirenom ili postojecem useru
    return render(request, template, variables)
