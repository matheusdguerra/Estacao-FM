from django.shortcuts import render, get_object_or_404, get_list_or_404
from fm.core.models import Stations
from .filters import StationFilter


def home(request):
    template_name = 'index.html'
    stations_list = Stations.objects.all()
    uf_list = Stations.objects.values('uf').order_by('uf').distinct()
    stations_filter = StationFilter(request.GET, queryset=stations_list)

    context = {
        'stations_list': stations_list,
        'filter': stations_filter,
        'uf_list': uf_list
    }

    return render(request, template_name, context)


def station_detail(request, id):
    station = get_object_or_404(Stations, pk=id)
    return render(request, 'detail.html', {'station': station})


def station_uf(request, uf):
    stations_uf = get_list_or_404(Stations, uf=uf)
    return render(request, 'station_uf.html', {'stations_uf': stations_uf})
