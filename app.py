import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Tablero que convierte tus ideas en una realidad")

with st.sidebar:
    st.subheader("Propiedades del Tablero")
    drawing_mode = st.sidebar.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
    stroke_color = st.color_picker("Color de trazo", "#C8A2C8", key="1")
    bg_color = st.color_picker("Color del fondo", "#000000",key="2")

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=800,
    width=800,
    drawing_mode=drawing_mode,
    key="canvas",
)
