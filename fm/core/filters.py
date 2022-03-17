import django_filters
from fm.core.models import Stations

# https://www.dicas-de-django.com.br/16-filtros-com-django-filter


class StationFilter(django_filters.FilterSet):
    uf = django_filters.CharFilter(lookup_expr='icontains')
    localidade = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Stations
        fields = ['uf', 'localidade', ]
