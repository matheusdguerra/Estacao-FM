from django.shortcuts import render
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
