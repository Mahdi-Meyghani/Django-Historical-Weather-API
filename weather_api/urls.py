from django.urls import path
from . import views

urlpatterns = [
    path('', views.documentation, name='documentation'),
    path('v1/api/<str:staid>/', views.station, name='station')
]