# 📊 Proyecto: Telco Customer Churn Analytics

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red) ![Pandas](https://img.shields.io/badge/Library-Pandas-brightgreen) ![Seaborn](https://img.shields.io/badge/Library-Seaborn-orange)

Este proyecto consiste en una plataforma interactiva de **Análisis Exploratorio de Datos (EDA)** desarrollada en **Python**. El sistema permite identificar los factores críticos que influyen en la deserción de clientes (Churn) mediante el procesamiento de datos, estadísticas avanzadas y visualizaciones dinámicas.

## 🚀 Características

* **Carga Dinámica**: Sistema de validación de archivos CSV con pre-procesamiento automático de tipos de datos.
* **Auditoría de Datos**: Detección visual de valores nulos y espacios en blanco mediante Heatmaps de Seaborn.
* **Análisis Bivariado**: Explorador interactivo que permite cruzar variables categóricas y numéricas para hallar patrones de fuga.
* **Arquitectura Profesional**: Implementación de **Programación Orientada a Objetos (POO)** mediante la clase `DataAnalyzer` para centralizar la lógica analítica.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 🐍
* **Framework Web:** Streamlit
* **Gestión de Datos:** Pandas & Numpy
* **Visualización:** Matplotlib & Seaborn

## 📂 Estructura del Proyecto

```text
📦 telco-churn-app
 ┣ 📂 .streamlit               # Configuración de tema y despliegue
 ┃ ┗ 📜 config.toml
 ┣ 📂 img                      # Recursos visuales (Logos de Python, Pandas, etc.)
 ┣ 📜 README.md                # Documentación
 ┣ 📜 TelcoCustomerChrun.csv   # Archivo a subir para el análisis
 ┣ 📜 app.py                   # Archivo principal de la aplicación
 ┣ 📜 requirements.txt         # Dependencias necesarias
```

### 📂 Desglose de los Módulos

#### 🏠 Home (Panel Principal)
* **Vista General:** Presentación de los objetivos del proyecto y descripción de las variables del dataset.

#### 🌐 Módulo de Carga
* **Ingesta de Datos:** Interfaz para subir el dataset oficial TelcoCustomerChurn.csv.

* **Transformación:** Conversión inmediata de TotalCharges a numérico y SeniorCitizen a objeto.

#### 📊 Análisis Exploratorio (EDA)
* **Estructura y Limpieza:** Reporte de tipos de datos y eliminación de registros incompletos.

* **Estadísticas Descriptivas:** Análisis de tendencia central y dispersión para entender la media de cargos y permanencia.

* **Visualización de Distribuciones:** Histogramas y Pie Charts automáticos para segmentación de mercado.

* **Hallazgos Clave:** Dashboard con métricas de impacto (KPIs) y análisis de Churn por tipo de contrato y cargos.

### 📸 Capturas de la aplicación:
* **Módulo de carga y visualización:**
<img width="749" height="465" alt="image" src="https://github.com/user-attachments/assets/2d4f39a4-f5b2-4f0a-92dc-17deea363536" />
<img width="753" height="601" alt="image" src="https://github.com/user-attachments/assets/6a7ecb6e-462b-43f2-89c1-556da1a9dfde" />

* **Opciones del Módulo de Análisis Exploratorio (EDA):**
<img width="741" height="167" alt="image" src="https://github.com/user-attachments/assets/e3c323e6-ca65-4fc7-af49-7a013b15ee88" />
<img width="738" height="48" alt="image" src="https://github.com/user-attachments/assets/b7165287-5155-437e-98fd-78aca0a20594" />

* **Estructura del dataset:**
<img width="738" height="861" alt="image" src="https://github.com/user-attachments/assets/2220aad8-4760-45b4-b5e0-98679aff34d4" />

* **Gráfico Resumen Clave:**
<img width="724" height="523" alt="image" src="https://github.com/user-attachments/assets/5e264c22-dfce-44dc-953c-ebc93a40e0b8" />


### 🏁 Conclusiones Estratégicas
* **🚨 Crisis de Fidelidad:** Alta deserción detectada en el primer año de servicio.

* **💸 Sensibilidad al Precio:** Los cargos mensuales entre $70 y $90 disparan la fuga.

* **📑 Problemas Contractuales:** El modelo 'Mes a Mes' es la principal puerta de salida del cliente.

# 🛠️ Instrucciones de Uso

## 1. Clonar Repositorio:
```bash
git clone [https://github.com/SantiagoChoque/telco-churn-app.git](https://github.com/SantiagoChoque/telco-churn-app.git)
cd telco-churn-app
```
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```
4. Ejecutar aplicación:
```bash
streamlit run app.py
```
## ✏️ Autor: Santiago Gabriel Choque Fernández
* Repositorio GitHub: [[https://github.com/SantiagoChoque/telco-churn-app/](https://github.com/SantiagoChoque/telco-churn-app/)]
* Aplicación en Streamlit Cloud: [[https://telco-churn-app-santiagochoque.streamlit.app](https://app-santiagochoque.streamlit.app)]
* Correo: sgchoquefer@gmail.com
* Año: 2026
