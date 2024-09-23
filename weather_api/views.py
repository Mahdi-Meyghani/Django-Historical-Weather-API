from django.shortcuts import render
import pandas as pd

def documentation(request):
    df = pd.read_csv('data/stations.txt', skiprows=17)

    return render(request, 'documentation.html',
                  context={'stations': df.to_html(index=False, col_space=130)})