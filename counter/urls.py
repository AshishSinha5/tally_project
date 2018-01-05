from django.conf.urls import url
from . import views

app_name = 'counter'

urlpatterns = [
    # /counter/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /counter/712/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
]