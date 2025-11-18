# app.py
import streamlit as st
# NUEVO: Importamos ImageFilter para las operaciones morfológicas
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import io
import os

# --- Importamos nuestra función de IA ---
if not os.path.exists("models"):
    os.makedirs("models")
if not os.path.exists("models/analysis.py"):
    with open("models/analysis.py", "w") as f:
        f.write("# Archivo de análisis de IA\n")
        f.write("def analizar_con_ia(api_key, o, p): return 'Error: analysis.py está vacío.'\n")

from models.analysis import analizar_con_ia

# --- 1. Configuración de la Página ---
st.set_page_config(layout="wide", page_title="Editor con IA")
st.title("✨ Editor de Imágenes con Análisis de IA")

# --- 2. Sliders y Botones ---
st.sidebar.title("🛠️ Controles de Edición")

st.sidebar.subheader("Modo de Procesamiento")
# NUEVO: Un 'radio' para elegir qué tipo de operación hacer
modo_proceso = st.sidebar.radio(
    "Elige una operación:",
    ("Edición Manual (Sliders)", "Mejora Automática (Ecualizar)", "Operaciones Morfológicas"),
    key="modo_proceso"
)

st.sidebar.divider()

# --- Controles de Edición Manual ---
# MODIFICADO: Se desactivan si no es el modo "Edición Manual"
st.sidebar.subheader("Edición Manual")
brillo = st.sidebar.slider("Brillo", 0.5, 1.5, 1.0, disabled=(modo_proceso != "Edición Manual (Sliders)"))
contraste = st.sidebar.slider("Contraste", 0.5, 1.5, 1.0, disabled=(modo_proceso != "Edición Manual (Sliders)"))
nitidez = st.sidebar.slider("Nitidez", 0.5, 3.0, 1.0, disabled=(modo_proceso != "Edición Manual (Sliders)"))

# --- NUEVO: Controles Morfológicos ---
# MODIFICADO: Se desactivan si no es el modo "Morfológicas"
st.sidebar.subheader("Operaciones Morfológicas")
# Usamos un 'select' para elegir la operación
filtro_morfologico = st.sidebar.selectbox(
    "Filtro:",
    ("Ninguno", "Erosión (MinFilter)", "Dilatación (MaxFilter)", "Detectar Bordes (Find Edges)"),
    disabled=(modo_proceso != "Operaciones Morfológicas")
)

# --- 3. Carga de la Imagen ---
uploaded_file = st.file_uploader("Sube tu imagen aquí:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    original_image = Image.open(uploaded_file).convert("RGB") 

    # --- 4. Procesamiento (Lógica MODIFICADA) ---
    
    st.header("Comparación de Resultados")
    
    if modo_proceso == "Edición Manual (Sliders)":
        img = original_image
        img = ImageEnhance.Brightness(img).enhance(brillo)
        img = ImageEnhance.Contrast(img).enhance(contraste)
        img = ImageEnhance.Sharpness(img).enhance(nitidez)
        processed_image = img
        caption = "Imagen Procesada (Manual)"

    elif modo_proceso == "Mejora Automática (Ecualizar)":
        img_gray = original_image.convert('L')
        img_equalized = ImageOps.equalize(img_gray)
        processed_image = img_equalized.convert('RGB')
        caption = "Imagen Procesada (Ecualizada)"

    elif modo_proceso == "Operaciones Morfológicas":
        if filtro_morfologico == "Erosión (MinFilter)":
            # MinFilter "erosiona" las áreas brillantes
            processed_image = original_image.filter(ImageFilter.MinFilter(3))
            caption = "Imagen Procesada (Erosión)"
        elif filtro_morfologico == "Dilatación (MaxFilter)":
            # MaxFilter "dilata" las áreas brillantes
            processed_image = original_image.filter(ImageFilter.MaxFilter(3))
            caption = "Imagen Procesada (Dilatación)"
        elif filtro_morfologico == "Detectar Bordes (Find Edges)":
            # Bonus: Un filtro de realce que encuentra bordes
            processed_image = original_image.filter(ImageFilter.FIND_EDGES)
            caption = "Imagen Procesada (Detección de Bordes)"
        else:
            processed_image = original_image # Si es "Ninguno"
            caption = "Imagen Procesada (Sin filtro)"
    
    else:
        processed_image = original_image # Por si acaso
        caption = "Imagen Procesada"


    # --- 5. Mostrar Resultados ---
    col1, col2 = st.columns(2)
    with col1:
        st.image(original_image, caption="Imagen Original", use_container_width=True)
    with col2:
        st.image(processed_image, caption=caption, use_container_width=True)

    # --- 6. Análisis de IA (Nivel 3) ---
    st.sidebar.divider()
    if st.sidebar.button("🤖 Analizar cambios con IA"):
        try:
            api_key = st.secrets["GOOGLE_API_KEY"]
            if not api_key or "tu_clave" in api_key:
                st.error("Por favor, añade tu GOOGLE_API_KEY al archivo .streamlit/secrets.toml")
                st.stop()
        except:
            st.error("No se encontró el archivo .streamlit/secrets.toml o la clave GOOGLE_API_KEY.")
            st.stop()
        
        with st.spinner("🤖 La IA está comparando tus imágenes..."):
            analisis = analizar_con_ia(api_key, original_image, processed_image)
            
            if analisis:
                st.subheader("Análisis de la IA (Gemini)")
                st.markdown(analisis)
    
    # --- 7. Descarga ---
    # (No hay cambios en esta sección)
    st.header("Descarga")
    buf = io.BytesIO()
    processed_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Descargar Imagen Procesada",
        data=byte_im,
        file_name=f"procesada_{uploaded_file.name}",
        mime="image/png"
    )

else:
    st.info("Sube una imagen para empezar a editar.")