import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Buscador", layout="centered")

# Título de la aplicación
st.title("Buscador de Información")

# Entrada del usuario
query = st.text_input("Introduce tu término de búsqueda:")

# Datos de ejemplo
data = [
    "Streamlit es una herramienta para crear aplicaciones web interactivas",
    "Puedes usar Streamlit para visualizaciones de datos",
    "El buscador permite filtrar información rápidamente",
    "Aprender Python es esencial para proyectos como este",
]

# Buscar resultados
if query:
    results = [item for item in data if query.lower() in item.lower()]
    if results:
        st.subheader("Resultados encontrados:")
        for result in results:
            st.write("- " + result)
    else:
        st.write("No se encontraron resultados.")