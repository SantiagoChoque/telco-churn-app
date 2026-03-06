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
 ┣ 📂 .streamlit         # Configuración de tema y despliegue
 ┃ ┗ 📜 config.toml
 ┣ 📂 img                # Recursos visuales (Logos de Python, Pandas, etc.)
 ┣ 📜 app.py             # Archivo principal de la aplicación
 ┣ 📜 requirements.txt   # Dependencias del proyecto
 ┗ 📜 README.md          # Documentación
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
* Repositorio GitHub: [https://github.com/SantiagoChoque/app-eda/](https://github.com/SantiagoChoque/app-eda/)
* Aplicación en Streamlit Cloud: [https://app-santiagochoque.streamlit.app](https://app-santiagochoque.streamlit.app)
* Correo: sgchoquefer@gmail.com
* Año: 2026
