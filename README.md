# 🏙️ EDA de Datos de Airbnb en Nueva York

Este proyecto forma parte del Máster en Data Science & IA Generativa de **Evolve Academy**.  
El objetivo es realizar un **Análisis Exploratorio de Datos (EDA)** completo sobre un dataset real de Airbnb, incluyendo carga, exploración, limpieza, transformación y visualización.

## 📌 Objetivos del proyecto

- Comprender la estructura del dataset: dimensiones, tipos de datos, calidad.
- Detectar y corregir valores nulos, duplicados e incoherencias.
- Normalizar los datos y documentar las decisiones de limpieza.
- Realizar visualizaciones que permitan extraer conclusiones relevantes.
- Publicar el proyecto de forma organizada en un repositorio.

## 🧼 Proceso de limpieza y decisiones

En la fase de data cleaning se aplicaron transformaciones como:

✔ Conversión de tipos (fechas, booleanos, numéricos)  
✔ Corrección de formatos monetarios  
✔ Normalización de categorías  
✔ Eliminación de duplicados  
✔ Imputación / eliminación de registros con incoherencias  
✔ Tratamiento de outliers en *minimum_nights* y *price*  
✔ Conversión de *last_review* a fecha válida

> Se documentan todos los pasos en el notebook **02_Data_Cleaning.ipynb**.

---

## 📊 Visualizaciones destacadas

- Histograma de precio por noche  
- Distribución de reviews y actividad temporal del mercado  
- Estacionalidad por meses del año  
- Boxplot de precios por zona  
- Scatter Precio vs. Reviews  
- Mapa geográfico interactivo de alojamientos en NYC

Las visualizaciones permiten entender tendencias de mercado, estacionalidad y distribución espacial.

---

## 🔎 Principales hallazgos

**Concentración geográfica**  
La mayoría de alojamientos se encuentran en **Manhattan y Brooklyn**.

**Mercado altamente variable**  
Amplio rango de precios → coexistencia de oferta económica y de lujo.

**Estacionalidad marcada**  
La mayor actividad se concentra en **junio y verano**.

**Impacto de la pandemia**  
Caída brusca de reviews en 2020 y recuperación gradual después.

**Año de construcción poco realista**  
Años acotados entre 2003–2022 → fuerte indicio de **anonimización del dato**.

**Presencia de empresas de gestión**  
Algunos anfitriones administran más de 300 anuncios.

---

## 🧠 Conclusión final

Airbnb en Nueva York es un mercado turístico muy activo y competitivo, con fuerte dependencia estacional y una amplia
variedad de alojamientos según barrio, precio y nivel de profesionalización.  
El dataset muestra transformaciones de anonimización, pero aún así permite obtener una visión clara del comportamiento
del mercado.

---

## 📎 Fuente del Dataset

Datos públicos de **Airbnb Open Data**  
Disponible en Kaggle / Open Data Hosting.

---

## 👨‍💻 Autor

**Óscar Fernández-Chichilla López**  
Máster en Data Science & IA Generativa — *Evolve Academy (2025/2026)*

---