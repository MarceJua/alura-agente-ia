# 🩺 Alura Agente: Asistente de IA para Clínica "Sanitas Innova"

Este repositorio contiene la solución completa para el **Challenge Alura Agente**, que consiste en un agente de Inteligencia Artificial corporativo optimizado para resolver consultas de los colaboradores de la clínica **Sanitas Innova**. El agente utiliza una arquitectura RAG (Retrieval-Augmented Generation) para responder preguntas complejas y precisas basadas exclusivamente en la política de privacidad de datos del paciente (POL-PRIV-001) y en las instrucciones pre y post-consulta (PROT-MED-004).

---

## 🚀 Arquitectura del Sistema

La solución implementa una tubería RAG robusta estructurada en cinco etapas clave para evitar la alucinación de datos y garantizar respuestas confiables y auditables:

```
                  ┌─────────────────────────────────────────────────────────┐
                  │                 Documentos Fuente                       │
                  │  (POL-PRIV-001.md / PROT-MED-004.md)                    │
                  └──────────────────────────┬──────────────────────────────┘
                                             │
                                             ▼
                  ┌─────────────────────────────────────────────────────────┐
                  │     Procesamiento: Markdown Chunking & Metadatos         │
                  │     (Filtro de secciones + Inyección de metadatos)      │
                  └──────────────────────────┬──────────────────────────────┘
                                             │
                                             ▼
                  ┌─────────────────────────────────────────────────────────┐
                  │              Indexación: Embeddings                     │
                  │  (Generación de vectores y almacenamiento en Qdrant/Chroma)│
                  └──────────────────────────┬──────────────────────────────┘
                                             │
                                             ▼
    ┌──────────────────┐                     │
    │  Pregunta del    ├─────────────────────┼──────────────────┐
    │  Colaborador     │                     │                  │
    └────────┬─────────┘                     ▼                  │
             │                    ┌──────────────────────┐      │
             │                    │ Recuperación Semántica│      │
             │                    │  (Búsqueda Vectorial)│      │
             │                    └──────────┬───────────┘      │
             │                               │                  │
             │                               ▼                  │
             │                    ┌──────────────────────┐      │
             │                    │ Reranker (Cohere)    │      │
             │                    │ (Ordena Relevancia)  │      │
             │                    └──────────┬───────────┘      │
             │                               │                  │
             └───────────────┬───────────────┘                  │
                             │ Contexo Filtrado                 │ Fallback
                             ▼                                  ▼
                  ┌─────────────────────────────────────────────────────────┐
                  │            Generación Controlada (LLM)                  │
                  │   (Validación estricta de fuentes / Respuesta en chat)  │
                  └──────────────────────────┬──────────────────────────────┘
                                             │
                                             ▼
                  ┌─────────────────────────────────────────────────────────┐
                  │          Respuesta Grounded + Citación de Fuentes       │
                  └─────────────────────────────────────────────────────────┘
```

1. **Ingesta y Limpieza:** Extracción estructurada del contenido en Markdown, aislando metadatos críticos como códigos de protocolo, áreas clínicas, responsables (DPO) y vigencia.
2. **Chunking Semántico:** División del texto mediante un divisor lógico respetando la estructura de encabezados para mantener la cohesión de los datos.
3. **Indexación Vectorial:** Conversión de texto en vectores densos almacenados en una base de datos vectorial con indexación de metadatos para filtrado previo.
4. **Recuperación y Reranking:** Búsqueda híbrida (semántica + filtros de metadatos) combinada con un modelo _Reranker_ para priorizar los fragmentos con mayor relevancia clínica.
5. **Generación Grounded:** Prompting restrictivo que obliga al LLM a responder basándose única y exclusivamente en el contexto recuperado, retornando un mensaje de _fallback_ configurado si la información no existe.

---

## 🛠️ Stack Tecnológico

El agente está construido con herramientas modernas, modulares y de alto rendimiento en el ecosistema de IA:

- **Lenguaje:** Python 3.12
- **Orquestación LLM/RAG:** LangChain
- **Base de Datos Vectorial:** Qdrant o Chroma (local) / Oracle Autonomous Database (en la nube)
- **Modelos de Embeddings y Generación:** OpenAI (GPT-4o) / Cohere (Rerank-v3)
- **Interfaz de Usuario:** Streamlit (interfaz ágil, directa y enfocada en datos)
- **Contenerización y Despliegue:** Docker, OCI Container Registry y OCI Compute

---

## 💻 Instrucciones de Ejecución Local

Sigue estos pasos para levantar el agente localmente en tu máquina de desarrollo:

### 1. Clonar el repositorio y configurar variables de entorno

```bash
git clone https://github.com/tu-usuario/alura-agente-clinica.git
cd alura-agente-clinica
cp .env.example .env
```

_Edita el archivo `.env` con tus llaves de API necesarias (`OPENAI_API_KEY`, `COHERE_API_KEY`, etc.)._

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```

### 3. Instalar las dependencias del proyecto

```bash
pip install -r requirements.txt
```

### 4. Indexar los documentos de la Clínica "Sanitas Innova"

```bash
python scripts/ingest_knowledge_base.py
```

_Este comando procesará el archivo `clinica-knowledge-base.md`, generará los embeddings e indexará los chunks en la base de datos vectorial._

### 5. Iniciar la interfaz conversacional

```bash
streamlit run app.py
```

Abre tu navegador en `http://localhost:8501` para comenzar a interactuar con el asistente clínico.

---

## ❓ Casos de Prueba y Respuestas del Agente

Para validar la precisión del sistema y garantizar que no existan alucinaciones, puedes realizar las siguientes preguntas de control al agente:

### Caso de Prueba 1: Conservación de datos confidenciales

- **Pregunta del Colaborador:** _"¿Durante cuánto tiempo debemos conservar las fichas clínicas electrónicas y en qué condiciones se eliminan los registros físicos en papel?"_
- **Respuesta Esperada del Agente:**
  > Basado en la Política de Privacidad **POL-PRIV-001 (Sección 1.2)**, las fichas clínicas electrónicas se deben conservar de forma obligatoria por un período mínimo de **15 años** desde la última interacción médica del paciente. Los registros físicos en papel se resguardan por **5 años**, tras lo cual se destruyen de manera segura mediante un proceso de **trituración industrial con certificación de destrucción confidencial**.

### Caso de Prueba 2: Instrucciones de ayuno médico

- **Pregunta del Colaborador:** _"Tengo un paciente de Gastroenterología programado para una Endoscopía Digestiva Alta. ¿Cuáles son las instrucciones de ayuno y qué medicamentos tiene prohibidos?"_
- **Respuesta Esperada del Agente:**
  > De acuerdo con el protocolo de preparación **PROT-MED-004 (Área de Gastroenterología)**, las instrucciones obligatorias son:
  >
  > 1. **Ayuno:** Ayuno absoluto de sólidos y líquidos de al menos **8 horas** antes de la intervención.
  > 2. **Medicación Suspendida:** Se prohíbe la ingesta de **antiácidos y protectores gástricos (como el omeprazol)** en las **24 horas previas** al procedimiento. Se permite la toma de medicación crítica con un sorbo mínimo de agua (máximo 50 ml) hasta 3 horas antes del examen.

### Caso de Prueba 3: Manejo de Alucinaciones (Fuera de Ámbito)

- **Pregunta del Colaborador:** _"¿Cuál es la política de la clínica para el reembolso de estacionamiento de los médicos?"_
- **Respuesta Esperada del Agente:**
  > **[Código Fallback: INF-NO-DISP]** Lo siento, no he encontrado información sobre la política de reembolso de estacionamiento para médicos en los documentos de gobernanza y protocolos clínicos disponibles en mi base de datos actual. Si esta información pertenece al área de Recursos Humanos o Finanzas, por favor póngase en contacto con el administrador del área correspondiente.

---

## ☁️ Despliegue en la Nube (Oracle Cloud Infrastructure - OCI)

El proyecto se encuentra completamente productivo e implementado de forma segura en la infraestructura de **OCI**.

### Componentes de OCI Utilizados:

- **OCI Container Registry (OCIR):** Almacenamiento seguro de la imagen Docker de producción del agente.
- **OCI Compute:** Instancia de máquina virtual escalable configurada dentro de una red privada virtual (VCN).
- **OCI Vault:** Gestión cifrada de credenciales de API para mitigar riesgos de seguridad.
- **OCI Object Storage:** Repositorio en la nube para almacenamiento y sincronización automática de los documentos de conocimiento originales.

### 📸 Evidencia de Ejecución en la Nube

Aquí se presenta la captura de pantalla de la interfaz conversacional de Sanitas Innova respondiendo consultas de manera segura desde la instancia desplegada en la nube:

![Evidencia de Ejecución en la Nube](https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&q=80&w=1000)

_(Reemplazar por el enlace real del GIF o captura de pantalla obtenido tras el despliegue final en OCI)_

---

## 📊 Registro de Ejecución (Logs locales en producción)

El agente registra cada una de las interacciones en un archivo estructurado local `logs/agent_execution.jsonl` bajo el siguiente formato para permitir la auditoría de respuestas:

```json
{
  "timestamp": "2026-07-10T22:35:11-07:00",
  "query": "¿Por cuánto tiempo se guardan las fichas en papel?",
  "response": "De acuerdo con el documento POL-PRIV-001, las fichas físicas se conservan por 5 años y luego se destruyen con trituración industrial certificada.",
  "source_documents": ["POL-PRIV-001"],
  "latency_seconds": 1.45,
  "status": "SUCCESS"
}
```
