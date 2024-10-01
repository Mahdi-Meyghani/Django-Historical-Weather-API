from django.core.management.base import BaseCommand
from weather_api.models import WeatherData
import glob
import pandas as pd
from pathlib import Path


class Command(BaseCommand):
    help = "Load historical weather data to postgres database"

    def handle(self, *args, **kwargs):
        self.stdout.write("Start the function handle...")
        self.stdout.write("======================================================")

        filepaths = glob.glob("data/*.txt")[1:]
        filepaths = [Path(filepath) for filepath in filepaths]

        for filepath in filepaths:
            self.stdout.write("Create dataframe of each path")
            self.stdout.write("======================================================")

            df = pd.read_csv(filepath, skiprows=20)
            df.columns = map(str.strip, df.columns)
            df['DATE'] = pd.to_datetime(df['DATE'], format='%Y%m%d')
            df['DATE'] = df['DATE'].astype(str)
            df['TG'] = df['TG'] / 10

            self.stdout.write("Start bulk_create dataframe")
            self.stdout.write("======================================================")

            WeatherData.objects.bulk_create([WeatherData(
                STAID=row['STAID'], SOUID=row['SOUID'], DATE=row['DATE'], TG=row['TG'], Q_TG=row['Q_TG'])
                for index, row in df.iterrows()
            ])

            self.stdout.write("Finish bulk_create")
            self.stdout.write("======================================================")

        print("We are Done man :)")
