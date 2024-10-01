from django.core.management.base import BaseCommand
import pandas as pd
from pathlib import Path
from weather_api.models import AvailableStations


class Command(BaseCommand):
    help = "Insert available stations from 'data/stations.txt' into postgres table named 'available_stations'"

    def handle(self, *args, **kwargs):
        print("Start insert data...")
        print("********************************************************************************")
        path = Path("data", "stations.txt")
        df = pd.read_csv(path, skiprows=17)

        df.columns = map(str.strip, df.columns)
        AvailableStations.objects.bulk_create([
            AvailableStations(STAID=row["STAID"], STANAME=row["STANAME"], CN=row["CN"],
                              LAT=row["LAT"], LON=row["LON"], HGHT=row["HGHT"], ) for _, row in df.iterrows()
        ])

    print("Finish inserting data...")
