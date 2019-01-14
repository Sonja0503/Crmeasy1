from django.conf.urls import patterns, include, url
from marketing.views import HomePage
from django.contrib import admin
from accounts.urls import account_urls
from contacts.urls import contact_urls


admin.autodiscover()

urlpatterns = patterns('',
    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),
    url(r'^signup/$', 'crmapp.subscribers.views.subscriber_new', name='signUp'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
    url(r'^account/', include(account_urls)),
    url(r'^contact/', include(contact_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
