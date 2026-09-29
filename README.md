Actúa como arquitecto empresarial senior (TOGAF 10, ArchiMate 3.2, integración SOAP/REST, TM Forum TMF667, Microsoft Azure). Hoy debo entregar a mi gerencia el Architecture Definition Document (ADD) de Process One. NO tengo tiempo para aclaraciones: NO me hagas preguntas. Trabaja con lo que hay; lo que falte queda como pendiente para la siguiente revisión.

ARCHIVOS ADJUNTOS
[A] Mi Word con el formato corporativo del ADD y mi avance. ES EL DOCUMENTO FINAL: su estructura, títulos, orden, tablas y columnas no se cambian.
[B] ADD_Process_One_v0.9.2.docx: fuente con el contenido técnico completo de Process One.
[C] Documentación de las APIs SOAP de OnBase (si está adjunta).
[D] Documentación de la API TMF667 Document Management que ya existe en la empresa (si está adjunta).
[E] Modelo ArchiMate en XML (si está adjunto).

OBJETIVO
Pasar TODA la información de [B] al formato de [A], respetando lo que yo ya avancé en [A], completando todas las secciones, y decidir la integración con OnBase según el análisis de APIs de abajo. El resultado debe quedar listo para revisión de gerencia.

REGLAS DE TRABAJO
1. Cero preguntas. Si falta un dato, escribe {{DATO_FALTANTE}} en el lugar exacto y regístralo en la sección de Pendientes con responsable y "Revisión siguiente".
2. Prioridad de fuentes: documentación real [C]/[D] > mi avance en [A] > contenido de [B]. Si [A] y [B] se contradicen, conserva [A] salvo que [C]/[D] demuestren que está mal; en ese caso corrige y anótalo en la bitácora.
3. No borres mi texto de [A]: complétalo, mejóralo en redacción si hace falta, y agrega lo que falte desde [B].
4. Estructura: mantén exactamente los títulos, el orden y las columnas de las tablas de [A]. Si [B] tiene información que no tiene sección equivalente, ubícala en la sección más cercana o en Anexos; nunca la pierdas.
5. Ninguna sección queda vacía. Si una sección no aplica a Process One, escribe "No aplica" y una frase de justificación (por ejemplo, Cadena de valor: Process One enriquece un proceso de soporte existente; se analizan las etapas del proceso).
6. Mantén los ID (OBJ, DRV, PR, RES, RSK, BB, RN, RNQ, INT, DAT, TEC, SEG, RNF, ADR, GAP, PEN, AG) y su trazabilidad. No dupliques ni reutilices ID.
7. No inventes IPs, cuentas, nombres de personas, nombres de operaciones SOAP, keywords de OnBase ni cuotas: usa {{MARCADOR}}. Nunca escribas contraseñas, llaves ni certificados.
8. Estilo: institucional, impersonal, frases cortas, español. Números con punto de miles y coma decimal (1.288; 4,2 h).
9. Arquitectura que NO se cambia (componentes reales): OnBase on-premises con sus APIs; API Gateway on-premises; VPN site-to-site; en Azure: Process One Web, Backend de Process One y API de Ingesta de OnBase en Azure Container Apps; Azure Blob Storage; Azure AI Search con indexer y skillset (OCR, enriquecimiento, embeddings) que indexa automáticamente lo que llega a Blob; sistema multiagente de 18 agentes en Microsoft Foundry con modelos Azure OpenAI; chatbot en Copilot Studio (Teams y web). El documento aprobado se carga a OnBase como revisión NO vigente; la publicación la hace el flujo de OnBase. Los 18 agentes se detallan con información real en sitio: deja su catálogo con lo que haya y el resto como pendiente.

ANÁLISIS DE APIS Y DECISIÓN DE INTEGRACIÓN (obligatorio, hazlo antes de redactar la sección de aplicaciones)
Paso 1 – Operaciones que Process One necesita:
  N1 Listar documentos por tipo y por fecha de modificación (carga inicial e incremental).
  N2 Obtener metadatos de un documento (tipo, área, versión, estado, fechas, dueño, relacionados/adjuntos).
  N3 Descargar el binario del documento y de sus adjuntos.
  N4 Crear el documento aprobado como revisión NO vigente, vinculado al documento vigente y al ticket SGP.
  N5 (deseable) Consultar tipos documentales / catálogo.
Paso 2 – Con [C], arma la tabla "Operaciones SOAP de OnBase": operación exacta, qué hace, entrada, salida, necesidad que cubre (N1–N5), fuente (archivo y página). Si [C] no está, usa las operaciones genéricas de [B] marcadas como {{OPERACIÓN_SOAP}}.
Paso 3 – Con [D], arma la tabla "Cobertura de la TMF667 existente": para N1–N5 indica Cubre / Cubre con cambio / No cubre, y qué cambio haría falta (nuevo filtro, nuevo campo, descarga de contenido, POST con estado no vigente, relación isRevisionOf, etc.).
Paso 4 – Decide con esta regla y justifícala en un ADR:
  OPCIÓN A – Usar la TMF667 existente y solicitar modificaciones: si existe, cubre N1–N3 (aunque sea con cambios menores), respeta la cuota de OnBase (máximo 450 llamadas por hora hacia OnBase) y los cambios para N4 son viables por el equipo dueño del API Gateway. Resultado: la API de Ingesta consume la TMF667 v4 a través de la VPN; se emite un "Requerimiento de cambio a la TMF667" con la lista de cambios.
  OPCIÓN B – Integración directa con las APIs SOAP de OnBase: si la TMF667 no existe, no está documentada, no cubre N1–N3, o los cambios no son viables. Resultado: la API de Ingesta consume los servicios SOAP de OnBase (a través del API Gateway como proxy de seguridad si existe, o directo por la VPN), aplica ella misma la cuota de 450 llamadas por hora, y hace la traducción SOAP ↔ modelo interno. La adopción de TMF667 queda como evolución futura en el roadmap.
  OPCIÓN MIXTA: solo si está claramente justificado (p. ej., lectura por TMF667 y escritura N4 por SOAP).
  Si falta [D], aplica OPCIÓN B como decisión vigente y deja "Evaluar TMF667 existente" como pendiente para la siguiente revisión.
Paso 5 – Refleja la decisión de forma coherente en TODO el documento: resumen ejecutivo, alcance, supuestos, principios, componentes y diseño de la API de Ingesta, tabla de servicios/interfaces/APIs (una fila por operación real), intercambio de información, mapeo de atributos OnBase ↔ modelo (↔ TMF667 si opción A), contratos de servicio, conectividad (puertos y protocolos), capacidad (llamadas y horas de carga: 1.288 objetos ≈ 1.882 llamadas ≈ 4,2 h a 450 req/h, recalcula si las operaciones reales cambian el número de llamadas), identidad y auditoría, decisiones (ADR), riesgos, brechas, roadmap y pendientes. Si es opción A, agrega en Anexos la tabla "Requerimiento de cambio a la TMF667" (ID, operación/recurso, cambio solicitado, motivo, prioridad, responsable).

FORMATO DE ENTREGA
- Si puedes generar archivos: entrega el Word completo con el formato de [A] (mismos estilos, títulos y tablas), con los {{MARCADORES}} resaltados en amarillo, y además un resumen de cambios.
- Si no puedes generar archivos: entrega el documento COMPLETO en el orden de [A], sección por sección, listo para pegar en Word: títulos con su numeración, párrafos y tablas en formato markdown con TODAS sus columnas. No resumas, no digas "igual que en la fuente", no omitas filas.
- Divide la entrega en partes si es largo. Parte 1 empieza con: (1) la tabla de análisis de APIs y la DECISIÓN tomada, (2) el control del documento. Termina cada parte con "Parte X de N – Escribe CONTINÚA" y continúa exactamente donde quedaste.
- La bitácora del documento debe incluir una fila nueva: versión {{VERSIÓN}}, fecha de hoy, "Consolidación en formato corporativo; análisis de APIs y decisión de integración; pendientes para la revisión siguiente".

DIAGRAMAS
- En cada sección donde el formato pide un diagrama, deja: "Figura N. [título]" y una línea "Fuente: vista ArchiMate [nombre]" usando las figuras de [B]. Si la decisión fue OPCIÓN B, indica en la figura de arquitectura TO-BE y en la de despliegue que la fachada TMF667 se reemplaza por la integración SOAP directa (y lista qué cambia en cada diagrama).
- Si adjunté [E], al final entrega "Cambios en el modelo ArchiMate": fragmentos XML en formato Open Exchange listos para pegar, cada uno con su punto de inserción (antes de </elements>, antes de </relationships>, o BUSCAR / REEMPLAZAR POR dentro de la vista). Reglas: identifiers únicos que empiecen con letra; relaciones válidas en ArchiMate 3.2 (componente Realization servicio, servicio Serving proceso, interfaz Serving componente, componente Composition interfaz, Flow con nombre entre componentes, nodo Serving componente); las conexiones de una vista apuntan a nodos de esa vista y a relaciones existentes; coordenadas absolutas y sin solapes. Para cargarlo: Archi → File → Import → Open Exchange XML Model.

CIERRE (al final de la última parte)
1. Tabla "Pendientes para la revisión siguiente": ID, pendiente, responsable, impacto.
2. Checklist: todas las secciones de [A] completas · decisión de integración reflejada en todas las secciones · tablas con todas sus columnas · ID sin duplicados · sin datos confidenciales inventados · bitácora actualizada.

Empieza ahora con la Parte 1.
