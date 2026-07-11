# Instrucciones de Desarrollo: Agente de IA Corporativo (Alura Agente)

Este documento contiene las directrices técnicas estructuradas para guiar el desarrollo de la aplicación utilizando **GitHub Copilot** como asistente de programación.

---

## 1. Stack Tecnológico Recomendado

El desarrollo debe estructurarse utilizando el siguiente ecosistema de herramientas:

- **Lenguaje Base:** **Python 3.12** como lenguaje principal de programación [45].
- **Orquestación de IA:** **LangChain** como framework central para estructurar el pipeline de RAG y la lógica de toma de decisiones del agente [45].
- **Procesamiento de Documentos:**
  - **PyPDF** para la lectura y procesamiento de archivos PDF nativos [45].
  - **Pandas** para la carga, limpieza y parsing de bases de datos o archivos estructurados (como CSV) [45].
- **Modelos de Lenguaje y Embeddings:**
  - Soporte integrado para modelos líderes de la industria como **Gemma, ChatGPT, o Cohere** [45].
  - El modelo de _embeddings_ debe ser estrictamente consistente tanto en la fase de indexación de documentos como en la conversión de preguntas de los colaboradores [21].
- **Base de Datos Vectorial:**
  - Implementación de índices locales o administrados usando **Chroma, Qdrant, Pinecone, Weaviate o pgvector (PostgreSQL)** [21].
  - Uso de algoritmos de indexación eficiente como **HNSW (Hierarchical Navigable Small World)** para búsquedas rápidas por similitud semántica [21].

---

## 2. Reglas Estrictas de Desarrollo

Para garantizar que la solución sea empresarial, robusta y confiable, GitHub Copilot debe seguir de manera estricta las siguientes reglas:

### A. Prevención Absoluta de Alucinaciones

- **Generación de Respuestas:** El LLM debe ser instruido de manera explícita (system prompting) para responder **únicamente** utilizando los fragmentos de contexto recuperados de los documentos corporativos oficiales [27, 28].
- **Política de Fallback:** Si la consulta del colaborador no puede responderse con el contexto disponible, el agente debe declarar explícitamente: _"No encontré esta información en los documentos disponibles"_ [29]. Queda terminantemente prohibido usar conocimiento externo del modelo para inventar datos o políticas corporativas [27].
- **Trazabilidad y Citación:** Cada respuesta generada debe adjuntar obligatoriamente sus metadatos de procedencia: nombre del archivo de origen, sección, página y/o fecha de actualización [27, 28].
- **Umbral de Confianza:** Implementar un umbral de puntuación mínima (threshold) para la búsqueda semántica [28]. Si el coeficiente de similitud de los fragmentos recuperados no supera este valor, el pipeline debe omitir el envío de datos al LLM y saltar directamente al flujo de fallback [28].

### B. Modularidad del Código (Pipeline RAG)

El código debe estar separado en módulos acoplados de forma débil y cohesivos:

1.  **Módulo de Ingesta:** Limpieza de marcas técnicas (HTML, Markdown) y conversión de datos tabulares (JSON, CSV, Excel) en frases o estructuras legibles antes de la generación del vector [16, 17].
2.  **Módulo de Chunking:** Fragmentación inteligente del texto en bloques (de 500 a 1000 caracteres) con superposición (_overlap_) o estructuración lógica para preservar la coherencia contextual [18].
3.  **Módulo de Indexación:** Envío de vectores de embeddings e inserción de metadatos asociados para permitir filtros específicos previos a la búsqueda semántica [21, 24].
4.  **Módulo de Recuperación y Reranking:** Configuración de búsqueda semántica combinada con reclasificación avanzada (_reranker_) para filtrar y priorizar únicamente los 3 a 5 fragmentos más útiles para armar el contexto [25].

### C. Registro y Logging Claro

Para garantizar la trazabilidad de cada interacción, el agente debe registrar todas las ejecuciones bajo un estándar estructurado:

- **Ejecución Local:** Grabar de manera asíncrona un archivo de registro en formato **JSON Lines** que contenga de forma obligatoria los siguientes campos para cada consulta:
  - `pregunta` del colaborador.
  - `contexto_recuperado` (fragmentos utilizados y metadatos).
  - `respuesta_generada`.
  - `timestamp` (marca de tiempo exacta).
  - `tiempo_de_respuesta` (latencia total en segundos) [37].
- **Ejecución en Nube (OCI):** Estructurar el logging de tal forma que pueda ser centralizado y canalizado hacia herramientas de monitoreo en producción, garantizando la auditoría de cada decisión tomada por la IA [38, 39].

---

## 3. Objetivo Final de Despliegue en la Nube (OCI)

El desarrollo del agente local debe concebirse pensando en una migración sin fricciones hacia la nube de **Oracle Cloud Infrastructure (OCI)** [34, 44]. Las instrucciones de despliegue para Copilot son:

- **Contenerización:** Toda la aplicación (API de backend, RAG, dependencias) debe empaquetarse en una imagen de Docker y ser almacenada en **OCI Container Registry (OCIR)** [35].
- **Infraestructura de Cómputo:** Configurar el pipeline para que el host final sea flexible, permitiendo despliegues en **OCI Compute** (instancias de máquinas virtuales), **Container Instances** (ejecución sin servidores), o clusters de **OKE (Oracle Kubernetes Engine)** [35].
- **Almacenamiento de Archivos:** Las fuentes de datos originales deben conectarse a **OCI Object Storage**, con seguridad reforzada mediante políticas de IAM [35].
- **Persistencia Vectorial:** Utilizar **Oracle Autonomous Database** (aprovechando su soporte nativo para búsqueda vectorial) o bases vectoriales dedicadas autoalojadas [35].
- **Seguridad:** Las credenciales del modelo, llaves de API, y strings de conexión deben leerse obligatoriamente de forma segura desde **OCI Vault**, evitando exponer secretos en archivos de configuración locales o variables de entorno del contenedor [35].
