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
    
    # Tomar el último registro para cada nombre de cliente
    ultimo_registro_por_cliente = resultado.groupby('Nombre del Cliente').last()
    
    # Calcular la suma de la deuda para el cliente seleccionado
    total_deuda = ultimo_registro_por_cliente['Valor Total de Deuda'].sum()  
      
    # Mostrar el total de la deuda como label en la parte superior
    st.subheader(f"Total de Deuda para {nombre_cliente}: ${total_deuda:.2f}")
