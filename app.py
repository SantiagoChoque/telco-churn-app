import streamlit as st 
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as py

if 'pagina' not in st.session_state:
    st.session_state.pagina = "🏠 Home"

ejercicios = ["🏠 Home", "🌐: Cargue su dataset", "📊: Análisis exploratorio de datos", "📘: Conclusiones y Recomendaciones"]

st.sidebar.image("img/DMC.png")
st.sidebar.title("📌 Navegación: ", text_alignment="left")
st.sidebar.selectbox("Elija el ejercicio: ", ejercicios, key="pagina")
#------------------------------------------------------------------------------------------------------------------------------
if st.session_state.pagina == "🏠 Home":
    st.title(" Proyecto Final de Especialización Python for Analytics", text_alignment="center")
    st.header(" Análisis Exploratorio de Datos",text_alignment="center")
    st.subheader("📦 Caso de Estudio n°2: TelcoCustomer",text_alignment="center")
    st.divider()
    st.subheader("🎯 Descripción del objetivo:")
    st.write(""" El presente trabajo tiene como propósito realizar un análisis descriptivo
            del dataset de Telcochurn, analizando valores faltantes, realizando análisis 
            estadísticos y sacando conclusiones de los mismos. No es propósito realizar 
            modelos predictivos, si no aplicar de manera integra los conceptos de la programación
            de Python, junto a las librerías Pandas, Numpy, Matplotlib, entre otras para desarrollar
            una herramienta funcional.
            """ 
            )
    st.divider()
    
    st.subheader("📖 Explicación del dataset: ")
    st.write("""
            El dataset Telco Customer Churn contiene información sobre una empresa de telecomunicaciones que proporcionó servicios de telefonía residencial e 
            Internet a 7,043 clientes. 
            
            El conjunto de datos incluye información en las siguientes categorías: 
            
            **👥 Información Demográfica:** Incluye el género del cliente, si es un adulto mayor (SeniorCitizen), y si tiene pareja o dependientes. 
            
            **🛠️ Servicios Contratados:** Registra si el cliente tiene servicio telefónico, múltiples líneas, tipo de servicio de Internet 
            (DSL, fibra óptica o ninguno), y servicios adicionales como seguridad en línea, respaldo, protección de dispositivos, soporte técnico y streaming de TV o películas. 

            **💳 Información de la Cuenta del Cliente:** Contiene datos sobre la permanencia en meses (tenure), el tipo de contrato 
            (mes a mes, un año o dos años), el método de pago, la facturación electrónica, los cargos mensuales y los cargos totales. 

            **📉 Variable Objetivo (Churn):** Indica si el cliente abandonó la compañía ("Yes" o "No") durante el último mes. 

            **🎯 Objetivo del Análisis**
            El propósito principal de trabajar con este dataset es aplicar técnicas de limpieza, transformación y visualización de datos para comprender las causas que motivan 
            a los clientes a dejar el servicio, facilitando así el desarrollo de estrategias de retención basadas en datos.  """)
    
    st.divider()
    st.subheader("👨‍💻 Datos generales:")
    st.write("**Nombre completo**: Santiago Gabriel Choque Fernández")
    st.write("**Curso**: Especialización Python for Analytics")
    st.write("**Año**: 2026")
    
    st.divider()

    st.subheader("🛠️ Tecnologías Utilizadas: ")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("img/PYTHON.png", caption="Python Core")
    with col2:
        st.image("img/STREAMLIT.png", caption="Streamlit UI")
    with col3:
        st.image("img/PANDAS.png", caption="Pandas & Numpy")
    with col4:
        st.image("img/unnamed.jpg", caption="Matplotlib & Seaborn")
        
    st.divider()
#------------------------------------------------------------------------------------------------------------------------------
if st.session_state.pagina == "🌐: Cargue su dataset":
    st.title("📥 Carga de dataset:")
    st.divider()
    
    st.header("📝 Instrucciones")
    st.write("En este módulo debe cargar el archivo CSV específico para proceder con el análisis de bajas (churn).")
    st.divider()

    documento = st.file_uploader("Ingrese el documento _TelcoCustomerChurn.csv_:", type=["csv"])
    
    if documento is not None:
        if documento.name == "TelcoCustomerChurn.csv":
            st.success("✅ El archivo ha sido ingresado exitosamente. Puede dirigirse al siguiente módulo.")
            st.divider()
            
            if 'df' not in st.session_state:
                st.session_state.df = pd.read_csv(documento)
            
            st.subheader("👀 Vista previa del dataset")
            vis=st.slider("Seleccione el número de filas del 0 al 20 para la vista previa", 0, 20)
            st.write(st.session_state.df.head(vis))
            st.divider()
            st.subheader("📊 Dimensiones del dataset")
            st.write(f"El dataset tiene: **{st.session_state.df.shape[0]}** filas y **{st.session_state.df.shape[1]}** columnas")
            st.session_state.df['TotalCharges'] = pd.to_numeric(st.session_state.df['TotalCharges'], errors='coerce')
            st.session_state.df['SeniorCitizen'] = st.session_state.df['SeniorCitizen'].astype(object)
            st.divider()
        else:
            st.error("❌ El nombre del archivo no es correcto. Debe ser 'TelcoCustomerChurn.csv'")
            st.divider()
#------------------------------------------------------------------------------------------------------------------------------
#FUNCIÓN PERSONALIZADA A USAR EN ITEM 2:

def clasificar_variables(df):
    """
    Función para identificar y contar variables numéricas y categóricas.
    nos devuelve dos listas con los nombres de las columnas.
    """ 
    numericas = df.select_dtypes(include=["number"]).columns.tolist()
    categoricas = df.select_dtypes(include=["object"]).columns.tolist()
    
    return numericas,categoricas

#Requisito (Crear una clase para POO)

class DataAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe
        self.numericas = self.df.select_dtypes(include=["number"]).columns.tolist()
        self.categoricas = self.df.select_dtypes(include=["object"]).columns.tolist()

    def obtener_resumen_estructural(self):
        return pd.DataFrame({
            "Columna": self.df.columns,
            "Tipo de dato": self.df.dtypes.values,
            "Nulos (NaN)": self.df.isnull().sum().values
        })

    def obtener_estadisticas(self, tipo="number"):
        return self.df.describe(include=tipo)

    def plot_distribucion_numerica(self, columna):
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.histplot(self.df[columna], ax=ax, color="skyblue", kde=True)
        ax.set_title(f"Distribución de {columna}")
        return fig


if st.session_state.pagina == "📊: Análisis exploratorio de datos":
    st.title("📊 Análisis exploratorio de datos")
    
    if "df" not in st.session_state:
        st.info("⚠️ Suba el archivo csv en el módulo: 🌐: Cargue su dataset")
    else:
        analyzer = DataAnalyzer(st.session_state.df)
        
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "🏗️ Estructura", "🏷️ Variables", "🧹 Limpieza", "📉 Estadísticas", "🔢 Numéricas", "🔠 Categóricas"])

        with tab1:
            st.header("🏗️ Estructura del dataset")
            # USO DE ST.CHECKBOX (REQUISITO)
            ver_tabla = st.checkbox("Mostrar tabla de resumen estructural", value=True)
            if ver_tabla:
                st.table(analyzer.obtener_resumen_estructural())

        with tab2:
            st.header("🏷️ Identificación de variables")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader(f"🔢 Numéricas ({len(analyzer.numericas)})")
                st.write(pd.DataFrame(analyzer.numericas, columns=["Variable"]))
            with col2:
                st.subheader(f"🔤 Categóricas ({len(analyzer.categoricas)})")
                st.write(pd.DataFrame(analyzer.categoricas, columns=["Variable"]))
        with tab3:
            st.header("🧹 Análisis de valores faltantes")
            st.write("En esta sección se presentan tanto los valores NA como los que están rellenados con ' '")
            nul_antes = st.session_state.df.isnull().sum().values
            vacios_antes = st.session_state.df.apply(lambda x: x.astype(str).str.strip() == "").sum().values
            rows_antes = st.session_state.df.shape[0]
            filas_problema = st.session_state.df[st.session_state.df['TotalCharges'].astype(str).str.strip() == ""]
            
            st.subheader("1. Estado Inicial del Dataset")
            df_info_antes = pd.DataFrame({
            "Columna": st.session_state.df.columns,
            "Tipo de Dato": st.session_state.df.dtypes.values,
            "Nulos (NaN)": nul_antes,
            "Vacíos (' ')": vacios_antes
        })
            
            st.table(df_info_antes)
            
            
            matriz_vacios = st.session_state.df.isnull()
            fig, ax = plt.subplots(figsize=(12, 3))
            sns.heatmap(matriz_vacios, cbar=False, cmap="viridis", ax=ax)
            ax.set_title("Heatmap de Espacios en Blanco y NaNs")
            st.pyplot(fig)
            plt.close(fig)
            st.write("""- Se opta por eliminar los registros cuyos Total Charges sean nulos, debido a que no es posible
                    que el cargo total fuera inexistente cuando si hubo cargos mensuales.
                    """)
            st.write("- Nótese la pequeña linea que existe en TotalCharges que nos impediría trabajar con dicha variable.")
            st.divider()
            
            st.subheader("2. Aplicando Limpieza de Datos")
            st.session_state.df.dropna(subset=['TotalCharges'], inplace=True)
            rows_despues = st.session_state.df.shape[0]
            nulos_est_despues = st.session_state.df.isnull().sum().values
            vacios_cnt_despues = st.session_state.df.apply(lambda x: x.astype(str).str.strip() == "").sum().values
            
            st.subheader("3. Resultado Final (Antes vs Después)")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Filas Iniciales", rows_antes)
                st.metric("Vacíos detectados", len(filas_problema))
            with col2:
                st.metric("Filas Finales", rows_despues)
                st.metric("Vacíos restantes", vacios_cnt_despues.sum())
                df_info_despues = pd.DataFrame({
            "Columna": st.session_state.df.columns,
            "Tipo de Dato": st.session_state.df.dtypes.values,
            "Nulos (NaN)": nulos_est_despues,
            "Vacíos (' ')": vacios_cnt_despues
        })
            st.table(df_info_despues)
        
        with tab4:
            st.header("📉 Estadísticas Descriptivas")
            st.subheader("🔢 Numéricas: ")
            st.write(analyzer.obtener_estadisticas("number"))
            
            st.write("""
                    **💡 Interpretación de métricas críticas:**
                    
                    - **Permanencia:** La media se sitúa en **32 meses**, pero con una desviación estándar elevada (**24**).
                    Esto puede indicar una alta volatilidad en los clientes.
                    
                    - **Monthly Charges:** El cobro promedio es de **64 unidades monetarias**. La amplitud entre el mínimo (\$18.25) y el máximo (\$118).
                    
                    - **Total Charges:** Con una media de **2283**, este valor acumulado confirma que la mayor rentabilidad proviene de clientes a los que se ha prestado el servicio por bastante tiempo.
                    
                    """)
            
            st.subheader("🔤 Categóricas: ")
            st.write(analyzer.obtener_estadisticas("object"))
            
            st.write("""
                    **🧩 Perfil de Usuario (Análisis de Moda):**
                    De acuerdo a las frecuencias más altas, el cliente promedio presenta el siguiente perfil:
                    - **Demografía:** Varón, joven (no senior), sin cargas familiares (ni pareja ni dependientes).
                    - **Conectividad:** Cuenta con servicio telefónico pero sin líneas múltiples; su Internet es de **Fibra Óptica**.
                    - **Contrato:** Predomina el modelo de pago **Mes a Mes** con boleta electrónica.
                    """)
            
        with tab5:
            st.header("📈 Análisis de Distribución de Variables Numéricas")
            st.write("Visualización automática de variables usando la clase `DataAnalyzer`.")
            for col in analyzer.numericas:
                with st.expander(f"🔍 Ver análisis detallado de: {col}"):
                    fig = analyzer.plot_distribucion_numerica(col)
                    st.pyplot(fig)
                    plt.close(fig)
                    stats = analyzer.obtener_estadisticas().loc[:, [col]]
                    st.write(f"Estadísticas de {col}:")
                    st.dataframe(stats.T)
            
            st.write("""
                    **📝 Hallazgos en Distribuciones:**
                    - **Permanencia:**. Las mayores frecuencias están en los extremos (clientes nuevos y muy antiguos). La falta de clientes crítica en el centro de la gráfica sugiere deficiencias en los planes de fidelización de mediano plazo.
                    - **Cargos Mensuales:** Se observa un comportamiento heterogéneo. Aunque muchos clientes prefieren planes básicos (\$20), hay un repunte notable en el rango de \$70 a \$100, coincidente con los servicios de Fibra Óptica.
                    - **Cargos Totales:** La curva descendente confirma que la empresa tiene una gran entrada de clientes, pero muchos abandonan antes de generar un cargo acumulado alto.
                    """)
        
        
        with tab6:
            st.header("🔠 Análisis de variables categóricas")
            columnas_cat = ["gender", "Partner", "Dependents"]
            fig, axes = plt.subplots(1,3, figsize=(12, 10))
            axes = axes.flatten()
            for i, col in enumerate(columnas_cat):
                datos = st.session_state.df[col].value_counts()
                axes[i].pie(datos, labels=datos.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
                axes[i].set_title(f"Distribución de {col}")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)
            
            st.write("""
                    - **Género y Pareja:** La distribución es casi equitativa (**~50%**), indicando que estas variables no sesgan el mercado por sí solas.
                    - **Dependientes:** Es un hallazgo clave que el **70%** de los clientes no tengan dependientes, lo que los hace un segmento más móvil y propenso al cambio de compañía.
                    """)
            
            columnas_cat = ["SeniorCitizen","PhoneService"]
            fig, axes = plt.subplots(1,2, figsize=(12, 10))
            axes = axes.flatten()
            for i, col in enumerate(columnas_cat):
                datos = st.session_state.df[col].value_counts()
                axes[i].pie(datos, labels=datos.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
                axes[i].set_title(f"Distribución de {col}")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)
            
            st.write("""
                    - **Seniority:** Solo el **16%** de los clientes adultos mayores, lo que indica un mercado mayoritariamente joven/adulto.
                    - **Telefonía:** El servicio telefónico es casi universal (**90%**).
                    """)
            
            st.header("📡 Análisis de Servicios Adicionales")
            columnas_cat = ["MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup","DeviceProtection","TechSupport"]
            fig, axes = plt.subplots(2, 3, figsize=(15, 10))
            axes = axes.flatten()
            for i, col in enumerate(columnas_cat):
                datos = st.session_state.df[col].value_counts()
                axes[i].pie(datos, labels=datos.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2"))
                axes[i].set_title(f"Distribución de {col}")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)

            st.write("""
                    - **Infraestructura:** La **Fibra Óptica (44%)** supera al DSL (34.4%), producto principal respecto a internet que ofrece la empresa.
                    - **Servicios de Valor Añadido (SVA):** Existe una baja adopción en seguridad y soporte técnico (**~30%**). La mayoría de los clientes (**50%+**) rechaza estos servicios.
                    """)

            st.subheader("💳 Análisis de Contratos y Pagos")
            columnas_cat1 = ["Contract", "PaymentMethod", "StreamingTV", "StreamingMovies"]
            fig, axes = plt.subplots(1, 2, figsize=(15, 5))
            sns.countplot(data=st.session_state.df, x="Contract", ax=axes[0], palette="viridis")
            axes[0].set_title("Distribución por Tipo de Contrato")
            sns.countplot(data=st.session_state.df, x="PaymentMethod", ax=axes[1], palette="Set3")
            axes[1].set_title("Distribución por Método de Pago")
            plt.xticks(rotation=45) 
        
            st.pyplot(fig)
            plt.close(fig)
            
            st.write("""
                    - **Tipo de contrato:** La predominancia de contratos **'Mes a Mes'** genera una alta exposición al riesgo de fuga.
                    - **Finanzas:** El método de pago preferido es el **Electronic Check**, sugiriendo un cliente digitalizado.
                    """)
            
            st.write("### 📊 Proporciones Detalladas")
            col_selector = st.selectbox("Selecciona una variable para ver su tabla de proporciones:", columnas_cat1)
            conteo = st.session_state.df[col_selector].value_counts()
            proporcion = st.session_state.df[col_selector].value_counts(normalize=True) * 100
            df_resumen = pd.DataFrame({
                "Conteo Absoluto": conteo,
                "Proporción (%)": proporcion.map("{:.2f}%".format)
            })
        
            st.table(df_resumen)
            
        tab7, tab8, tab9, tab10 = st.tabs(["🔗 Bivariado Num","🌓 Bivariado Cat","🧪 Análisis Paramétrico","🏆 Hallazgos Clave"])
        with tab7:
            st.header("🔗 Análisis bivariado: Numérico vs Categórico")
            st.subheader("🌡️ Densidad de Cargos Mensuales por Churn")
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            sns.histplot(data=st.session_state.df, x="MonthlyCharges", hue="Churn", kde=True, element="step", ax=ax2)
            ax2.set_title("Comparación de Densidad: Monthly Charges")
            ax2.set_xlabel("Monto Mensual ($)")
            ax2.set_ylabel("Frecuencia de Clientes")
            st.pyplot(fig2)
            plt.close(fig2)
            
            st.write("""
                    **🔍 Conclusiones del Histograma de Cargos:**
                    - Los clientes leales se concentran en cargos bajos (**<30 unidades monetarias**).
                    - El segmento crítico de deserción se dispara entre los **70 y 100 unidades monetarias**. Los precios altos están directamente relacionados con la fuga.
                    """)
            
            st.subheader("⏳ Permanencia del cliente vs Churn")
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            sns.histplot(data=st.session_state.df, x="tenure", hue="Churn", kde=True, element="step", ax=ax2)
            ax2.set_title("Histograma de Meses de permanencia por abandono")
            ax2.set_xlabel("Meses de permanencia")
            ax2.set_ylabel("Frecuencia de Clientes")
            st.pyplot(fig2)
            plt.close(fig2)
            
            st.write("""
                    **⚠️ Fugas tempranas:** Las fugas son masivas en los primeros **10 meses**. Esto indica la satisfacción inicial es ineficiente para retener al cliente a largo plazo.
                    """)
            
            st.subheader("💰 Cargos Totales según Estado de Churn")
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            sns.histplot(data=st.session_state.df, x="TotalCharges", hue="Churn", kde=True, element="step", ax=ax2)
            ax2.set_title("Cargos anuales acumulados por abandono")
            ax2.set_xlabel("Cargo Total ($)")
            ax2.set_ylabel("Frecuencia de Clientes")
            st.pyplot(fig2)
            plt.close(fig2)
            
            st.write("""
                    La mayoría de las fugas ocurren antes de que el cliente genere un ingreso acumulado significativo, reforzando la idea de que se pierden clientes en etapas tempranas.
                    """)
            
            
        with tab8:
            st.header("🌓 Análisis bivariado: Categórico vs Categórico")
            st.subheader("👵 Seniority vs Churn")
            st.table(pd.crosstab(st.session_state.df["SeniorCitizen"],st.session_state.df["Churn"]))
            st.pyplot(pd.crosstab(st.session_state.df["SeniorCitizen"],st.session_state.df["Churn"]).plot(kind="bar",stacked="True").get_figure())
            st.write("""
                    Aunque los adultos mayores son menos en cantidad, su tasa proporcional de abandono de los servicios es mayor. Sin embargo, el volumen total de fuga proviene de los clientes jóvenes.
                    """)

            st.subheader("🚻 Fuga de clientes por Género")
            st.table(pd.crosstab(st.session_state.df["gender"],st.session_state.df["Churn"]))
            st.pyplot(pd.crosstab(st.session_state.df["gender"],st.session_state.df["Churn"]).plot(kind="bar").get_figure())
            
            st.write("""
                    El género no muestra ser un factor determinante; la deserción se distribuye de manera similar en ambos casos.
                    """)
            st.subheader("👶 Impacto de tener Dependientes")
            st.table(pd.crosstab(st.session_state.df["Dependents"],st.session_state.df["Churn"]))
            st.pyplot(pd.crosstab(st.session_state.df["Dependents"],st.session_state.df["Churn"]).plot(kind="bar").get_figure())
            st.write("""
                    **Dependientes:** Los clientes sin dependientes son los que mayoritariamente abandonan nuestros servicios.
                    """)
            st.subheader("📂 Análisis de Fuga por Contrato e Internet")
    
            variables_interes = ["Contract", "InternetService"]
            fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
            for i, col in enumerate(variables_interes):
                tabla = pd.crosstab(st.session_state.df[col], st.session_state.df["Churn"])
                tabla.plot(kind="bar", stacked=True, ax=axes[i])
                
                axes[i].set_title(f"Fuga por {col}")
                axes[i].set_ylabel("Cantidad de Clientes")
                axes[i].legend(title="Churn")
                st.table(tabla)
            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)
            st.write("""
                    **🚨 Hallazgos Finales:**
                    - El contrato **'Month-to-month'** es uno de los factores principales de fuga.
                    - Los clientes de **Fibra Óptica** se van más que los de DSL.
                    """)
        with tab9:
            st.header("🧪 Explorador Bivariado Dinámico")
        
            columnas = st.session_state.df.columns
            selección = st.multiselect("Seleccione exactamente 2 variables para comparar:", columnas, max_selections=2)
            if len(selección) == 2:
                var1, var2 = selección
            
                st.subheader(f"🔍 Análisis Visual: {var1} vs {var2}")
            
                tabla = pd.crosstab(st.session_state.df[var1], st.session_state.df[var2])
                fig, ax = plt.subplots(figsize=(10, 5))
                tabla.plot(kind="bar", stacked=True, ax=ax, color=sns.color_palette("viridis", n_colors=len(tabla.columns)))
                
                ax.set_title(f"Relación entre {var1} y {var2}")
                ax.set_ylabel("Cantidad de Registros")
                plt.xticks(rotation=45)
                st.pyplot(fig)
                plt.close(fig)
                st.subheader(f"📊 Tabla de contingencia: {var1} vs {var2}")
                st.table(tabla)
            else:
                st.info("💡 Por favor, selecciona 2 variables de la lista para generar la comparación dinámica.")
        with tab10:
            st.header("🏆 Hallazgos Clave e Insights del Negocio")
        

            total_clientes = len(st.session_state.df)
            tasa_churn = (st.session_state.df["Churn"] == "Yes").mean() * 100
        
            col1, col2, col3 = st.columns(3)
            col1.metric("Clientes Totales", total_clientes)
            col2.metric("Tasa de Churn(Abandono)", f"{tasa_churn:.2f}%")
            col3.metric("Impacto Financiero", "Alto ⚠️")
            st.divider()

            st.subheader("🎯 Resumen Crítico: Contrato y Costos")
            st.write("Esta grafico nos ayuda a visualizar la causa raíz: Combinación de contratos inestables y altos cargos mensuales.")
        
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.boxplot(x="Contract", y="MonthlyCharges", hue="Churn", data=st.session_state.df, ax=ax)
            ax.set_title("Boxplot: Contrato, Cargos y Fuga")
            st.pyplot(fig)
            plt.close(fig)
            st.subheader("💡 Insights Derivados del Análisis")
        
            st.info("""
            **1. Factor Contractual:** La inestabilidad del contrato mensual es el riesgo #1. Migrar clientes a planes anuales debe ser la prioridad estratégica.
            """)
        
            st.warning("""
            **2. Techo de Precio:** Entre los **$70 y $90**, los clientes se vuelven extremadamente sensibles al precio. Se requiere revisar la propuesta de valor en Fibra Óptica.
            """)
        
            st.success("""
            **3. Retención Orgánica:** Fomentar planes para parejas o familias (Dependents) ayuda a anclar al cliente y reducir la deserción de forma natural.
            """)
#----------------------------------------------------------------------------------------------------------------------------------------------
if st.session_state.pagina == "📘: Conclusiones y Recomendaciones":
    st.title("📘 Conclusiones orientadas a la toma de desiciones")
    st.divider()
    if 'df' not in st.session_state:
        st.info("⚠️ Suba el archivo csv en el módulo: 🌐: Cargue su dataset")
    else:
        st.header("🏁 Conclusiones Finales")
        st.write("""
    1.  **🚨 Crisis de Fidelidad:** La mayoría de clientes se pierden en el primer año. La empresa falla en consolidar la relación tras la instalación.
            Es crucial que se implementen estrategias de fidelización del cliente con el propósito de mantenerlos durante más tiempo.
    2.  **💸 El costo de la Fibra:** Uno de los factores que se encontró durante el análisis es que se puede encontrar una relación entre el precio de la fibra óptica (70 a 90 unidades monetarias)
        con la fuga de los clientes. Es posible que la competencia ofrezca mejores servicios a un menor precio. Es crucial poder poner a disposición del cliente planes u ofertas que permitan
        que este acceda al servicio,
    3.  **📑 El problema de los contratos:** Otra de las causas de fuga de clientes es el modelo de contrato "mes a mes" que ofrece la empresa. Que el contrato sea tan libre puede ocasionar
    que el cliente observe las ofertas de otras empresas e irse fácilmente.
    4. **👨 El Cliente Solitario**: Los datos muestran que los clientes sin pareja (Partner) y
    sin dependientes (Dependents) tienen una tasa de deserción significativamente mayor.
    Al no tener un núcleo familiar vinculado al servicio, los "costos de cambio" emocionales
    y logísticos son menores, facilitando la fuga.
    5. **🛡️ Baja Adopción de Servicios de Protección:** Existe una relación inversa entre la fuga y la contratación de servicios adicionales como OnlineSecurity
    o TechSupport. La gran mayoría de los clientes que se van no cuentan con estos servicios, lo que sugiere que perciben la oferta de la empresa como un "commodity" reemplazable.
    """)
        st.divider()
        st.header("🚀 Recomendaciones para el Negocio")
        st.success("""
    - **🎁 Programa 'Primer Año':** Implementar bonificaciones escalonadas durante los meses 1-12 para incentivar la permanencia temprana.
    - **📦 Paquetización (Bundling):** Incluir servicios de seguridad y soporte sin costo adicional en planes de Fibra Óptica para aumentar el valor percibido.
    - **💳 Migración Contractual:** Ofrecer un mes gratis a cambio de la transición de contrato mensual a contrato de dos años.
    - **🏠 Creacion de planes familiares:** o beneficios por referidos que incentiven la conexión de más miembros del hogar para
    "anclar" al cliente principal.

    """)