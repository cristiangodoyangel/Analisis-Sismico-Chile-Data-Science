
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Importamos el data set en formato csv y lo guardamos en una variable.
path = r"C:\Users\StarMan\Desktop\DataScience\Proyecto\seismic_data.csv"
df_1 = pd.read_csv(path)

# revisamos la correcta carga de los datos.
print("\n")
print("======================= Carga de datos correcta =======================")
print("\n")
print(df_1.head())

# revisamos la informacion del dataset, lo primero siempre es conocer los datos que tenemos.
print("\n")
print("======================= Información del Dataset Sismico =======================")
print("\n")
print(df_1.info())  

# revisamos la estadistica descriptiva del dataset.
print("\n")
print("======================= Estadística Descriptiva del Dataset Sismico =======================")
print("\n")
print(df_1.describe().round(1).T)
print("\n")

# con la estadistica descriptiva podemos ver que el dataset tiene 4018 filas y 5 columnas.
# con la información del dataser podemos ver que la fecha no está en el formato correcto, 
# está en string, si necesitamos generar estadisticas sobre la fecha, debemos convertirlo a datetime.

# convertimos la fecha a datetime.
# Convertir a zona horaria de Chile
df_1['Fecha'] = pd.to_datetime(df_1['Date(UTC)'])

# todos los datos están en UTC, por lo que debemos convertirlos a Chile
df_1['Fecha_Chile'] = df_1['Fecha'].dt.tz_localize('UTC').dt.tz_convert('America/Santiago')

# se crean por separado, año y mes
df_1['Año'] = df_1['Fecha_Chile'].dt.year
df_1['Mes'] = df_1['Fecha_Chile'].dt.month

# verificamos la correcta conversión de la fecha.
print("\n")
print("======================= Verificación de Año y Mes =======================")
print(df_1[['Fecha_Chile', 'Año', 'Mes']].head())

#

