# RetroLens AI – Restauración Inteligente de Fotos Familiares

## 1. Descripción del Problema y Caso de Uso

### 🔍 El Desafío  
La digitalización de fotos familiares presenta un problema recurrente:  
con el paso del tiempo, las imágenes físicas se degradan —pierden contraste, se vuelven opacas o aparecen velos blanquecinos— y los escáneres caseros no logran rescatar la esencia original.

Las soluciones actuales obligan al usuario a elegir entre:

- **Software profesional (Photoshop):** potente pero costoso, complejo y con cientos de herramientas innecesarias.  
- **Filtros automáticos de celular:** resultados poco predecibles; alteran rostros o colores originales.

### ✅ La Solución  
RetroLens AI ofrece un punto medio perfecto:  
herramientas de mejora visual simples (brillo, contraste, nitidez, ecualización) junto con un **Asistente de IA** que analiza objetivamente si la calidad mejoró o empeoró.

El usuario edita, la IA asesora. Sin incertidumbre. Sin complejidad.

---

## 2. User Persona

**👤 Nombre:** Laura  
**Rol:** “Digitalizadora del Archivo Familiar”  
**Edad:** 45–55  
**Ocupación:** Fotógrafa amateur

### Contexto Tecnológico  
- Usa la PC para tareas cotidianas.  
- No conoce IA ni quiere aprender software complejo.  

### Sus Problemas  
- Tiene cientos de fotos escaneadas de los años 70–80 con mala calidad.  
- No sabe si sus ajustes mejoran realmente la imagen.  
- Se frustra probando aplicaciones que no son consistentes.

### Objetivos  
- Mejorar un lote grande de fotos durante su fin de semana.  
- Ver rápidamente si vale la pena mejorar cada foto.  
- Usar una herramienta simple y entendible en pocas horas.

---

## 3. Arquitectura del Sistema

La aplicación funciona bajo una arquitectura monolítica ligera usando **Streamlit** tanto para UI como para lógica.

```mermaid
graph TD
    User((Usuario: Laura)) -->|Carga Foto Escaneada| UI[Frontend Streamlit]
    
    subgraph "Núcleo de Procesamiento"
        UI -->|Selección: Mejora Automática| Equalizer[ImageOps: Ecualización Histograma]
        UI -->|Selección: Manual| Sliders[Pillow: Brillo/Contraste/Nitidez]
        UI -->|Selección: Morfología| Morph[Filtros: Erosión/Dilatación]
    end
    
    subgraph "Módulo de Inteligencia"
        UI -.->|Botón: Analizar| GenAI[Google Gemini 1.5 Flash]
        GenAI -->|Feedback de Calidad| UI
    end
    
    Equalizer --> Render[Imagen Final]
    Sliders --> Render
    Morph --> Render
    Render -->|Descarga PNG| User
4. Stack Tecnológico
Frontend & Backend: Streamlit

Procesamiento de Imágenes: Pillow (PIL)

IA Multimodal: Google Gemini 1.5 Flash

Entorno: Python 3.11

Privacidad: Todo el procesamiento visual ocurre localmente. Solo el análisis se envía a la nube.

5. Instrucciones de Instalación
1️⃣ Clonar el repositorio
bash
Copiar código
git clone https://github.com/tu-usuario/retrolens-ai.git
cd retrolens-ai
2️⃣ Crear entorno virtual
bash
Copiar código
python -m venv .venv
.\.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Mac / Linux
3️⃣ Instalar dependencias
bash
Copiar código
pip install -r requirements.txt
4️⃣ Configurar API Key
Crear carpeta:

Copiar código
.streamlit/
Crear archivo:

bash
Copiar código
.streamlit/secrets.toml
Contenido:

toml
Copiar código
GOOGLE_API_KEY = "tu_clave_de_google_ai_studio"
5️⃣ Ejecutar la app
bash
Copiar código
streamlit run app.py
6. Ejemplos de Uso
📸 Caso A — Foto "Lavada" de 1982
Laura sube una foto grisácea y sin contraste.
Activa Ecualización de Histograma.

➡️ La imagen recupera negros profundos y contraste.

Aquí puedes colocar tu captura de la opción “Mejora Automática” activada.

🛠 Caso B — Ajuste Fino + Validación IA
Ajusta Nitidez (1.8) y Contraste (1.2).
Presiona "Analizar cambios con IA".

Gemini responde:

“La nitidez ha mejorado los bordes de los rostros. El contraste es adecuado sin perder detalles en sombras.”

Aquí puedes insertar la captura con sliders + mensaje IA.

7. Decisiones de Diseño (Human-AI Interaction)
Para que Laura tenga una experiencia fluida, se tomaron decisiones clave:

✔ Transparencia
La IA no es automática.
El botón dice “Analizar con IA” para que el usuario decida cuándo usarla.

✔ Reversibilidad
Las funciones no destruyen la imagen.
Los cambios pueden activarse o desactivarse con checkboxes.

✔ Lenguaje Natural
Gemini describe mejoras de forma comprensible:
"Se ve más nítida", "está muy oscura", etc.

Nada de métricas técnicas confusas.

8. Limitaciones Conocidas
La función de análisis con IA requiere conexión a Internet.

La calidad del escaneo inicial limita los resultados finales.

No se recomienda para restauraciones profesionales o muy avanzadas.
