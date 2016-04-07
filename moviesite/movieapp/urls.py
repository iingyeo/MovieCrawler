from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^delete/(?P<item_id>\d+)/$', 'movieapp.views.delete'),
    url(r'^deleteall/$', 'movieapp.views.deleteAll'),
    url(r'^run/$', 'movieapp.views.run'),
]
