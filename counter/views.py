from django.shortcuts import render, get_object_or_404
from .models import CounterName, NetCount


def index(request):
    all_counters = CounterName.objects.all()
    return render(request, 'counter/index.html', {'all_counters': all_counters})


def detail(request, counter_id):
    # counter = CounterName.objects.get(pk=counter_id)
    counter = get_object_or_404(CounterName, pk=counter_id)
    latest_count = NetCount.objects.filter(CounterName__id=counter_id).last()
    latest_count = latest_count.numCount
    return render(request, 'counter/details.html', {'counter': counter,
                                                    'latest_count': latest_count,
                                                    })


def favorite(request):
    all_counters = CounterName.objects.all()
    try:
        selected_counter = CounterName.objects.get(pk=request.POST['counter'])
    except (KeyError, CounterName.DoesNotExist):
        return render(request, 'counter/index.html', {
            'all_counters': all_counters,
            'error_message': "You did not select any Counter",
        })
    else:
        selected_counter.is_favorite = True
        selected_counter.save()
        return render(request, 'counter/index.html', {'all_counters': all_counters})