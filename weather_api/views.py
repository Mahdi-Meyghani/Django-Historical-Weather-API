from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd


# 2 functions to avoiding code repeated
def dataframe_operations(dataframe):
    dataframe.columns = map(str.strip, dataframe.columns)
    dataframe['DATE'] = pd.to_datetime(dataframe['DATE'], format='%Y%m%d')
    dataframe['DATE'] = dataframe['DATE'].astype(str)

def dataframe_modified(dataframe):
    dataframe['TG'] = dataframe['TG'] / 10
    dataframe['TG'] = dataframe['TG'].replace({-999.9: "LOST"})


df = pd.read_csv('data/stations.txt', skiprows=17)
def documentation(request):
    return render(request, 'documentation.html',
                  context={'stations': df.to_html(index=False, col_space=130)})


def station(request, staid):
    filepath = f'data/TG_STAID{staid.zfill(6)}.txt'

    station_df = pd.read_csv(filepath, skiprows=20)
    dataframe_operations(station_df)
    dataframe_modified(station_df)

    df_filtered = station_df[['DATE', 'TG']]
    df_dictionary = df_filtered.to_dict('records')

    response = JsonResponse(df_dictionary, status=200, safe=False)

    return response


def station_date(request, staid, date):
    filepath = f'data/TG_STAID{staid.zfill(6)}.txt'

    station_df = pd.read_csv(filepath, skiprows=20)
    dataframe_operations(station_df)

    date_station_df = station_df.loc[station_df['DATE'] == date][['DATE', 'TG']]
    dataframe_modified(date_station_df)

    date_station_dict = date_station_df.to_dict('records')
    response = JsonResponse(date_station_dict, status=200, safe=False)

    return response


def station_year(request, staid, year):
    filepath = f'data/TG_STAID{staid.zfill(6)}.txt'

    station_df = pd.read_csv(filepath, skiprows=20)
    dataframe_operations(station_df)

    year_station_df = station_df.loc[station_df['DATE'].str.startswith(year)][['DATE', 'TG']]
    dataframe_modified(year_station_df)

    year_station_dict = year_station_df.to_dict('records')
    response = JsonResponse(year_station_dict, status=200, safe=False)

    return response


def error_500(request):
    return render(request, 'error_500.html', status=500)