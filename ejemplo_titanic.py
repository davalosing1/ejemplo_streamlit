import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV "database_titanic.csv" en un DataFrame de pandas.
df = pd.read_csv("database_titanic.csv")

# Muestra un título y una descripción en la aplicación Streamlit.
st.write("""
# Mi primera aplicación interactiva
## Gráficos usando la base de datos del Titanic
""")

# Usando la notación "with" para crear una barra lateral en la aplicación Streamlit.
with st.sidebar:
    # Título para la sección de opciones en la barra lateral.
    st.write("# Opciones")
    
    # Crea un control deslizante (slider) que permite al usuario seleccionar un número de bins
    # en el rango de 0 a 10, con un valor predeterminado de 2.
    div = st.slider('Número de bins:', 0, 10, 2)
    
    # Muestra el valor actual del slider en la barra lateral.
    st.write("Bins=", div)

# Desplegamos un histograma con los datos del eje X
fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].hist(df["Age"], bins=div)
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de edades")

# Tomando datos para hombres y contando la cantidad
df_male = df[df["Sex"] == "male"]
cant_male = len(df_male)

# Tomando datos para mujeres y contando la cantidad
df_female = df[df["Sex"] == "female"]
cant_female = len(df_female)

ax[1].bar(["Masculino", "Femenino"], [cant_male, cant_female], color = "red")
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_title('Distribución de hombres y mujeres')

# Desplegamos el gráfico
st.pyplot(fig)

st.write("""
## Muestra de datos cargados
""")
# Graficamos una tabla
st.table(df.head())

# Muestra un título y una descripción en la aplicación Streamlit.
st.write("""
## Porcentaje de Sobrevivientes por Sexo
""")

# ====== Cálculos de porcentajes ======
surv_male = len(df[(df["Sex"] == "male") & (df["Survived"] == 1)])
total_male = len(df[df["Sex"] == "male"])
pct_male = (surv_male / total_male) * 100

surv_female = len(df[(df["Sex"] == "female") & (df["Survived"] == 1)])
total_female = len(df[df["Sex"] == "female"])
pct_female = (surv_female / total_female) * 100

# Datos para el gráfico
sex_labels = ["Hombres", "Mujeres"]
percentages = [pct_male, pct_female]

# Nuevos colores
colors = ["#1F77B4", "#FF7F0E"]

# Crear gráfico
fig, ax = plt.subplots(figsize=(7, 3))

ax.barh(sex_labels, percentages, color=colors)

# Etiquetas y estilo
ax.set_xlabel("Porcentaje de sobrevivientes (%)")
ax.set_xlim(0, 100)

# Mostrar porcentaje en las barras
for i, v in enumerate(percentages):
    ax.text(v + 1, i, f"{v:.1f}%", va="center", fontsize=12)

# Título
ax.set_title("Porcentaje de Sobrevivientes por Sexo")

# Mostrar en Streamlit
st.pyplot(fig)
