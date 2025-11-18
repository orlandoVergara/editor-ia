#1. Descripción del Problema y Caso de Uso
El Desafío
La digitalización de archivos familiares presenta un problema común: el paso del tiempo degrada las fotografías físicas (pérdida de contraste, colores apagados, "neblina" blanca), y los escáneres caseros a menudo no logran capturar la vivacidad original.

Las soluciones existentes obligan al usuario a elegir entre:

Software profesional (Photoshop): Curvas de aprendizaje empinadas, costos altos y cientos de herramientas innecesarias.

Filtros automáticos de celular: Resultados "caja negra" que a menudo alteran los rostros o la esencia de la foto original.

La Solución
Esta aplicación ofrece un término medio perfecto: herramientas de corrección visual directas (brillo, contraste, ecualización) potenciadas por un "Asistente de IA". El usuario edita, y la IA confirma si la calidad técnica ha mejorado objetivamente, eliminando la incertidumbre del proceso.

2. Definición del User Persona
Nombre: Laura Perfil: La "Digitalizadora del Archivo Familiar" Edad: 45-55 años | Ocupación: Fotógrafa amateur

Contexto Tecnológico: Laura utiliza su computadora regularmente para tareas cotidianas y aplicaciones básicas. No tiene experiencia técnica en Inteligencia Artificial ni paciencia para aprender software de edición complejo.

El Problema: Posee cientos de fotos familiares de los años 70 y 80 que ha escaneado, pero el resultado digital es decepcionante: las imágenes se ven opacas, con poco contraste y pixeladas. Quiere compartirlas en redes sociales con su familia, pero siente que la calidad actual "se ve mal".

Frustraciones Principales:

Complejidad: Las herramientas profesionales tienen demasiados botones o requieren suscripciones caras.

Incertidumbre: Al editar, no sabe si el resultado que obtiene es "lo mejor posible" o si está dañando la foto.

Tiempo: El proceso de probar apps en el celular foto por foto es lento e inconsistente.

Objetivos:

Mejorar un lote de 200+ fotos de manera eficiente durante sus fines de semana en casa.

Ver una diferencia clara y rápida (entender si vale la pena el esfuerzo).

Un flujo de trabajo simple que pueda dominar en una o dos tardes.

3. Arquitectura del Sistema
El sistema utiliza una arquitectura monolítica ligera, donde Streamlit gestiona tanto la interfaz de usuario como la lógica de procesamiento en Python.

Fragmento de código

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
Framework: Streamlit (Desarrollo rápido de UI/UX).

Procesamiento de Imagen: Pillow (PIL) (Librería estándar de Python para manipulación de rasters).

Se utiliza para todas las transformaciones de píxeles, asegurando velocidad y privacidad (el procesamiento de imagen es local).

Inteligencia Artificial: Google Generative AI (Gemini 1.5 Flash).

Modelo multimodal utilizado para "Visión por Computadora" semántica. Entiende el contenido de la foto y juzga la calidad.

Entorno: Python 3.11 gestionado con pip.

5. Instrucciones de Instalación
Clonar el repositorio:

Bash

git clone https://github.com/tu-usuario/retrolens-ai.git
cd retrolens-ai
Configurar entorno virtual:

Bash

python -m venv .venv
.\.venv\Scripts\Activate  # En Windows
# source .venv/bin/activate  # En Mac/Linux
Instalar dependencias:

Bash

pip install -r requirements.txt
Configurar API Key (Esencial):

Crea una carpeta .streamlit en la raíz.

Crea un archivo secrets.toml dentro.

Añade: GOOGLE_API_KEY = "tu_clave_de_google_ai_studio"

Ejecutar:

Bash

streamlit run app.py
6. Ejemplos de Uso
Caso A: La Foto "Lavada" de 1982
Laura sube una foto de un cumpleaños que se ve grisácea por el paso del tiempo.

Acción: Activa la casilla "Ecualización de Histograma".

Resultado: La foto recupera instantáneamente los negros profundos y el contraste.

Captura:

[INSERTA AQUÍ TU CAPTURA DE LA OPCIÓN "MEJORA AUTOMÁTICA" ACTIVADA]

Caso B: Ajuste Fino y Validación
Laura ajusta manualmente una foto que estaba un poco borrosa.

Acción: Sube Nitidez a 1.8 y Contraste a 1.2. Presiona "Analizar cambios con IA".

Resultado Gemini: "La nitidez ha mejorado significativamente los bordes de los rostros. El contraste es adecuado sin perder detalles en las sombras."

Captura:

[INSERTA AQUÍ TU CAPTURA DE LOS SLIDERS Y EL MENSAJE DE LA IA]

7. Decisiones de Diseño (Human-AI Interaction)
Para satisfacer a nuestro user persona (Laura), tomamos decisiones específicas de diseño HAI:

Transparencia del Modelo: No ocultamos la IA. El botón dice explícitamente "Analizar con IA" y se activa bajo demanda. Esto respeta el tiempo y los tokens de la usuaria, evitando llamadas innecesarias mientras ella solo está "jugando" con los sliders.

Reversibilidad: La implementación de "Mejora Automática" como un checkbox (casilla) en lugar de un botón destructivo permite a Laura ver el "antes y después" instantáneamente simplemente marcando y desmarcando, dándole sensación de control total.

Feedback Semántico: En lugar de mostrar métricas técnicas (ej: "SNR: 14db"), le pedimos a Gemini que responda en lenguaje natural ("Se ve mejor", "Está muy oscura"), alineándose con el conocimiento no-técnico de Laura.

8. Limitaciones Conocidas
Dependencia de la Nube: La función de análisis requiere conexión a internet para consultar la API de Google.

Tamaño de Archivo: Imágenes superiores a 10MB pueden experimentar lentitud en la carga inicial debido a las limitaciones de Streamlit Cloud.

Formatos RAW: La aplicación está optimizada para JPG y PNG comprimidos (escaneos estándar), no soporta revelado de archivos RAW de cámaras profesionales.
