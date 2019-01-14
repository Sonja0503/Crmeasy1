from django.conf.urls import patterns, url
from .views import AccountList

account_urls = patterns('',
    url(r'^list/$', AccountList.as_view(), name='account_list'),
    url(r'^new/$', 'crmapp.accounts.views.account_cru', name='account_new'),
    url(r'^(?P<uuid>[\d\w-]+)/edit/$', 'crmapp.accounts.views.account_cru', name='account_update'),
    url(r'^(?P<uuid>[\d\w-]+)/$', 'crmapp.accounts.views.account_detail', name='account_detail'),
)
