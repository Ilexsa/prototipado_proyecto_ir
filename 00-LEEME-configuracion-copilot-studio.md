# Agente "Arquitecto TOGAF – ADD" en Copilot Studio

Guía para montar el agente en Microsoft Copilot Studio usando el **GitHub Copilot harness** (agentes con Skills, sandbox Python y creación de archivos Word).

## 1. Diseño de la solución (por qué así)

| Componente | Qué lleva | Por qué |
|---|---|---|
| **Instrucciones** (`01-instrucciones-agente.md`) | Rol, flujo con las 3 paradas, nombres de las skills por fase, IDs de trazabilidad, reglas de honestidad y manejo de archivos | Se cargan en **todos** los turnos: solo lo que es verdad en toda la conversación |
| **4 Skills** (`skills/*.zip`) | El procedimiento detallado de cada fase, con referencias y scripts Python | Se cargan **bajo demanda**: el contexto se mantiene liviano y cada fase trae solo su guía |
| **Sandbox** (incluido en el harness) | Ejecuta los scripts: lee PDF/Word/OpenAPI, llena la plantilla Word, genera el HTML | Archivos exactos y repetibles, sin depender de que el modelo "escriba" un .docx |
| Knowledge (opcional) | Plantilla ADD oficial, principios corporativos, catálogo de building blocks | Evita subir la plantilla en cada caso |
| Tools (opcional) | Conector SharePoint/OneDrive para guardar entregables | El sandbox no tiene salida a red ni guarda archivos entre conversaciones |

**Cómo se "llama" una skill:** en Copilot Studio no se invocan directamente; el orquestador elige la skill comparando el mensaje con el **nombre y la descripción** de cada una. Por eso: (1) cada skill tiene una descripción tipo "enrutamiento" con cuándo usarla y cuándo NO, y (2) las instrucciones del agente nombran explícitamente la skill de cada fase ("Fase 1 → usa la skill **togaf-analisis-insumos**"). Es un puntero "suave": refuerza la selección, no la garantiza; se verifica en la vista de razonamiento (ver §5).

| Fase | Skill | Scripts incluidos | Entrega |
|---|---|---|---|
| 1 Análisis de insumos | `togaf-analisis-insumos` | `leer_insumos.py` (PDF, Word, OpenAPI YAML/JSON, Postman) | `01-analisis-insumos.md` |
| 🛑 Parada 1 | — (instrucciones) | — | Pide tu explicación |
| 2 Contraste + objetivo + brechas | `togaf-contraste-solucion` | — | `02-contraste-solucion.md` |
| 🛑 Parada 2 | — | — | Pide la plantilla Word |
| 3-4 Plantilla + ADD | `togaf-add-word` | `extraer_plantilla.py`, `llenar_plantilla.py`, `crear_add_base.py` | `ADD-<proyecto>.docx`, `vistas-plan.md` |
| 🛑 Parada 3 | — | — | ¿Pasamos a diagramas? |
| 5 Diagramas | `archimate-diagramas` | `generar_diagramas.py` + renderizador HTML | `diagramas_archimate.html`, `vistas.json` |

## 2. Requisitos previos (admin de Power Platform)

- Ambiente donde puedas crear agentes con el **GitHub Copilot harness**, con capacidad de **Copilot Credits** (este harness factura por uso, incluso en pruebas).
- Si quieres usar un modelo externo (p.ej. Anthropic), el admin debe habilitar modelos externos en Power Platform admin center y el proveedor en Microsoft 365 admin center. Ojo: modelos preview/experimentales o externos pueden procesar datos fuera de la región; valídalo con Seguridad antes de subir documentos internos.
- Políticas DLP que permitan los conectores opcionales que agregues.

## 3. Montaje paso a paso

1. **Crear el agente.** Inicio de Copilot Studio → crear **Agente** (no "Other ways to build", que es el harness estándar). Nombre sugerido: `Arquitecto TOGAF – ADD`. El harness no se puede cambiar después.
2. **Instrucciones.** Compilar → Instrucciones → pega el contenido de `01-instrucciones-agente.md` (≈4.400 caracteres) → Save.
3. **Modelo.** Compilar → Modelo → elige el modelo de razonamiento más capaz disponible en tu tenant que sea GA (evita preview en producción). Este flujo es largo y de mucho razonamiento; un modelo liviano pierde calidad en el contraste.
4. **Skills (en la interfaz en español: "Capacidades").** Compilar → Capacidades → **Agregar capacidad → Cargar una capacidad** → arrastra, uno por uno:
   - `skills/togaf-analisis-insumos.zip`
   - `skills/togaf-contraste-solucion.zip`
   - `skills/togaf-add-word.zip`
   - `skills/archimate-diagramas.zip`

   Sube siempre el **.zip**, no el `SKILL.md` suelto: el zip lleva también los scripts y las referencias. Cada zip tiene `SKILL.md` en la raíz. Revisa que cada capacidad muestre su nombre y descripción.

5. **Knowledge (opcional).** Si tienes plantilla ADD oficial o principios de arquitectura corporativos, agrégalos (SharePoint o archivos). Añade al final de las instrucciones: "Si el usuario no adjunta plantilla, usa la plantilla ADD oficial de Knowledge antes de generar una estándar."
6. **Tools (opcional).** Conector SharePoint u OneDrive para guardar entregables en una biblioteca del proyecto. Si lo agregas, añade a las instrucciones: "Al cerrar cada fase, ofrece guardar los archivos en <biblioteca> con la herramienta <nombre>."
7. **Memory.** Déjala **apagada**: los casos son independientes y la memoria no guarda archivos; evita arrastrar datos de un proyecto a otro.
8. **Verificar el sandbox (recomendado, una vez, en Versión preliminar).** Los scripts usan `python-docx`, `lxml`, `pdfplumber` (o `pypdf`) y `PyYAML` si hay YAML; no se puede hacer `pip install` en el sandbox. En Preview pide: "Ejecuta en Python: import docx, lxml, pdfplumber, yaml; imprime sus versiones". Si falta alguna: sin `pdfplumber` el lector usa `pypdf`; sin `yaml`, pide la especificación OpenAPI en JSON. Otra opción: la skill `agent-harness-explorer` del catálogo CAT genera un inventario completo del sandbox.
9. **Publicar** en Teams / Microsoft 365 Copilot. Comprueba en el canal elegido que el usuario puede **adjuntar archivos** y **descargar** los .docx/.html devueltos.

## 4. Cómo se usa (flujo para el arquitecto)

1. "Voy a elaborar el ADD del proyecto X" + adjunta brief, especificación técnica y especificación de la API.
2. Revisa las contradicciones y responde con tu solución e interpretación.
3. Ajusta el contraste; confirma.
4. Adjunta la plantilla Word del ADD (o pide la estándar).
5. Descarga el ADD; pide los diagramas; abre el HTML en el navegador y construye cada vista en tu herramienta (o importa el modelo con el XML Open Exchange y solo arma las vistas).

Guarda cada archivo entregado: si retomas en otra conversación, el agente te pedirá `01`, `02`, la plantilla o `vistas.json` según la fase.

## 5. Pruebas y depuración

- **Versión preliminar + vista de razonamiento:** confirma que en cada fase se carga la skill correcta. Si una skill no se activa, afina su `description` con las palabras que usan tus usuarios. Si se activa cuando no debe, añade más casos al "No la uses para…".
- **Evaluate:** carga los casos de `02-pruebas-evaluacion.csv` como conjunto de prueba (si el formato de importación difiere en tu versión, créalos manualmente).
- **Monitor:** revisa tareas, archivos accedidos y consumo de créditos.
- Casos a probar sí o sí: falta uno de los tres documentos; OpenAPI en YAML; plantilla con tablas vacías e instrucciones resaltadas; usuario que pide "haz el ADD directo" (debe pedir la explicación igual); cambio de un nombre de componente después del ADD (debe avisar que la vista cambia).

## 6. Límites conocidos

- El sandbox es temporal y sin salida a red: todo archivo se entrega como adjunto o se guarda con una Tool configurada.
- Las skills son por agente (viajan con él en soluciones/ALM). Si otro agente las necesita, súbelas también ahí.
- La exportación Open Exchange está pensada para Archi; verifica la importación en HOPEX u otra herramienta antes de depender de ella.
- Plantillas con controles de contenido complejos o campos protegidos pueden necesitar ajustes manuales finales en Word.
