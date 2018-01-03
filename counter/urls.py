from django.conf.urls import url
from . import views

app_name = 'counter'

urlpatterns = [
    # /counter/
    url(r'^$', views.index, name='index'),

    # /counter/favorite
    url(r'^favorite/$', views.favorite, name='favorite'),
    # /counter/712/
    url(r'^(?P<counter_id>[0-9]+)/$', views.detail, name='detail'),
]