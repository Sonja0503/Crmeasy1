from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse


from .forms import SubscriberForm
from .models import Subscriber
# Metoda koja zahtjeva request
def subscriber_new(request, template='subscribers/subscriber_new.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User(username=username, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()

            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            sub = Subscriber(address_one=address_one, address_two=address_two, city=city, state=state, user_rec=user)
            sub.save()

            authenticated = authenticate(username=username, password=password)
            if authenticated is not None:
                if authenticated.is_active:
                    login(request, authenticated)
                    return HttpResponseRedirect(reverse('home'))

                else:
                    return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))
            else:
                return HttpResponseRedirect(reverse('signUp'))
    else:
        form = SubscriberForm()
    return render(request, template, {'form':form})