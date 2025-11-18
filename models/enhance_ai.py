import google.generativeai as genai
import base64
from io import BytesIO
from PIL import Image, ImageEnhance, ImageFilter

def pil_to_base64(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("utf-8")

def base64_to_pil(b64):
    try:
        binary = base64.b64decode(b64)
        return Image.open(BytesIO(binary)).convert("RGB")
    except Exception as e:
        print("❌ Error al decodificar base64:", e)
        return None


def enhance_locally(img):
    img = ImageEnhance.Sharpness(img).enhance(1.3)
    img = ImageEnhance.Contrast(img).enhance(1.15)
    img = ImageEnhance.Color(img).enhance(1.05)
    img = img.filter(ImageFilter.DETAIL)
    return img


def enhance_with_ai(api_key, image):
    genai.configure(api_key=api_key)

    # Modelo válido para enhancement
    model = genai.GenerativeModel("gemini-1.5-flash")

    img_pre = enhance_locally(image)
    img_b64 = pil_to_base64(img_pre)

    prompt = """
    Mejora esta imagen de forma natural: nitidez, color, contraste, claridad.
    No alteres la escena ni agregues objetos.
    Devuelve la imagen final como base64 PNG.
    """

    response = model.generate_content(
        [
            {"text": prompt},
            {
                "mime_type": "image/png",
                "data": img_b64
            }
        ]
    )

    # Buscar base64 en los parts
    output_b64 = None

    try:
        for cand in response.candidates:
            for part in cand.content.parts:
                # Gemini suele devolver texto con el base64 adentro
                if hasattr(part, "text") and "base64" in part.text.lower():
                    cleaned = (
                        part.text
                        .replace("data:image/png;base64,", "")
                        .replace("```", "")
                        .replace(" ", "")
                        .strip()
                    )
                    output_b64 = cleaned

                # O imagen directa
                if hasattr(part, "inline_data"):
                    output_b64 = part.inline_data.data

    except Exception as e:
        print("❌ Error parseando respuesta:", e)

    if not output_b64:
        print("⚠ Respuesta cruda de la IA:", response)
        return None

    final_img = base64_to_pil(output_b64)
    return final_img
