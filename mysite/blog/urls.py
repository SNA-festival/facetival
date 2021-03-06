from django.conf.urls import patterns, include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings

#urlpatterns = patterns('',  mish v1 
urlpatterns = patterns('',
    url(r'^list/$', views.list, name='list'),
    url(r'^HomePage/$', views.Home, name='Home'),
    url(r'^HomeHome$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^guides/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
