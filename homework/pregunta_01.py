# pylint: disable=line-too-long
def pregunta_01():
    return

import matplotlib.pyplot as plr
import pandas as pd 

csvloc = "../files/input/shipping-data.csv"

def load_data():
    df = pd.read_csv(csvloc)
    return df

dataro = load_data()

print (dataro.head())

"""
* El archivo de datos se encuentra en la carpeta `data`.
* Todos los archivos debe ser creados en la carpeta `docs`.
* Su código debe crear la carpeta `docs` si no existe.
"""