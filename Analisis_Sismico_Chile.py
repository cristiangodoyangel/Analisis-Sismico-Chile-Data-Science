
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

print("\n")
print("======================= Información del Dataset Sismico =======================")
print("\n")
print(df_1.info())  

print("\n")
print("======================= Estadística Descriptiva del Dataset Sismico =======================")
print("\n")
print(df_1.describe().round(1).T)
print("\n")
