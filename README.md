# 🇨🇱 Sismos en Chile - Explicado por el Pastor

![Portada](https://github.com/cristiangodoyangel/Analisis-Sismico-Chile-Data-Science/blob/ccd2e4ea36b6f6c3129db5eaf1740cf6516abb31/assets/banner.png)

# Análisis de datos sísmicos en Chile (2012–2025)

Análisis de datos sísmicos en Chile entre 2012 y 2025, usando herramientas de ciencia de datos modernas, explicado de forma accesible y educativa por el Pastor Cristian Godoy Angel. Este proyecto combina análisis técnico con una mirada pastoral y pedagógica, para ayudar a entender de forma clara cómo se comporta la tierra en Chile, uno de los países más sísmicos del mundo.

# ✨ Propósito del Proyecto

Chile está sobre el Cinturón de Fuego del Pacífico, y por tanto la actividad sísmica es una realidad constante. Sin embargo, muchos no entienden cuándo, dónde y con qué frecuencia ocurren estos eventos. Este proyecto tiene como propósito:

Educar al público general sobre la distribución de los sismos en el país.

Presentar análisis de datos de manera clara, accesible y visual.

Fortalecer el vínculo entre ciencia, educación y conciencia social.



---

## 🧠 Habilidades de Ciencia de Datos aplicadas
Este proyecto es un ejemplo práctico de cómo aplicar diversas competencias de Data Science, que como estudiante de Alura Latam auspiciado por Oracle, estoy desarrollando:

✅ Recolección y carga de datos:

Lectura y validación de grandes volúmenes de datos .csv.

Integración de datasets con formatos espaciales (GeoJSON) mediante GeoPandas.

✅ Limpieza y transformación de datos (pandas):

Conversión de fechas y horas al huso horario chileno.

Extracción de variables temporales: año, mes, hora.

Agrupamiento por zona, región, tiempo.

✅ Análisis exploratorio de datos (EDA):

Distribución mensual y horaria de los sismos.

Promedios mensuales y anuales.

Clasificación geográfica por latitud y por polígonos regionales.

✅ Visualización de datos avanzada:

Gráficos dinámicos y personalizables con plotly.express.

Mapas interactivos con choropleth_mapbox para visualizar los sismos por región.

Gráficos ordenados por cuatrimestres y zonas del país.

✅ Análisis espacial con Python:

Uso de shapely para geometría.

Uniones espaciales (sjoin) con regiones oficiales de Chile.

Corrección de errores geográficos con buffer(0).

✅ Exportación y reutilización de datasets:

Generación de nuevos .csv procesados para uso futuro.

Preparación de datos para dashboards o informes PDF.

---

## 📊 Visualizaciones del Proyecto

🔥 Mapa de calor (Heatmap): Distribución de sismos por mes y hora del día.

📊 Promedios mensuales: Divididos en cuatrimestres, para facilitar la lectura.

🌍 Zonas geográficas: Clasificación en Norte, Centro y Sur, con sus top 3 sismos.

🗺️ Análisis por región: 16 regiones chilenas, con sus promedios anuales y top 3 sismos.

🗺️ Mapas interactivos con zoom: Mapas por región que muestran los 3 sismos más intensos dentro del área geográfica.

🧮 Estadísticas generales: Conteo, distribución, magnitudes, fechas.

## 🛠️ Tecnologías utilizadas

Python 3 — Lenguaje principal

pandas — Limpieza y análisis de datos

plotly.express — Visualización dinámica e interactiva

geopandas — Análisis geoespacial

shapely — Manipulación de geometrías

matplotlib / seaborn — Visualización adicional

Google Colab — Entorno de desarrollo colaborativo

GeoJSON — Para delimitar regiones oficiales de Chile

---

## 📁 Estructura del proyecto

```bash
📦 sismos-en-chile
├── terremotos_en_chile.py                     # Código fuente completo (Google Colab)
├── df_1_sismos_chile.csv                      # Dataset limpio con zonas geográficas
├── df_sismos_con_regiones.csv                 # Dataset unido a regiones oficiales de Chile
├── Sismos en Chile - Explicado por el Pastor.pdf  # Presentación lista para compartir
└── README.md                                  # Documentación del proyecto
```




