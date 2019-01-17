from django.conf.urls import patterns, url
from .views import BlogList
from .views import BlogDelete

blog_urls = patterns('',
    url(r'^list/$', BlogList.as_view(), name='blog_list'),
    url(r'^new/$', 'crmapp.blog.views.blog_new', name='blog_new'),
    url(r'^(?P<id>[\d\w-]+)/edit/$', 'crmapp.blog.views.blog_cru', name='blog_cru'),
    url(r'^(?P<id>[\d\w-]+)/user_blog/$', 'crmapp.blog.views.user_list_blog', name='user_list_blog'),
    url(r'^(?P<pk>[\d\w-]+)/delete/$', BlogDelete.as_view(), name='blog_delete'),
)