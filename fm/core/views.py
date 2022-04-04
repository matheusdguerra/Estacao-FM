from django.shortcuts import render, get_object_or_404
from fm.core.models import Stations
from .filters import StationFilter


def home(request):
    template_name = 'index.html'
    stations_list = Stations.objects.all()
    stations_filter = StationFilter(request.GET, queryset=stations_list)

    context = {
        'stations_list': stations_list,
        'filter': stations_filter
    }

    return render(request, template_name, context)


def station_detail(request, id):
    station = get_object_or_404(Stations, pk=id)
    return render(request, 'detail.html', {'station': station})
