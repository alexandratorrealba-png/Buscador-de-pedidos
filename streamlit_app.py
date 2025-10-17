import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Buscador de Pedidos')

# Carga los datos desde el archivo de Excel
# El archivo de Excel debe estar en la misma carpeta que este script
try:
    df = pd.read_excel('pedidos.xlsx')
except FileNotFoundError:
    st.error('Error: No se encontró el archivo "pedidos.xlsx". Asegúrate de que está en el repositorio.')
    df = pd.DataFrame() # Crea un DataFrame vacío para evitar errores

# Si se cargaron los datos, muestra el buscador
if not df.empty:
    # Crea un campo de texto para la búsqueda
    search_term = st.text_input('Ingresa un término de búsqueda (ej. número de orden, nombre, RUT)', '')

    # Filtra el DataFrame si hay un término de búsqueda
    if search_term:
        # Convierte todas las columnas a tipo string para buscar en ellas
        df_str = df.astype(str)
        # Busca en todas las columnas que contengan el término de búsqueda (sin importar mayúsculas/minúsculas)
        filtered_df = df_str[df_str.apply(lambda row: row.str.contains(search_term, case=False)).any(axis=1)]

        # Muestra los resultados si hay coincidencias
        if not filtered_df.empty:
            st.write('### Resultados de la búsqueda:')
            st.dataframe(filtered_df)
        else:
            st.warning('No se encontraron resultados para su búsqueda.')
    else:
        # Si no hay término de búsqueda, muestra toda la tabla
        st.write('### Historial completo de pedidos:')
        st.dataframe(df)

