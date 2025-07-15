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

## 🧠 ¿Qué aprenderás?

- Limpieza y transformación de datos con `pandas`
- Visualización interactiva con `plotly`
- Clasificación geográfica con lógica de latitudes
- Exploración de patrones temporales en datos reales

---

## 🛠️ Tecnologías

- Python 3
- pandas
- plotly
- seaborn / matplotlib
- Google Colab

---

## 📁 Estructura del proyecto

```bash
📦 sismos-en-chile
├── terremotos_en_chile.py        # Código fuente del análisis
├── Sismos en Chile - Explicado por el Pastor.pdf  # Presentación del proyecto
└── README.md
