from django.contrib import admin
from fm.core.models import Stations


class StationModelAdmin(admin.ModelAdmin):
    list_display = ('entidade', 'uf', 'localidade', 'frequencia')
    search_fields = ('entidade', 'uf', 'localidade', 'frequencia')


admin.site.register(Stations, StationModelAdmin)
