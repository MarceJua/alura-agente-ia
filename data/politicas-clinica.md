# Base de Conocimiento - Clínica Sanitas Innova

Este documento contiene las políticas oficiales y las directrices clínicas de la **Clínica Sanitas Innova**. Está estructurado específicamente para optimizar la recuperación y extracción de información precisa por parte de agentes RAG (Retrieval-Augmented Generation).

---

## PARTE 1: Política de Privacidad y Protección de Datos de Pacientes (POL-PRIV-001)

### 1.1. Información General del Responsable

- **Razón Social:** Clínica Médica Sanitas Innova S.A.
- **Domicilio Legal:** Av. Providencia 1020, Piso 4, Santiago, Chile.
- **Delegado de Protección de Datos (DPO):** Dr. Roberto Arenas.
- **Contacto DPO:** dpo@sanitasinnova.com | Teléfono: +56 2 2899 4000 (Anexo 802).

### 1.2. Datos Personales Recolectados y Categorización

La clínica clasifica y procesa tres (3) categorías estrictas de datos bajo estrictas medidas de cifrado (AES-256):

1.  **Datos de Identificación:** Nombre completo, RUN/Cédula, fecha de nacimiento, género, dirección de residencia, correo electrónico y número de teléfono móvil de contacto.
2.  **Datos Financieros:** Información de seguros médicos (Isapre o Fonasa), números de previsión, datos de tarjetas de pago, historial de facturación y copagos.
3.  **Datos Sensibles de Salud (Historial Clínico):** Diagnósticos médicos, antecedentes familiares, recetas emitidas, resultados de exámenes de laboratorio e imágenes, registro de alergias, notas de evolución médica y grabaciones de telemedicina.

### 1.3. Tiempos de Retención de la Información

Para cumplir con la legislación sanitaria vigente, se establecen los siguientes plazos improrrogables de conservación de fichas médicas:

- **Ficha Clínica Electrónica:** Conservación obligatoria por un período mínimo de **15 años** contados desde la fecha de la última atención registrada en el sistema.
- **Fichas Clínicas Físicas e Históricas (Papel):** Almacenadas en bodega centralizada durante un máximo de **5 años** tras su digitalización completa. Cumplido este plazo, se procede a su destrucción física mediante triturado certificado de nivel P-4 (seguridad de corte fino).
- **Registros de Videollamadas de Telemedicina:** Almacenados en servidores seguros locales por un plazo máximo de **2 años** desde la fecha de la sesión, tras lo cual se eliminan de forma automatizada mediante script programado.

### 1.4. Derechos del Paciente (Derechos ARCO)

Todo paciente o su representante legal (debidamente acreditado mediante poder notarial) puede ejercer sus derechos de Acceso, Rectificación, Cancelación y Oposición:

- **Canal Único de Solicitud:** Correo electrónico a arco@sanitasinnova.com, adjuntando el **Formulario F-09** disponible en el portal web de la clínica.
- **Plazo de Respuesta:** El equipo legal dispone de un plazo máximo de **10 días hábiles** para emitir una resolución y ejecutar los cambios o accesos solicitados.
- **Excepciones de Cancelación:** No se podrá cancelar ni eliminar la información de la Ficha Clínica si el paciente mantiene un tratamiento médico activo en curso, una deuda pendiente de liquidación con la clínica, o si colisiona con el requisito de retención legal de 15 años.

### 1.5. Protocolo de Transferencia y Compartición de Datos

- **Aseguradoras y Coberturas Médicas:** Solo se comparten datos clínicos mínimos indispensables (códigos de diagnóstico CIE-10 y procedimientos arancelados) mediante el protocolo de comunicación seguro **HL7 / FHIR** para procesar la cobertura de seguros. Requiere la firma previa del documento "Consentimiento de Transmisión de Cobertura" (**Formulario Form-F-102**).
- **Autoridades de Salud Pública:** Se notifican de manera obligatoria y sin requerir consentimiento previo las patologías de declaración obligatoria (según el Decreto Supremo N° 7 del Ministerio de Salud, como Tuberculosis, Dengue, COVID-19), utilizando los canales de transmisión encriptados del Minsal.

---

## PARTE 2: Guía de Instrucciones Pre y Post-Consulta (PROT-MED-004)

Esta sección detalla los requerimientos específicos que deben cumplir los pacientes antes de someterse a procedimientos médicos clave y las instrucciones clínicas de cuidado inmediato posterior.

| Especialidad / Procedimiento                            | Requisitos Pre-Consulta (Preparación Obligatoria)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Instrucciones Post-Consulta (Cuidados Posteriores)                                                                                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gastroenterología**<br>_(Endoscopía Digestiva Alta)_  | • **Ayuno Estricto:** Mínimo de **8 horas** de ayuno absoluto de sólidos y líquidos (incluye agua y chicles).<br>• **Medicamentos:** Suspender antiácidos e inhibidores de bomba de protones (Omeprazol) **24 horas antes**.<br>• **Acompañamiento:** Llegar **30 minutos antes** de la cita acompañado obligatoriamente por un adulto responsable (no se realizará el examen sin acompañante debido al uso de sedación).                                                                                                                                        | • **Conducción:** Prohibición absoluta de conducir vehículos o maquinaria pesada durante las **6 horas posteriores** debido a efectos residuales de la sedación.<br>• **Alimentación:** Iniciar con una dieta blanda e hidratación fría (gelatina, agua, sopa clara) durante las primeras **4 horas**. Evitar picantes o grasas.<br>• **Urgencias:** En caso de fiebre superior a **38°C** o dolor abdominal agudo, contactar a Urgencias (Anexo 405). |
| **Cardiología**<br>_(Prueba de Esfuerzo / Ergometría)_  | • **Vestimenta:** Acudir con ropa deportiva holgada y calzado deportivo cómodo (zapatillas de running).<br>• **Alimentación previa:** Desayuno ligero hasta un máximo de **2 horas antes** del examen. <br>• **Restricciones:** No consumir cafeína, té, bebidas energéticas, chocolate ni tabaco durante las **12 horas previas**.<br>• **Betabloqueadores:** Suspender medicamentos betabloqueadores (Atenolol, Propranolol) **48 horas antes**, únicamente si el cardiólogo tratante lo ha indicado expresamente por escrito en el **Formulario Form-C-302**. | • **Reposo:** Permanecer sentado en el área de observación clínica por un mínimo de **15 minutos** post-examen para monitoreo de presión arterial.<br>• **Duchas:** Evitar duchas con agua caliente durante las **2 horas posteriores** para prevenir vasodilatación periférica brusca y riesgo de síncope o mareos.                                                                                                                                   |
| **Laboratorio Clínico**<br>_(Perfil Lipídico Completo)_ | • **Ayuno requerido:** Ayuno estricto de **12 horas**. Solo se permite la ingesta de agua en cantidades moderadas (sin azúcar ni saborizantes).<br>• **Alcohol:** Prohibición absoluta de consumir bebidas alcohólicas durante las **48 horas previas** a la toma de muestra de sangre.<br>• **Actividad Física:** No realizar ejercicio físico extenuante o de alta intensidad **24 horas antes** del examen, ya que altera significativamente los marcadores enzimáticos.                                                                                      | • **Presión local:** Mantener la tela adhesiva y el algodón presionando firmemente el punto de punción durante al menos **10 minutos** continuos.<br>• **Fuerza física:** No levantar objetos pesados ni realizar esfuerzos físicos exigentes con el brazo utilizado para la extracción de sangre durante las siguientes **2 horas** (evita la formación de hematomas severos).                                                                        |

---

## PARTE 3: Preguntas Frecuentes de Uso Interno (FAQ para Colaboradores)

### Q1: ¿Qué debe hacer el personal si un paciente solicita una copia de su ficha clínica?

El colaborador debe guiar al paciente a rellenar el **Formulario F-09** y solicitarle enviarlo junto a una copia digital de su cédula de identidad al correo **arco@sanitasinnova.com**. Bajo ninguna circunstancia el colaborador debe imprimir o descargar la ficha directamente para entregársela al paciente en recepción sin la validación previa del DPO o el área legal, quienes tienen un plazo legal de **10 días hábiles** para responder la solicitud de acceso.

### Q2: El paciente consumió una taza de café negro sin azúcar 4 horas antes de su Prueba de Esfuerzo. ¿Se puede realizar el examen?

**No.** La directriz de Cardiología (PROT-MED-004) prohíbe taxativamente la ingesta de cafeína durante las **12 horas previas** al procedimiento. El café (incluso sin azúcar) altera la frecuencia cardíaca basal del paciente y falsea los resultados de la ergometría. El colaborador de recepción debe reprogramar la cita e indicarle al paciente que cumpla estrictamente con las 12 horas de abstención de café, té, bebidas de fantasía y tabaco.

### Q3: ¿Por cuánto tiempo debemos conservar los archivos en PDF de las recetas médicas digitales?

Las recetas médicas digitales forman parte integral de la **Ficha Clínica Electrónica** del paciente. Por lo tanto, entran en la categoría de Datos Sensibles de Salud y deben conservarse por un plazo mínimo de **15 años** en los servidores seguros y cifrados de la clínica, contabilizados desde la última atención médica del paciente.

### Q4: ¿Se puede realizar una Endoscopía Digestiva Alta si el paciente viene solo en su propio automóvil?

**No.** El protocolo clínico de Gastroenterología establece que es obligatorio que el paciente se presente **30 minutos antes** con un acompañante adulto responsable. Dado que el examen se realiza bajo sedación profunda, el paciente no está en condiciones neurológicas óptimas para retirarse solo o conducir un vehículo durante las siguientes **6 horas**. Si el paciente insiste en que no tiene acompañante, el procedimiento debe ser suspendido y reagendado por el equipo médico de admisión.
