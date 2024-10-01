from django.shortcuts import render
import pandas as pd
from .serializers import WeatherDataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import WeatherData
from .models import AvailableStations


queryset = AvailableStations.objects.all().values()
df = pd.DataFrame(queryset).drop(["id"], axis=1)


def documentation(request):
    return render(request, 'documentation.html',
                  context={'stations': df.to_html(index=False, col_space=130)})


@api_view(['GET'])
def station(request, staid):
    data = WeatherData.objects.filter(STAID=staid)
    serializer = WeatherDataSerializer(data, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def station_date(request, staid, date):
    data = WeatherData.objects.filter(STAID=staid, DATE=date)
    serializer = WeatherDataSerializer(data, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def station_year(request, staid, year):
    data = WeatherData.objects.filter(STAID=staid, DATE__startswith=year)
    serializer = WeatherDataSerializer(data, many=True)

    return Response(serializer.data)
