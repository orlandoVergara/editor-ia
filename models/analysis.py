import streamlit as st
import google.generativeai as genai
import base64
from io import BytesIO

def pil_to_base64(img):
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

@st.cache_data
def analizar_con_ia(api_key, original_img, processed_img):
    """
    Compara la imagen original con la procesada usando Gemini.
    """

    try:
        genai.configure(api_key=api_key)

        # Modelo correcto (antes fallaba)
        model = genai.GenerativeModel("models/gemini-2.0-flash-001")


        # Convertimos las imágenes a base64
        original_b64 = pil_to_base64(original_img)
        processed_b64 = pil_to_base64(processed_img)

        prompt = """
        Eres un experto en análisis fotográfico.
        Compara la IMAGEN ORIGINAL con la IMAGEN PROCESADA.

        Mi objetivo era mejorar la imagen. Basándote en los cambios:
        1. Describe brevemente qué se modificó.
        2. Indica si la imagen procesada es una mejora objetiva.

        Responde en máximo 3 frases.
        """

        # Formato correcto para imágenes + texto
        parts = [
            {"text": prompt},
            {"text": "IMAGEN ORIGINAL:"},
            {"inline_data": {"mime_type": "image/png", "data": original_b64}},
            {"text": "IMAGEN PROCESADA:"},
            {"inline_data": {"mime_type": "image/png", "data": processed_b64}},
        ]

        response = model.generate_content(parts)

        return response.text

    except Exception as e:
        st.error(f"Error al contactar a la IA: {str(e)}")
        return None
