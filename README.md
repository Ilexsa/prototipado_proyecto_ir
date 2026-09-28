# Architecture Definition Document (ADD)

> **Iniciativa / Proyecto:** [Nombre del proyecto]  
> **Área solicitante:** [Área]  
> **Patrocinador:** [Nombre y cargo]  
> **Líder de arquitectura:** [Nombre y cargo]  
> **Estado:** [Borrador / En revisión / Aprobado]  
> **Versión:** [v0.1]  
> **Fecha:** [dd/mm/aaaa]

---

## Control del documento

### Bitácora del documento

| # | Autor | Fecha | Descripción del cambio | Versión |
|---|---|---|---|---|
| 1 | [Nombre] | [dd/mm/aaaa] | Versión inicial del documento | v0.1 |

### Equipo de trabajo

| Actor | Rol | Área / Organización | Responsabilidad |
|---|---|---|---|
| [Nombre] | [Rol] | [Área] | [Responsabilidad dentro de la iniciativa] |

### Documentos relacionados

| Documento | Descripción | Versión | Ubicación |
|---|---|---|---|
| [Nombre] | [Descripción] | [Versión] | [Enlace o repositorio] |

---

# 1. Preliminar

## 1.1 Antecedentes

[Describir la situación actual, la necesidad que origina la iniciativa, los servicios involucrados, los volúmenes conocidos y los problemas u oportunidades identificados.]

## 1.2 Propósito del documento

[Explicar qué decisiones de arquitectura documenta el ADD y para qué será utilizado.]

## 1.3 Alcance

### Incluye

- [Proceso, sistema, integración o capacidad incluida]
- [Área o canal incluido]

### No incluye

- [Elemento fuera del alcance]
- [Configuraciones, manuales o procedimientos no cubiertos]

## 1.4 Conceptos clave

| Concepto | Definición |
|---|---|
| [Concepto] | [Definición sencilla y contextual] |

## 1.5 Supuestos

- [Supuesto validado o utilizado para definir la arquitectura]

## 1.6 Dependencias

- [Dependencia con otro proyecto, proveedor, plataforma o decisión]

---

# 2. Visión de arquitectura

## 2.1 Resumen ejecutivo

[Presentar brevemente la necesidad, la solución propuesta, su alcance, el valor esperado y las principales implicaciones para el negocio.]

## 2.2 Mapa de interesados

| Interesado | Área / Organización | Interés | Influencia | Clasificación | Estrategia de comunicación |
|---|---|---|---|---|---|
| [Nombre o grupo] | [Área] | [Interés] | [Alta/Media/Baja] | [Actor clave / Mantener satisfecho / Mantener informado / Monitorear] | [Reunión, correo, comité, aprobación] |

## 2.3 Objetivos de negocio

> Los objetivos deben ser medibles y acordados con el responsable de negocio.

| ID | Objetivo | Indicador | Línea base | Meta | Plazo | Responsable |
|---|---|---|---|---|---|---|
| OBJ-01 | [Objetivo] | [Indicador] | [Valor actual] | [Valor esperado] | [Fecha] | [Responsable] |

## 2.4 Motivadores de negocio

| ID | Motivador | Descripción | Impacto esperado |
|---|---|---|---|
| DRV-01 | [Necesidad, regulación, eficiencia, tecnología, etc.] | [Descripción] | [Impacto] |

## 2.5 Principios de arquitectura aplicables

| ID | Principio | Aplicación en la iniciativa |
|---|---|---|
| PR-01 | [Principio] | [Cómo condiciona o guía la solución] |

## 2.6 Análisis de cadena de valor

| Etapa | Responsable | Proceso / Documento de referencia | Pregunta de análisis | Respuesta / Decisión | Estado |
|---|---|---|---|---|---|
| [Etapa] | [Responsable] | [Código y nombre] | [Pregunta] | [Respuesta] | [Definido / Pendiente / No aplica] |

## 2.7 Evaluación de capacidades

**Semáforo sugerido:**

- 🟢 **Sin cambio:** capacidad disponible y suficiente.
- 🟠 **Por modificar:** capacidad existente que requiere ajustes.
- 🔴 **Nueva:** capacidad que debe implementarse.

| Cadena de valor / Etapa | Capacidad empresarial | Tipo | Estado actual | Cambio requerido | Responsable |
|---|---|---|---|---|---|
| [Etapa] | [Capacidad] | [Negocio / Proceso / Datos / Aplicación / Tecnología] | [Descripción] | [Sin cambio / Modificar / Nueva] | [Responsable] |

## 2.8 Declaración de restricciones

| ID | Tipo | Restricción | Impacto | Tratamiento |
|---|---|---|---|---|
| RES-01 | [Tiempo / Presupuesto / Empresarial / Regulatoria / Tecnológica] | [Descripción] | [Impacto] | [Tratamiento] |

## 2.9 Análisis de riesgos de la visión

| ID | Riesgo formulado como pregunta | Interesado | Probabilidad | Impacto | Nivel | Estrategia de mitigación | Responsable |
|---|---|---|---|---|---|---|---|
| RSK-01 | [¿Qué ocurriría si...?] | [Interesado] | [Baja/Media/Alta] | [Bajo/Medio/Alto] | [Nivel] | [Mitigación] | [Responsable] |

## 2.10 Roadmap de arquitectura

> Completar cuando la iniciativa requiera fases o paquetes de trabajo para alcanzar la arquitectura objetivo.

| Fase | Paquete de trabajo | Resultado esperado | Dependencias | Responsable | Inicio | Fin |
|---|---|---|---|---|---|---|
| [Fase] | [Paquete] | [Resultado] | [Dependencias] | [Responsable] | [Fecha] | [Fecha] |

## 2.11 Aprobación de la visión

| Nombre | Rol | Decisión | Fecha | Evidencia / Firma |
|---|---|---|---|---|
| [Nombre] | Patrocinador | [Aprobado / Aprobado con observaciones / Rechazado] | [dd/mm/aaaa] | [Firma o enlace] |

---

# 3. Arquitectura de negocio

## 3.1 Building Blocks de negocio

| ID | Building Block | Descripción | Estado | Cambio requerido | Referencia |
|---|---|---|---|---|---|
| BB-N-01 | [Nombre] | [Descripción] | [Actual / Objetivo] | [Crear / Modificar / Reutilizar / Retirar] | [eTOM, ODA u otra referencia] |

## 3.2 Modelo de negocio (opcional)

[Explicar el modelo de negocio, participantes, propuesta de valor, relaciones, ingresos, costos y responsabilidades cuando sea necesario para entender la solución.]

## 3.3 Escenarios de negocio

| # | Escenario de negocio | Actor | Precondiciones / Entradas | Flujo resumido | Salidas | Resultado esperado | Excepciones |
|---|---|---|---|---|---|---|---|
| 01 | [Escenario] | [Actor] | [Entradas] | [Flujo] | [Salidas] | [Resultado] | [Excepción] |

## 3.4 Flujo de proceso de negocio

**Diagrama:** [Insertar enlace, imagen o referencia al modelo BPMN]

**Tipo de proceso:** [Organizacional / De negocio]

**Descripción:**  
[Describir el inicio, actividades principales, decisiones, participantes y resultado del proceso.]

### Reglas de modelado

- Utilizar nombres de capacidades para los procesos y mantenerlos independientes de un producto o mercado específico.
- Reutilizar procesos existentes antes de crear nuevos elementos.
- Representar las actividades a un nivel general. Usar notas o vistas complementarias cuando se necesite mayor detalle.
- Basar los Building Blocks de negocio en los marcos empresariales definidos por la organización.

## 3.5 Actores y responsabilidades

| Actor / Rol | Responsabilidad | Actividades principales | Sistemas utilizados |
|---|---|---|---|
| [Actor] | [Responsabilidad] | [Actividades] | [Sistemas] |

## 3.6 Reglas de negocio

| ID | Regla | Fuente | Responsable | Excepción |
|---|---|---|---|---|
| RN-01 | [Regla de negocio] | [Documento o área] | [Responsable] | [Excepción] |

## 3.7 Requisitos de negocio

| ID | Requisito | Prioridad | Criterio de aceptación | Fuente | Estado |
|---|---|---|---|---|---|
| RNQ-01 | [Requisito] | [Alta/Media/Baja] | [Criterio medible] | [Interesado] | [Pendiente/Validado] |

## 3.8 Análisis de riesgos de negocio

| ID | Riesgo formulado como pregunta | Interesado | Impacto | Estrategia de mitigación | Responsable |
|---|---|---|---|---|---|
| RSK-N-01 | [¿Qué ocurriría si...?] | [Interesado] | [Bajo/Medio/Alto] | [Mitigación] | [Responsable] |

---

# 4. Arquitectura de sistemas de información

## 4.1 Vista general

[Describir cómo las aplicaciones y los datos soportan los procesos de negocio incluidos en el alcance.]

## 4.2 Arquitectura AS-IS

**Diagrama:** [Insertar enlace, imagen o referencia al modelo]

**Descripción:**  
[Explicar la situación actual, componentes, integraciones, limitaciones y dependencias. Si la solución es completamente nueva, indicar “No aplica” y justificar.]

## 4.3 Arquitectura TO-BE

**Diagrama:** [Insertar enlace, imagen o referencia al modelo]

**Descripción:**  
[Explicar la arquitectura objetivo, el flujo principal, las responsabilidades de cada componente y los cambios frente al AS-IS.]

## 4.4 Building Blocks de aplicaciones

| ID | Componente / Plataforma | Propósito | Estado | Cambio | Propietario | Criticidad |
|---|---|---|---|---|---|---|
| BB-A-01 | [Nombre] | [Propósito] | [Existente / Nuevo] | [Reutilizar / Modificar / Crear / Retirar] | [Área] | [Alta/Media/Baja] |

## 4.5 Servicios, interfaces y APIs

| ID | Proveedor | Consumidor | Servicio / Interfaz | Operación | Protocolo | Autenticación | Datos principales | SLA |
|---|---|---|---|---|---|---|---|---|
| INT-01 | [Sistema] | [Sistema] | [Nombre] | [Consulta/Creación/etc.] | [REST/SOAP/Eventos/etc.] | [Método] | [Entidades] | [Valor] |

## 4.6 Colaboraciones entre aplicaciones

| Colaboración | Aplicaciones participantes | Propósito | Evento de inicio | Resultado |
|---|---|---|---|---|
| [Nombre] | [Aplicaciones] | [Propósito] | [Evento] | [Resultado] |

## 4.7 Reglas de modelado

- Organizar los diagramas en las capas de negocio, sistemas de información y tecnología.
- Representar los componentes de aplicación como plataformas o sistemas claramente identificables.
- Usar servicios de aplicación para exponer funcionalidades y elementos de interfaz para representar APIs.
- Usar colaboraciones de aplicación cuando una acción sea ejecutada conjuntamente por varias aplicaciones.
- Representar las entidades o tablas relevantes mediante objetos de datos.
- Reutilizar elementos existentes en el inventario de arquitectura antes de crear nuevos objetos.

---

# 5. Arquitectura de datos

## 5.1 Vista general de datos

[Describir los dominios de datos involucrados, su propósito y su relación con los procesos y aplicaciones.]

## 5.2 Intercambio de información interno y con terceros

**Diagrama de colaboración:** [Insertar enlace, imagen o referencia]

| ID | Origen | Destino | Entidad de datos | Campos principales | Evento / Frecuencia | Medio | Clasificación |
|---|---|---|---|---|---|---|---|
| DAT-01 | [Origen] | [Destino] | [Entidad] | [Campos] | [Evento/Frecuencia] | [API/Archivo/Evento] | [Pública/Interna/Confidencial/Restringida] |

## 5.3 Modelo de datos

**Diagrama:** [Insertar modelo conceptual, lógico o físico]

| Entidad | Descripción | Sistema maestro | Propietario | Retención | Referencia de modelo |
|---|---|---|---|---|---|
| [Entidad] | [Descripción] | [Sistema] | [Área] | [Periodo] | [TM Forum u otro estándar] |

## 5.4 Calidad y gobierno de datos

| Regla / Control | Dimensión | Responsable | Evidencia | Frecuencia |
|---|---|---|---|---|
| [Control] | [Exactitud/Completitud/Consistencia/etc.] | [Responsable] | [Evidencia] | [Frecuencia] |

## 5.5 Privacidad y protección de datos

| Tipo de dato | Finalidad | Base / Justificación | Acceso autorizado | Protección | Retención |
|---|---|---|---|---|---|
| [Dato] | [Finalidad] | [Justificación] | [Roles] | [Cifrado/Enmascarado/etc.] | [Periodo] |

## 5.6 Especificación técnica de contratos de servicio

| Contrato | Versión | Esquema | Validaciones | Manejo de errores | Trazabilidad | Ubicación |
|---|---|---|---|---|---|---|
| [Nombre] | [Versión] | [JSON/XML/etc.] | [Reglas] | [Códigos y tratamiento] | [ID de correlación/logs] | [Enlace] |

---

# 6. Arquitectura de tecnología

## 6.1 Diagrama de despliegue

**Diagrama:** [Insertar enlace, imagen o referencia al modelo ArchiMate]

**Descripción:**  
[Describir ambientes, nodos, redes, servicios de infraestructura y ubicación de los componentes.]

## 6.2 Componentes tecnológicos

| ID | Componente | Tipo | Ambiente | Ubicación | Propósito | Disponibilidad | Escalabilidad |
|---|---|---|---|---|---|---|---|
| TEC-01 | [Componente] | [Servidor/Servicio/Nube/Red/etc.] | [Desarrollo/Pruebas/Producción] | [Ubicación] | [Propósito] | [Objetivo] | [Mecanismo] |

## 6.3 Conectividad

| Origen | Destino | Puerto / Protocolo | Dirección | Seguridad | Responsable |
|---|---|---|---|---|---|
| [Origen] | [Destino] | [Puerto/Protocolo] | [Entrada/Salida/Bidireccional] | [Control] | [Área] |

## 6.4 Ambientes y despliegue

| Ambiente | Propósito | Componentes | Datos permitidos | Método de despliegue | Aprobador |
|---|---|---|---|---|---|
| [Ambiente] | [Propósito] | [Componentes] | [Tipo de datos] | [Manual/Automatizado] | [Rol] |

## 6.5 Continuidad, respaldo y recuperación

| Componente | Respaldo | RPO | RTO | Alta disponibilidad | Prueba de recuperación |
|---|---|---|---|---|---|
| [Componente] | [Estrategia] | [Objetivo] | [Objetivo] | [Diseño] | [Frecuencia] |

## 6.6 Monitoreo y observabilidad

| Componente / Flujo | Métrica o evento | Umbral | Alerta | Responsable | Retención |
|---|---|---|---|---|---|
| [Componente] | [Métrica] | [Umbral] | [Canal] | [Responsable] | [Periodo] |

## 6.7 Capacidad y rendimiento

| Componente | Volumen esperado | Pico | Tiempo de respuesta | Crecimiento | Estrategia de capacidad |
|---|---|---|---|---|---|
| [Componente] | [Volumen] | [Pico] | [Objetivo] | [% o periodo] | [Estrategia] |

---

# 7. Seguridad y cumplimiento

## 7.1 Identidad y control de acceso

| Componente | Tipo de identidad | Autenticación | Autorización | Roles | Responsable |
|---|---|---|---|---|---|
| [Componente] | [Usuario/Servicio] | [Método] | [Método] | [Roles] | [Área] |

## 7.2 Controles de seguridad

| ID | Riesgo / Requisito | Control | Capa | Evidencia | Responsable |
|---|---|---|---|---|---|
| SEG-01 | [Riesgo] | [Control] | [Aplicación/Datos/Red/Infraestructura] | [Evidencia] | [Responsable] |

## 7.3 Registro y auditoría

| Evento auditado | Fuente | Datos registrados | Retención | Acceso | Alerta asociada |
|---|---|---|---|---|---|
| [Evento] | [Sistema] | [Datos] | [Periodo] | [Roles] | [Alerta] |

## 7.4 Cumplimiento

| Norma / Política | Aplicabilidad | Requisito | Evidencia | Responsable | Estado |
|---|---|---|---|---|---|
| [Norma] | [Justificación] | [Requisito] | [Evidencia] | [Responsable] | [Cumple/Pendiente/No aplica] |

---

# 8. Requisitos no funcionales

| ID | Categoría | Requisito medible | Criterio de aceptación | Prioridad | Responsable |
|---|---|---|---|---|---|
| RNF-01 | [Disponibilidad/Rendimiento/Seguridad/etc.] | [Requisito] | [Criterio] | [Alta/Media/Baja] | [Responsable] |

---

# 9. Decisiones de arquitectura

| ID | Decisión | Contexto | Alternativas consideradas | Justificación | Consecuencias | Estado | Fecha |
|---|---|---|---|---|---|---|---|
| ADR-01 | [Decisión] | [Contexto] | [Alternativas] | [Justificación] | [Positivas y negativas] | [Propuesta/Aprobada/Rechazada] | [dd/mm/aaaa] |

---

# 10. Brechas y plan de transición

## 10.1 Análisis de brechas

| ID | Dominio | Estado actual | Estado objetivo | Brecha | Acción requerida | Prioridad |
|---|---|---|---|---|---|---|
| GAP-01 | [Negocio/Datos/Aplicaciones/Tecnología] | [AS-IS] | [TO-BE] | [Brecha] | [Acción] | [Alta/Media/Baja] |

## 10.2 Plan de transición

| Fase | Acción | Entregable | Dependencia | Responsable | Fecha objetivo | Criterio de cierre |
|---|---|---|---|---|---|---|
| [Fase] | [Acción] | [Entregable] | [Dependencia] | [Responsable] | [Fecha] | [Criterio] |

---

# 11. Gestión del cambio

## 11.1 Solicitud y control del cambio

> Todo cambio sobre el alcance o la arquitectura aprobada debe iniciar mediante el mecanismo corporativo de solicitud de cambio vigente, por ejemplo, RAW.

| ID de cambio | Descripción | Motivo | Impacto | Solicitante | Aprobador | Estado |
|---|---|---|---|---|---|---|
| [ID] | [Descripción] | [Motivo] | [Impacto] | [Nombre] | [Nombre] | [Estado] |

## 11.2 Impacto organizacional

| Grupo afectado | Cambio | Impacto | Comunicación | Capacitación | Responsable |
|---|---|---|---|---|---|
| [Grupo] | [Cambio] | [Impacto] | [Plan] | [Necesidad] | [Responsable] |

---

# 12. Riesgos consolidados

| ID | Dominio | Riesgo | Probabilidad | Impacto | Nivel | Mitigación | Contingencia | Responsable | Estado |
|---|---|---|---|---|---|---|---|---|---|
| RSK-01 | [Dominio] | [Riesgo] | [Baja/Media/Alta] | [Bajo/Medio/Alto] | [Nivel] | [Mitigación] | [Contingencia] | [Responsable] | [Estado] |

---

# 13. Pendientes y definiciones requeridas

| ID | Pendiente / Definición | Responsable | Fecha compromiso | Impacto si no se resuelve | Estado |
|---|---|---|---|---|---|
| PEN-01 | [Pendiente] | [Responsable] | [Fecha] | [Impacto] | [Abierto/Cerrado] |

---

# 14. Conclusiones y recomendaciones

[Resumir la viabilidad de la arquitectura, sus beneficios, condiciones de implementación, riesgos principales y acciones recomendadas.]

---

# 15. Aprobaciones y firmas

| Participante | Rol | Área / Organización | Decisión | Observaciones | Fecha | Firma / Evidencia |
|---|---|---|---|---|---|---|
| [Nombre] | [Rol] | [Área] | [Aprobado / Aprobado con observaciones / Rechazado] | [Observaciones] | [dd/mm/aaaa] | [Firma o enlace] |

---

# 16. Anexos

## Anexo A. Diagramas

- [Mapa de interesados]
- [Cadena de valor]
- [Evaluación de capacidades]
- [Proceso BPMN]
- [Arquitectura AS-IS]
- [Arquitectura TO-BE]
- [Intercambio de información]
- [Modelo de datos]
- [Diagrama de despliegue]

## Anexo B. Catálogo de referencias

| Referencia | Uso en el documento | Ubicación |
|---|---|---|
| TM Forum ODA Component Directory | Referencia para Building Blocks | https://www.tmforum.org/oda/directory/components-map |
| TM Forum Information Framework | Referencia para modelos de datos | https://www.tmforum.org/oda/moda/ |
| TOGAF | Método de arquitectura empresarial | [Ubicación autorizada] |
| ArchiMate | Lenguaje de modelado de arquitectura | [Ubicación autorizada] |
| eTOM | Referencia para procesos y capacidades | [Ubicación autorizada] |

## Anexo C. Glosario

| Término | Definición |
|---|---|
| ADD | Architecture Definition Document |
| AS-IS | Situación actual de la arquitectura |
| TO-BE | Situación objetivo de la arquitectura |
| BPMN | Notación utilizada para modelar procesos de negocio |
| SLA | Acuerdo de nivel de servicio |
| RPO | Pérdida máxima de datos aceptable, expresada en tiempo |
| RTO | Tiempo máximo esperado para recuperar el servicio |

## Anexo D. Lista de verificación de entrega

- [ ] El alcance y las exclusiones están claramente definidos.
- [ ] Los objetivos de negocio son medibles.
- [ ] Los interesados y responsables fueron identificados.
- [ ] La cadena de valor y las capacidades afectadas fueron analizadas.
- [ ] Las arquitecturas AS-IS y TO-BE están documentadas o justificadas.
- [ ] Los procesos, aplicaciones, integraciones y datos están identificados.
- [ ] El diagrama de despliegue y los ambientes están definidos.
- [ ] Los requisitos de seguridad y cumplimiento fueron revisados.
- [ ] Los requisitos no funcionales tienen criterios de aceptación.
- [ ] Los riesgos, restricciones, brechas y pendientes tienen responsables.
- [ ] Las decisiones de arquitectura están justificadas.
- [ ] El roadmap o plan de transición está definido cuando aplica.
- [ ] El documento cuenta con las aprobaciones requeridas.
