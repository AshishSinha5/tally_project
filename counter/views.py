from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import CounterName, NetCount
NoneType = type(None)


class IndexView(generic.ListView):
    template_name = 'counter/index.html'

    def get_queryset(self):
        return CounterName.objects.all()


class DetailView(generic.DetailView):
    model = CounterName
    template_name = 'counter/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        counter = context['countername']
        context['latestCount'] = NetCount.objects.filter(CounterName__id=counter.id).last()
        return context


class CounterCreate(CreateView):
    model = CounterName
    fields = ['title', 'description']
    template_name = 'counter/counter_form.html'


class CounterUpdate(UpdateView):
    model = CounterName
    fields = ['title', 'description']
    template_name = 'counter/counter_form.html'


class CounterDelete(DeleteView):
    model = CounterName
    success_url = reverse_lazy('counter:index');













