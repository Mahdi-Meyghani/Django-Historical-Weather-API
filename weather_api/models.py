from django.db import models


class WeatherData(models.Model):
    STAID = models.IntegerField()
    SOUID = models.IntegerField()
    DATE = models.CharField(max_length=200)
    TG = models.FloatField()
    Q_TG = models.IntegerField()

    class Meta:
        db_table = "weather_data"


class AvailableStations(models.Model):
    STAID =models.IntegerField()
    STANAME = models.CharField(max_length=250)
    CN = models.CharField(max_length=250)
    LAT = models.CharField(max_length=250)
    LON = models.CharField(max_length=250)
    HGHT = models.IntegerField()

    class Meta:
        db_table = "available_stations"
