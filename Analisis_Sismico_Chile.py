
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

# nos encontramos con un detalle, el mes es numérico ya que necesitamos que sea numérico para las estadísticas y gráficos,
# pero también lo necesitamos en texto para que se entienda mejor

# Columna numérica, para análisis y gráficos.
df_1['Mes'] = df_1['Fecha_Chile'].dt.month

# Columna en texto, para mostrar la tabla final a los usuarios, para los labels de gráficos
meses = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}
df_1['Mes_Nombre'] = df_1['Mes'].map(meses)

# verificamos si tenemos correctamente los datos numéricos y en texto
print("\n")
print("======================= Verificación de Año y Mes =======================")
print(df_1[['Fecha_Chile', 'Año', 'Mes', 'Mes_Nombre']].head())
print("\n")

# vemos otro detalle, la hora. necesitamos mostrar la hora para que se entienda mejor y segmentar los sismos por hora
# se extrae la hora exacta del datetime, se convierte a texto como hora exacta.
df_1['Hora_Exacta'] = df_1['Fecha_Chile'].dt.time
print("\n")
print("======================= Verificación de Hora =======================")
print(df_1[[ 'Año', 'Mes_Nombre', 'Hora_Exacta']].head())
print("\n")

# Se extrae la hora exacta del datetime, se convierte a texto como hora exacta.
df_1['Hora_Exacta'] = df_1['Fecha_Chile'].dt.time
print("\n")
print("======================= Verificación de Hora =======================")
print(df_1[[ 'Año', 'Mes_Nombre', 'Hora_Exacta']].head())
print("\n")

# Se extrae la hora exacta del datetime, se convierte Hora para análisis y gráficos.
df_1['Hora'] = df_1['Fecha_Chile'].dt.hour
print("\n")
print("======================= Verificación de Hora =======================")
print(df_1[['Fecha_Chile', 'Año', 'Mes', 'Mes_Nombre', 'Hora', 'Hora_Exacta']].head())
print("\n")
