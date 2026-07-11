# Requisitos de Entrega y Validación - Challenge Alura Agente

Este documento detalla los requisitos fundamentales, las etapas de desarrollo y los entregables críticos necesarios para completar de forma exitosa el **Challenge Alura Agente** [42].

---

## 🔄 Las Tres Etapas del Proyecto [43, 44]

1. **Etapa 1: Ingesta y Procesamiento de Documentos**
   - Seleccionar un documento fuente (formatos recomendados: **PDF** o **CSV**) [43, 51].
   - Desarrollar código para leer, limpiar y fragmentar el archivo para que el sistema "entienda" y extraiga correctamente su contenido [43, 53].

2. **Etapa 2: Construcción del Agente de IA**
   - Desarrollar un agente capaz de comprender y responder preguntas en lenguaje natural utilizando el documento procesado como contexto [44].
   - Asegurar que el agente use técnicas de búsqueda semántica (RAG) para localizar la información correcta e indicar la fuente original [27, 44].

3. **Etapa 3: Despliegue en la Nube (OCI)**
   - Implementar y publicar públicamente el agente en la infraestructura de nube de **Oracle Cloud Infrastructure (OCI)** para que deje de ejecutarse únicamente en entorno local [44].

---

## 💻 Entregables Exactos para GitHub [46, 52]

El proyecto debe publicarse en un **repositorio público** de GitHub y contener la siguiente estructura y elementos de validación [4, 52]:

- **Repositorio Estructurado y Limpio:** Estructura de carpetas organizada con todo el código fuente del proyecto y un historial de commits frecuente que demuestre la evolución del desarrollo [52].
- **Archivo README.md Profesional:** Debe incluir de manera detallada:
  - **Descripción General:** Propósito del agente corporativo y contexto seleccionado [52].
  - **Arquitectura de la Solución:** Diagrama técnico de la arquitectura implementada (RAG, flujo de datos y servicios en la nube) [46, 52].
  - **Tecnologías y Herramientas:** Detalle del stack técnico (Python, LangChain, base de datos vectorial, etc.) [52].
  - **Instrucciones de Ejecución:** Guía clara paso a paso para clonar, configurar e iniciar el proyecto de forma local [46, 52].
  - **Casos de Uso (QA):** Ejemplos prácticos de preguntas que el agente puede responder con éxito y las respuestas correspondientes [46, 52].
  - **Evidencia Visual del Despliegue:** Un enlace público, captura de pantalla o video incrustado que demuestre el agente ejecutándose en línea dentro de OCI [4, 46, 53].

---

## ☁️ Despliegue en OCI y Registro de Ejecución

### 1. Pasos de Despliegue Recomendados en OCI [35]

Para cumplir con el requisito obligatorio de usar **al menos un servicio de OCI** [4, 36]:

- **Contenerización (Docker):** Empaquetar la aplicación en una imagen Docker y hospedarla en _OCI Container Registry (OCIR)_ [35].
- **Servicio de Cómputo VM:** Utilizar _OCI Compute_ (instancias de VM sencillas), _Container Instances_, u _OKE (Oracle Kubernetes Engine)_ para el escalado y ejecución pública del agente [35, 45].
- **Almacenamiento de Datos:** Guardar los documentos fuentes originales en _OCI Object Storage_ [35].
- **Base de Datos Vectorial:** Sincronizar embeddings en _Oracle Autonomous Database_ (con soporte de búsqueda vectorial nativo) o emplear soluciones dedicadas de bases de datos vectoriales en la VM [35].
- **Seguridad:** Resguardar API keys sensibles del LLM y credenciales críticas dentro de _OCI Vault_ [35].

### 2. Registro de Ejecución y Trazabilidad (Logging) [36, 37]

El registro de ejecución es un requisito obligatorio para asegurar la auditoría de la IA [36, 39]. Se puede implementar en dos modalidades:

- **Trazabilidad Local (Recomendado para pruebas iniciales):**
  - Almacenar logs locales estructurados en formato **JSON Lines** (`.jsonl`) [37].
  - Registrar metadatos esenciales en cada interacción: **pregunta del usuario, contexto recuperado del documento, respuesta final generada por el LLM, marca de tiempo (timestamp) y tiempo de respuesta** [37].
- **Trazabilidad en la Nube (Producción):**
  - Centralizar los logs mediante servicios nativos en la nube para permitir la retención a largo plazo, alarmas de error y monitoreo de latencias y consumo de tokens [38].
- **Evidencias Multimedia:** Es mandatorio registrar el agente funcionando en la nube mediante capturas o videos integrados en el README [4, 37].

---

## ⚠️ Puntos Críticos para un Desarrollo Exitoso

- **Primero Local, luego Cloud:** Desarrolla y valida el agente localmente antes de iniciar el deploy en OCI [47]. Tratar de subir a producción un código no probado localmente ralentiza el ciclo de desarrollo [47].
- **Prevención de Alucinaciones (Garantía de Confianza):** Configura system prompts restrictivos para que el agente responda únicamente basándose en el contexto extraído de los documentos [27, 28]. Si la respuesta no está disponible, el agente debe indicarlo con un mensaje claro de _fallback_ ("no encontré esta información") en lugar de inventar contenido [28, 29].
- **Funcionalidad > Estética del Frontend:** El core del desafío es la precisión del RAG y el despliegue funcional en OCI, no el diseño visual [30, 47]. Una interfaz funcional y simple (como un chat en **Streamlit** o un bot de Teams/Slack) es más que suficiente para cumplir los requisitos [30, 31, 34, 47].
