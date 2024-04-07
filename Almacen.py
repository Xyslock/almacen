import streamlit as st
from PIL import Image

# Cargar la imagen
image_path = "img/babsy_bunny.jpg"
image = Image.open(image_path)

# Configurar la página
st.set_page_config(
    page_title="Presentación LooneyToons",
    page_icon="🐰",
    layout="wide",
)

# Título y descripción
st.title("¡Bienvenidos a LooneyToons!")
st.markdown("## Descubre el mundo mágico de los personajes más traviesos y divertidos.")

# Mostrar la imagen
st.image(image, caption="Babsy Bunny", use_column_width=True)

# Información adicional
st.markdown(
    """
    ### Acerca de Babsy Bunny
    Babsy Bunny es una de las adorables protagonistas de la serie animada **Tiny Toon Adventures**. 
    Su personalidad alegre y su ingenio la convierten en una compañera inolvidable en las aventuras de LooneyToons.
    """
)

# Pie de página
st.markdown("---")
st.markdown("© 2024 LooneyToons. Todos los derechos reservados.")

