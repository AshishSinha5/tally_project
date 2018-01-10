from django.conf.urls import url
from . import views

app_name = 'counter'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),

    url(r'^counter/add/$', views.CounterCreate.as_view(), name='counter-add'),

    url(r'^counter/(?P<pk>[0-9]+)/$', views.CounterUpdate.as_view(), name='counter-update'),

    url(r'^counter/(?P<pk>[0-9]+)/delete/$', views.CounterDelete.as_view(), name='counter-delete'),

]