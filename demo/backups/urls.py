from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.demo_list, name='demo_list'),
    url(r'^person/(?P<pk>\d+)/$', views.demo_detail, name='demo_detail'),
]
