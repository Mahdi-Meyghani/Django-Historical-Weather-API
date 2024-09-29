from django.db import models


class WeatherData(models.Model):
    STAID = models.IntegerField()
    SOUID = models.IntegerField()
    DATE = models.CharField(max_length=200)
    TG = models.FloatField()
    Q_TG = models.IntegerField()

    class Meta:
        db_table = "weather_data"