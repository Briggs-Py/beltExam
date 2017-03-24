from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d{1,4})$', views.index, name='index'),
    url(r'^new/(?P<id>\d{1,4})$', views.new, name='new'),
    url(r'^process/(?P<id>\d{1,4})$', views.process, name='process'),
    url(r'^show/(?P<id>\d{1,4})$', views.show, name='show'),
    url(r'^add/(?P<id>\d{1,4})$', views.add, name='add'),
    url(r'^remove/(?P<id>\d{1,4})$', views.remove, name='remove'),
    url(r'^goback$', views.goback, name='goback'),
    url(r'^delete/(?P<id>\d{1,4})$', views.delete, name='delete')
]
