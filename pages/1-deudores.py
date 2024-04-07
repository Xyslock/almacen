import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import openpyxl

# Leer el archivo de Excel si existe, si no, crear un dataframe vacío
try:
    data = pd.read_excel('base/datos.xlsx')
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Error al leer el archivo de Excel. Asegúrate de que 'datos.xlsx' es un archivo de Excel válido.")
except FileNotFoundError:
    data = pd.DataFrame(columns=['Nombre del Cliente', 'Producto', 'Fecha de Compra', 'Valor del Producto', 'Valor Abonado', 'Fecha de Abono', 'Valor Restante', 'Valor Total de Deuda'])

# Crear el formulario
with st.form(key='my_form'):
    nombre_del_cliente = st.text_input(label='Nombre del Cliente')
    producto = st.text_input(label='Producto')
    valor_del_producto = st.number_input(label='Valor del Producto')
    valor_abonado = st.number_input(label='Valor Abonado')

    submit_button = st.form_submit_button(label='Guardar')

# Si el botón de guardar es presionado, añadir los datos al dataframe
if submit_button:
    fecha_de_compra = datetime.today().strftime('%Y-%m-%d')
    fecha_de_abono = datetime.today().strftime('%Y-%m-%d')
    valor_restante = valor_del_producto - valor_abonado
    new_row = {'Nombre del Cliente':nombre_del_cliente, 'Producto':producto, 'Fecha de Compra':fecha_de_compra, 'Valor del Producto':valor_del_producto, 'Valor Abonado':valor_abonado, 'Fecha de Abono':fecha_de_abono, 'Valor Restante':valor_restante}
    data = pd.concat([data, pd.DataFrame(new_row, index=[0])], ignore_index=True)


    # Calcular el valor total de la deuda para cada cliente
    data['Valor Total de Deuda'] = data.groupby('Nombre del Cliente')['Valor Restante'].transform('sum')

    # Guardar el dataframe en un archivo de Excel
    data.to_excel('base/datos.xlsx', index=False)

    # Si el valor total de la deuda es 0, eliminar los registros de ese cliente
    data = data[data['Valor Total de Deuda'] != 0]

    # Actualizar la aplicación para reflejar los cambios en el archivo de Excel
    st.experimental_rerun()
