import streamlit as st
import pandas as pd

# Cargar el archivo de Excel en un DataFrame de pandas
df = pd.read_excel('base/datos.xlsx')

# Crear un campo de texto para el nombre del cliente
nombre_cliente = st.text_input('Nombre del Cliente')

if st.button('Buscar'):
    # Filtrar el DataFrame basado en el nombre del cliente
    resultado = df[df['Nombre del Cliente'] == nombre_cliente]
    
    # Imprimir el DataFrame resultado
    print(resultado)
    
    # Mostrar el resultado
    st.write(resultado)
