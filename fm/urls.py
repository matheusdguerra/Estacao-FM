from django.contrib import admin
from django.urls import path
from fm.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<int:id>/', views.station_detail, name='station_detail'),
    path('<str:uf>/', views.station_uf, name='station_uf'),
]
