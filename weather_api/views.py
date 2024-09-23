from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

df = pd.read_csv('data/stations.txt', skiprows=17)
def documentation(request):
    return render(request, 'documentation.html',
                  context={'stations': df.to_html(index=False, col_space=130)})


def station(request, staid):
    filepath = f'data/TG_STAID{staid.zfill(6)}.txt'

    station_df = pd.read_csv(filepath, skiprows=20)
    station_df.columns = map(str.strip, station_df.columns)
    station_df['DATE'] = pd.to_datetime(station_df['DATE'], format='%Y%m%d')
    station_df['DATE'] = station_df['DATE'].astype(str)
    station_df['TG'] = station_df['TG'] / 10
    station_df['TG'] = station_df['TG'].replace({-999.9: "LOST"})

    df_filtered = station_df[['DATE', 'TG']]
    df_dictionary = df_filtered.to_dict('records')

    response = JsonResponse(df_dictionary, status=200, safe=False)

    return response