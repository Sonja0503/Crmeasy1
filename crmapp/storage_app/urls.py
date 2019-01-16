from django.conf.urls import patterns, url
from .views import ItemList
from .views import ItemDelete

item_urls = patterns('',
    url(r'^list/$', ItemList.as_view(), name='item_list'),
    url(r'^new/$', 'crmapp.storage_app.views.item_new', name='item_new'),
    url(r'^(?P<id>[\d\w-]+)/edit/$', 'crmapp.storage_app.views.item_cru', name='item_update'),
    url(r'^(?P<pk>[\d\w-]+)/delete/$', ItemDelete.as_view(), name='item_delete'),

)