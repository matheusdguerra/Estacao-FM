from django.shortcuts import render
from fm.core.models import Stations


def home(request):
    stations = Stations.objects.all()
    return render(request, 'index.html', {'stations': stations})
