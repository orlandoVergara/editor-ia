RetroLens AI – Restauración Inteligente de Fotos Familiares
1. Descripción del Problema y Caso de Uso
🔍 El Desafío

La digitalización de fotos familiares presenta un problema recurrente: con el paso del tiempo, las imágenes físicas se degradan —pierden contraste, se vuelven opacas o aparecen velos blanquecinos— y los escáneres caseros no logran rescatar la esencia original.

Las soluciones actuales obligan al usuario a elegir entre:

Software profesional (Photoshop): potente pero costoso, complejo y con demasiadas herramientas.

Filtros automáticos de celular: resultados impredecibles y poco fieles a la foto original.

✅ La Solución

RetroLens AI ofrece un equilibrio ideal:
herramientas de mejora visual simples (brillo, contraste, nitidez, ecualización), acompañadas por un Asistente de IA que evalúa objetivamente si la calidad mejora o empeora.

El usuario edita.
La IA asesora.
Sin complicación. Sin incertidumbre.

2. User Persona

👤 Nombre: Laura
Rol: “Digitalizadora del Archivo Familiar”
Edad: 45–55
Ocupación: Fotógrafa amateur

Contexto Tecnológico

Usa su computadora para tareas cotidianas.

No tiene conocimientos de IA ni quiere aprender software complejo.

Problemas Principales

Cientos de fotos escaneadas con mala calidad.

Incertidumbre sobre si sus ajustes mejoran la imagen.

Frustración al probar apps poco consistentes.

Objetivos

Mejorar grandes lotes de fotos los fines de semana.

Ver rápidamente si vale la pena editar cada imagen.

Dominar el flujo de trabajo en 1-2 tardes.

3. Arquitectura del Sistema

La aplicación utiliza una arquitectura monolítica simple con Streamlit manejando UI y lógica.

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

Framework: Streamlit

Procesamiento de imágenes: Pillow (PIL)

IA: Google Gemini 1.5 Flash

Entorno: Python 3.11

Privacidad: Todo el procesamiento es local, excepto el análisis IA.

5. Instrucciones de Instalación
1️⃣ Clonar el repositorio
git clone https://github.com/tu-usuario/retrolens-ai.git
cd retrolens-ai

2️⃣ Crear entorno virtual
python -m venv .venv
.\.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Mac / Linux

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Configurar la API Key

Crear la carpeta:

.streamlit/


Crear el archivo:

.streamlit/secrets.toml


Agregar:

GOOGLE_API_KEY = "tu_clave_de_google_ai_studio"

5️⃣ Ejecutar la aplicación
streamlit run app.py

6. Ejemplos de Uso
📸 Caso A — Foto "Lavada" de 1982

Laura sube una foto grisácea y sin contraste.
Activa Ecualización de Histograma.

➡️ La imagen recupera contraste y profundidad.

(Inserta aquí captura de “Mejora Automática” activada)

🛠 Caso B — Ajuste Fino + Validación IA

Ajusta Nitidez (1.8) y Contraste (1.2).
Presiona "Analizar con IA".

Respuesta típica de Gemini:

"La nitidez ha mejorado los bordes de los rostros.
El contraste es adecuado sin perder detalles en sombras."

(Inserta aquí captura con sliders + resultado IA)

7. Decisiones de Diseño (Human–AI Interaction)
✔ Transparencia

La IA no actúa sola.
El botón “Analizar con IA” permite a la usuaria decidir cuándo usarla.

✔ Reversibilidad

Los efectos no son destructivos.
Los cambios pueden activarse/desactivarse fácilmente.

✔ Lenguaje Natural

Gemini brinda feedback simple y comprensible
("Se ve más nítida", "está muy oscura") evitando métricas técnicas.

8. Limitaciones Conocidas

El análisis con IA requiere conexión a internet.

La calidad del escaneo original afecta el resultado final.

No está orientado a restauración profesional avanzada.
