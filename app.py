import streamlit as st

# Título de la aplicación
st.title('Mi Primera Aplicación en Streamlit')
#st.header('Autor: Jeferson Parrales')
#st.subheader('Maestría: Inteligencia Artificial y Ciencia de Datos')
#st.subheader('Materia: Paradigmas de Programación para Inteligencia Artificial y Análisis de Datos')

# Nombres y Apellidos
name = st.text_input('Nombres y Apellidos')

# Input Box para Edad
age = st.number_input('Edad', min_value=0, max_value=100, step=1)

# Slider para Seleccionar Mes
month = st.slider('Selecciona un Mes', min_value=1, max_value=12)

# Checkbox para aceptar términos
accept_terms = st.checkbox('Acepto los Términos y Condiciones')

# Radio Buttons para Género
gender = st.radio('Selecciona tu Género', ('Masculino', 'Femenino', 'Otro'))

# Selectbox para País
country = st.selectbox('Selecciona tu País', ['Argentina', 'Chile', 'Perú', 'México', 'Colombia'])

# File Uploader
uploaded_file = st.file_uploader('Cargar un Archivo')

# Selector de Fecha
selected_date = st.date_input('Selecciona una Fecha')

# Selector de Hora
selected_time = st.time_input('Selecciona una Hora')

# Sidebar
st.sidebar.title('Barra Lateral')
st.sidebar.write('Configura algunos elementos aquí:')
st.sidebar.number_input('Edad', min_value=0, max_value=100, step=1, key='sidebar_age')
st.sidebar.slider('Selecciona un Mes', min_value=1, max_value=12, key='sidebar_month')
st.sidebar.selectbox('Selecciona tu País', ['Argentina', 'Chile', 'Perú', 'México', 'Colombia'], key='sidebar_country')

# Botón para enviar información
if st.button('Enviar Información'):
    st.write(f'Gracias, {name}, por enviar tu información.')