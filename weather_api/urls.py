from django.urls import path
from . import views

urlpatterns = [
    path('', views.documentation, name='documentation'),
    path('v1/api/<str:staid>/', views.station, name='station'),
    path('v1/api/<str:staid>/<str:date>/', views.station_date, name='station_date'),
    path('v1/api/yearly/<str:staid>/<str:year>/', views.station_year, name='station_year'),
]