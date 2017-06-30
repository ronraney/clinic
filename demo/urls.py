from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.demo_list, name='demo_list'),
    url(r'^person/(?P<pk>\d+)/$', views.demo_detail, name='demo_detail'),
    url(r'^person/new/$', views.demo_new, name='demo_new'),
    url(r'^person/(?P<pk>\d+)/edit/$', views.demo_edit, name='demo_edit'),
]
