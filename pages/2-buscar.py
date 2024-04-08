import streamlit as st
import pandas as pd

# Cargar el archivo de Excel en un DataFrame de pandas
df = pd.read_excel('base/datos.xlsx')

# Crear un campo de texto para el nombre del cliente
nombre_cliente = st.text_input('Nombre del Cliente')

if st.button('Buscar'):
    # Filtrar el DataFrame basado en el nombre del cliente
    resultado = df[df['Nombre del Cliente'] == nombre_cliente]
    
    # Mostrar el resultado
    st.write(resultado)
    
    # Suma del valor total de la deuda
    suma_deuda = resultado['Valor Total de Deuda'].sum()
    st.write(f'Suma del Valor Total de Deuda: {suma_deuda}')

    # Botón de eliminar registro
    for index, row in resultado.iterrows():
        if st.button(f"Eliminar {index}"):
            df.drop(index, inplace=True)
            st.write(f"Registro {index} eliminado.")
