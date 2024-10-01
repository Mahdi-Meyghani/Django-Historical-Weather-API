from django.urls import path
from . import views

urlpatterns = [
    path('', views.documentation, name='documentation'),
    path('v1/api/<int:staid>/', views.station, name='station'),
    path('v1/api/<int:staid>/<str:date>/', views.station_date, name='station_date'),
    path('v1/api/yearly/<int:staid>/<str:year>/', views.station_year, name='station_year'),
]