# Vista 10 – Arquitectura de sistemas TO-BE: actores, proceso y aplicaciones

Vista bidimensional en dos capas, con el mismo esquema de tu boceto:

- **Capa de negocio:** los actores (BusinessActor) sobre el paso del proceso que ejecutan. Van desde el Usuario solicitante que abre el ticket hasta el Ingeniero de Procesos que comunica y cierra el ticket. El proceso **Actualización documental** agrupa los pasos 2 a 10.
- **Capa de aplicación:** solo componentes de aplicación (ApplicationComponent). La primera fila tiene los componentes que usan las personas; la segunda, los que soportan a los primeros. La tecnología (VPN, Blob Storage, Container Apps, redes) queda fuera de esta vista y está en la vista 09 Despliegue.
- Relaciones: Assignment (actor → paso), Triggering (secuencia del proceso), Serving (componente → paso que soporta) y Flow con nombre entre componentes.
- Viewpoint: *Application Usage*. Fase ADM: B–C.

## Actores de negocio

| Actor | Pasos | Qué hace |
| --- | --- | --- |
| Usuario solicitante | 1 | Detecta la necesidad y registra el ticket en SGP |
| Ingeniero de Procesos | 2, 4, 5, 6, 10, 11 | Valida, identifica el impacto, levanta, revisa y aprueba el borrador (HITL), carga el documento, comunica y cierra el ticket |
| Jefe de Ingeniería de Procesos | 3 | Asigna la solicitud |
| Áreas involucradas | 4, 5, 7 | Participan en el levantamiento y revisan el documento |
| Gerentes de las áreas | 8 | Aprueban el documento |
| Gerencias (Procesos, Operaciones e involucradas) | 9 | Revisan cambios, procesos e impacto |
| Administrador de OnBase | 10 | Publica el documento como vigente mediante el flujo de OnBase |

## Componentes de aplicación (explicación para el ADD)

| Componente | Estado | Qué es | Qué hace en el proceso | Pasos |
| --- | --- | --- | --- | --- |
| SGP | Existente, sin cambios | Sistema de tickets de solicitudes | Registra la solicitud; el Ingeniero cierra el ticket al final. Process One guarda la referencia al ticket | 1, 11 |
| Chatbot de Process One | Nuevo | Agente conversacional en Copilot Studio, disponible en Teams y web | Sugiere documentos potencialmente impactados y responde preguntas sobre los manuales con cita de documento y página. Usa el agente AG-16 | 4, 5 |
| Process One Web | Nuevo | Aplicación web del Ingeniero de Procesos | Registra la solicitud con su ticket, lanza el análisis, muestra hallazgos con evidencia, permite aprobar, observar o ajustar el borrador, registra la revisión de áreas y la aprobación de gerentes y ordena la carga | 6, 7, 8 |
| Backend de Process One | Nuevo | Lógica de negocio de la solución | Orquesta el análisis con los agentes, guarda solicitudes, borradores, iteraciones y aprobaciones, y solo pide la carga con aprobaciones completas y hash verificado | 6 a 10 (soporte) |
| Sistema multiagente (18 agentes) | Nuevo | Agentes de IA en Microsoft Foundry: orquestador, 16 especialistas y verificador | Analiza el manual, genera hallazgos citados y redacta el borrador; atiende al chatbot | 4, 5, 6 (soporte) |
| Azure AI Search – índice RAG | Nuevo | Base de conocimiento documental | Indexa automáticamente los documentos que llegan de OnBase (OCR, enriquecimiento, embeddings) y entrega fragmentos con cita a los agentes | 4, 5, 6 (soporte) |
| API de Ingesta de OnBase | Nuevo | Único punto de integración con OnBase desde Azure | Extrae documentos respetando la cuota de 450 llamadas por hora y carga el documento aprobado como revisión no vigente | 10 y carga del rezago |
| API Gateway (fachada TMF667 v4) | Existente, se configura | Plataforma corporativa de APIs | Expone OnBase como API TMF667 Document Management v4, o hace de proxy de los servicios SOAP, con cuota, mTLS y auditoría | 10 y extracción |
| OnBase | Existente | Repositorio documental oficial | Entrega los documentos y recibe el documento aprobado como revisión no vigente; lo publica como vigente mediante su flujo | 10 |
| Correo corporativo | Existente | Correo institucional | Comunicación formal de la actualización | 11 |

Pie sugerido en el Word (sección 4.1 o 4.3):
*"Figura N. Arquitectura de sistemas TO-BE: actores, proceso de actualización documental y componentes de aplicación (vista ArchiMate 10)"*.

## Cómo cargarla en Archi

**Recomendado:** importa `ProcessOne_ArchiMate_v0.9.3.xml` con **File → Import → Open Exchange XML Model…**. Trae las 10 vistas; la 10 reemplaza a la versión anterior.

**Si ya modificaste tu modelo en Archi**, expórtalo (**File → Export → Model to Open Exchange File…**) y pega estos tres bloques:

**C1 – antes de `</elements>`** (9 elementos nuevos: 7 actores, el proceso "Actualización documental" y "Correo corporativo")
```xml
    <element identifier="id-act_sol" xsi:type="BusinessActor">
      <name xml:lang="es">Usuario solicitante</name>
      <documentation xml:lang="es">Colaborador o área que detecta la necesidad y registra el ticket en SGP.</documentation>
    </element>
    <element identifier="id-act_ip" xsi:type="BusinessActor">
      <name xml:lang="es">Ingeniero de Procesos</name>
      <documentation xml:lang="es">Valida, identifica impacto, levanta, revisa y aprueba el borrador (HITL), carga el documento y cierra el ticket.</documentation>
    </element>
    <element identifier="id-act_jip" xsi:type="BusinessActor">
      <name xml:lang="es">Jefe de Ingeniería de Procesos</name>
      <documentation xml:lang="es">Asigna la solicitud a un Ingeniero de Procesos y da seguimiento.</documentation>
    </element>
    <element identifier="id-act_area" xsi:type="BusinessActor">
      <name xml:lang="es">Áreas involucradas</name>
      <documentation xml:lang="es">Participan en el levantamiento y revisan el documento generado por Process One.</documentation>
    </element>
    <element identifier="id-act_ger" xsi:type="BusinessActor">
      <name xml:lang="es">Gerentes de las áreas</name>
      <documentation xml:lang="es">Aprueban el documento revisado.</documentation>
    </element>
    <element identifier="id-act_gcias" xsi:type="BusinessActor">
      <name xml:lang="es">Gerencias (Procesos, Operaciones e involucradas)</name>
      <documentation xml:lang="es">Revisan cambios, procesos e impacto en la socialización.</documentation>
    </element>
    <element identifier="id-act_aob" xsi:type="BusinessActor">
      <name xml:lang="es">Administrador de OnBase</name>
      <documentation xml:lang="es">Custodia el repositorio y publica el documento como vigente mediante el flujo de OnBase.</documentation>
    </element>
    <element identifier="id-ac_correo" xsi:type="ApplicationComponent">
      <name xml:lang="es">Correo corporativo</name>
      <documentation xml:lang="es">Canal de la comunicación formal de la actualización (paso 11).</documentation>
    </element>
    <element identifier="id-bp_doc" xsi:type="BusinessProcess">
      <name xml:lang="es">Actualización documental</name>
      <documentation xml:lang="es">Pasos 2 a 10 del proceso de actualización de procesos y manuales, enriquecidos por Process One.</documentation>
    </element>
```

**C2 – antes de `</relationships>`** (40 relaciones nuevas)
```xml
    <relationship identifier="id-r-ass-act_sol-p01" source="id-act_sol" target="id-p01" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_ip-p02" source="id-act_ip" target="id-p02" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_jip-p03" source="id-act_jip" target="id-p03" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_ip-p04" source="id-act_ip" target="id-p04" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_ip-p05" source="id-act_ip" target="id-p05" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_ip-p06" source="id-act_ip" target="id-p06" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_area-p07" source="id-act_area" target="id-p07" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_ger-p08" source="id-act_ger" target="id-p08" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_gcias-p09" source="id-act_gcias" target="id-p09" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_ip-p10" source="id-act_ip" target="id-p10" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_aob-p10" source="id-act_aob" target="id-p10" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_ip-p11" source="id-act_ip" target="id-p11" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_area-p04" source="id-act_area" target="id-p04" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_area-p05" source="id-act_area" target="id-p05" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_ip-rol_ip" source="id-act_ip" target="id-rol_ip" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_jip-rol_jip" source="id-act_jip" target="id-rol_jip" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_sol-rol_sol" source="id-act_sol" target="id-rol_sol" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_area-rol_area" source="id-act_area" target="id-rol_area" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_ger-rol_ger" source="id-act_ger" target="id-rol_ger" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_gcias-rol_gcias" source="id-act_gcias" target="id-rol_gcias" xsi:type="Assignment" />
    <relationship identifier="id-r-ass-act_aob-rol_aob" source="id-act_aob" target="id-rol_aob" xsi:type="Assignment" />
    <relationship identifier="id-r-com-bp_doc-p02" source="id-bp_doc" target="id-p02" xsi:type="Composition" />
    <relationship identifier="id-r-com-bp_doc-p03" source="id-bp_doc" target="id-p03" xsi:type="Composition" />
    <relationship identifier="id-r-com-bp_doc-p04" source="id-bp_doc" target="id-p04" xsi:type="Composition" />
    <relationship identifier="id-r-com-bp_doc-p05" source="id-bp_doc" target="id-p05" xsi:type="Composition" />
    <relationship identifier="id-r-com-bp_doc-p06" source="id-bp_doc" target="id-p06" xsi:type="Composition" />
    <relationship identifier="id-r-com-bp_doc-p07" source="id-bp_doc" target="id-p07" xsi:type="Composition" />
    <relationship identifier="id-r-com-bp_doc-p08" source="id-bp_doc" target="id-p08" xsi:type="Composition" />
    <relationship identifier="id-r-com-bp_doc-p09" source="id-bp_doc" target="id-p09" xsi:type="Composition" />
    <relationship identifier="id-r-com-bp_doc-p10" source="id-bp_doc" target="id-p10" xsi:type="Composition" />
    <relationship identifier="id-r-ser-ac_sgp-p01" source="id-ac_sgp" target="id-p01" xsi:type="Serving" />
    <relationship identifier="id-r-ser-ac_sgp-p11" source="id-ac_sgp" target="id-p11" xsi:type="Serving" />
    <relationship identifier="id-r-ser-ac_cbot-p04" source="id-ac_cbot" target="id-p04" xsi:type="Serving" />
    <relationship identifier="id-r-ser-ac_cbot-p05" source="id-ac_cbot" target="id-p05" xsi:type="Serving" />
    <relationship identifier="id-r-ser-ac_web-p06" source="id-ac_web" target="id-p06" xsi:type="Serving" />
    <relationship identifier="id-r-ser-ac_web-p07" source="id-ac_web" target="id-p07" xsi:type="Serving" />
    <relationship identifier="id-r-ser-ac_web-p08" source="id-ac_web" target="id-p08" xsi:type="Serving" />
    <relationship identifier="id-r-ser-ac_ing-p10" source="id-ac_ing" target="id-p10" xsi:type="Serving" />
    <relationship identifier="id-r-ser-ac_onb-p10" source="id-ac_onb" target="id-p10" xsi:type="Serving" />
    <relationship identifier="id-r-ser-ac_correo-p11" source="id-ac_correo" target="id-p11" xsi:type="Serving" />
```

**C3 – antes de `</diagrams>`** (la vista; si ya pegaste la versión anterior de la vista 10, bórrala antes)
```xml
      <view identifier="id-v-v10" xsi:type="Diagram" viewpoint="Application Usage">
        <name xml:lang="es">10 Arquitectura de sistemas TO-BE – actores, proceso y aplicaciones</name>
        <documentation xml:lang="es">Preocupación: quién interviene en cada paso y qué aplicación lo soporta. Capa de negocio: actores y proceso de actualización documental. Capa de aplicación: solo componentes de aplicación (la tecnología está en la vista 09). Fase ADM: B–C.</documentation>
        <node identifier="id-v-v10-n-act_sol" elementRef="id-act_sol" xsi:type="Element" x="58" y="36" w="137" h="55">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-act_ip-2" elementRef="id-act_ip" xsi:type="Element" x="282" y="36" w="137" h="55">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-act_jip" elementRef="id-act_jip" xsi:type="Element" x="442" y="36" w="137" h="55">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-act_ip-4" elementRef="id-act_ip" xsi:type="Element" x="602" y="36" w="137" h="55">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-act_ip-5" elementRef="id-act_ip" xsi:type="Element" x="762" y="36" w="137" h="55">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-act_ip-6" elementRef="id-act_ip" xsi:type="Element" x="922" y="36" w="137" h="55">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-act_area" elementRef="id-act_area" xsi:type="Element" x="1082" y="36" w="137" h="55">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-act_ger" elementRef="id-act_ger" xsi:type="Element" x="1242" y="36" w="137" h="55">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-act_gcias" elementRef="id-act_gcias" xsi:type="Element" x="1402" y="30" w="137" h="68">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-act_aob" elementRef="id-act_aob" xsi:type="Element" x="1562" y="36" w="137" h="55">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-act_ip-11" elementRef="id-act_ip" xsi:type="Element" x="1786" y="36" w="137" h="55">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-p01" elementRef="id-p01" xsi:type="Element" x="58" y="185" w="137" h="68">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-bp_doc" elementRef="id-bp_doc" xsi:type="Element" x="268" y="155" w="1445" h="112">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
          <node identifier="id-v-v10-n-p02" elementRef="id-p02" xsi:type="Element" x="282" y="192" w="137" h="55">
            <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
          </node>
          <node identifier="id-v-v10-n-p03" elementRef="id-p03" xsi:type="Element" x="442" y="185" w="137" h="68">
            <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
          </node>
          <node identifier="id-v-v10-n-p04" elementRef="id-p04" xsi:type="Element" x="602" y="185" w="137" h="68">
            <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
          </node>
          <node identifier="id-v-v10-n-p05" elementRef="id-p05" xsi:type="Element" x="762" y="192" w="137" h="55">
            <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
          </node>
          <node identifier="id-v-v10-n-p06" elementRef="id-p06" xsi:type="Element" x="922" y="185" w="137" h="68">
            <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
          </node>
          <node identifier="id-v-v10-n-p07" elementRef="id-p07" xsi:type="Element" x="1082" y="192" w="137" h="55">
            <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
          </node>
          <node identifier="id-v-v10-n-p08" elementRef="id-p08" xsi:type="Element" x="1242" y="192" w="137" h="55">
            <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
          </node>
          <node identifier="id-v-v10-n-p09" elementRef="id-p09" xsi:type="Element" x="1402" y="192" w="137" h="55">
            <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
          </node>
          <node identifier="id-v-v10-n-p10" elementRef="id-p10" xsi:type="Element" x="1562" y="192" w="137" h="55">
            <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
          </node>
        </node>
        <node identifier="id-v-v10-n-p11" elementRef="id-p11" xsi:type="Element" x="1786" y="185" w="137" h="68">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ev_fin" elementRef="id-ev_fin" xsi:type="Element" x="1978" y="185" w="137" h="68">
          <style><fillColor r="255" g="255" b="181" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ac_sgp" elementRef="id-ac_sgp" xsi:type="Element" x="58" y="366" w="137" h="55">
          <style><fillColor r="181" g="255" b="255" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ac_cbot" elementRef="id-ac_cbot" xsi:type="Element" x="682" y="366" w="137" h="55">
          <style><fillColor r="181" g="255" b="255" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ac_web" elementRef="id-ac_web" xsi:type="Element" x="1082" y="366" w="137" h="55">
          <style><fillColor r="181" g="255" b="255" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ac_onb" elementRef="id-ac_onb" xsi:type="Element" x="1562" y="366" w="137" h="55">
          <style><fillColor r="181" g="255" b="255" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ac_correo" elementRef="id-ac_correo" xsi:type="Element" x="1786" y="366" w="137" h="55">
          <style><fillColor r="181" g="255" b="255" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ac_sgp-2" elementRef="id-ac_sgp" xsi:type="Element" x="1978" y="366" w="137" h="55">
          <style><fillColor r="181" g="255" b="255" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ac_srch" elementRef="id-ac_srch" xsi:type="Element" x="602" y="496" w="137" h="55">
          <style><fillColor r="181" g="255" b="255" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ac_mas" elementRef="id-ac_mas" xsi:type="Element" x="842" y="496" w="137" h="55">
          <style><fillColor r="181" g="255" b="255" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ac_back" elementRef="id-ac_back" xsi:type="Element" x="1082" y="496" w="137" h="55">
          <style><fillColor r="181" g="255" b="255" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ac_ing" elementRef="id-ac_ing" xsi:type="Element" x="1322" y="496" w="137" h="55">
          <style><fillColor r="181" g="255" b="255" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <node identifier="id-v-v10-n-ac_gw" elementRef="id-ac_gw" xsi:type="Element" x="1562" y="496" w="137" h="55">
          <style><fillColor r="181" g="255" b="255" /><lineColor r="92" g="92" b="92" /><font name="Segoe UI" size="9"><color r="0" g="0" b="0" /></font></style>
        </node>
        <connection identifier="id-v-v10-c-act_sol-p01-ass" relationshipRef="id-r-ass-act_sol-p01" xsi:type="Relationship" source="id-v-v10-n-act_sol" target="id-v-v10-n-p01">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-act_ip-2-p02-ass" relationshipRef="id-r-ass-act_ip-p02" xsi:type="Relationship" source="id-v-v10-n-act_ip-2" target="id-v-v10-n-p02">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-act_jip-p03-ass" relationshipRef="id-r-ass-act_jip-p03" xsi:type="Relationship" source="id-v-v10-n-act_jip" target="id-v-v10-n-p03">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-act_ip-4-p04-ass" relationshipRef="id-r-ass-act_ip-p04" xsi:type="Relationship" source="id-v-v10-n-act_ip-4" target="id-v-v10-n-p04">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-act_ip-5-p05-ass" relationshipRef="id-r-ass-act_ip-p05" xsi:type="Relationship" source="id-v-v10-n-act_ip-5" target="id-v-v10-n-p05">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-act_ip-6-p06-ass" relationshipRef="id-r-ass-act_ip-p06" xsi:type="Relationship" source="id-v-v10-n-act_ip-6" target="id-v-v10-n-p06">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-act_area-p07-ass" relationshipRef="id-r-ass-act_area-p07" xsi:type="Relationship" source="id-v-v10-n-act_area" target="id-v-v10-n-p07">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-act_ger-p08-ass" relationshipRef="id-r-ass-act_ger-p08" xsi:type="Relationship" source="id-v-v10-n-act_ger" target="id-v-v10-n-p08">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-act_gcias-p09-ass" relationshipRef="id-r-ass-act_gcias-p09" xsi:type="Relationship" source="id-v-v10-n-act_gcias" target="id-v-v10-n-p09">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-act_aob-p10-ass" relationshipRef="id-r-ass-act_aob-p10" xsi:type="Relationship" source="id-v-v10-n-act_aob" target="id-v-v10-n-p10">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-act_ip-11-p11-ass" relationshipRef="id-r-ass-act_ip-p11" xsi:type="Relationship" source="id-v-v10-n-act_ip-11" target="id-v-v10-n-p11">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-p01-p02-tri" relationshipRef="id-r-tri-p01-p02" xsi:type="Relationship" source="id-v-v10-n-p01" target="id-v-v10-n-p02">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-p02-p03-tri" relationshipRef="id-r-tri-p02-p03" xsi:type="Relationship" source="id-v-v10-n-p02" target="id-v-v10-n-p03">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-p03-p04-tri" relationshipRef="id-r-tri-p03-p04" xsi:type="Relationship" source="id-v-v10-n-p03" target="id-v-v10-n-p04">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-p04-p05-tri" relationshipRef="id-r-tri-p04-p05" xsi:type="Relationship" source="id-v-v10-n-p04" target="id-v-v10-n-p05">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-p05-p06-tri" relationshipRef="id-r-tri-p05-p06" xsi:type="Relationship" source="id-v-v10-n-p05" target="id-v-v10-n-p06">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-p06-p07-tri" relationshipRef="id-r-tri-p06-p07" xsi:type="Relationship" source="id-v-v10-n-p06" target="id-v-v10-n-p07">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-p07-p08-tri" relationshipRef="id-r-tri-p07-p08" xsi:type="Relationship" source="id-v-v10-n-p07" target="id-v-v10-n-p08">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-p08-p09-tri" relationshipRef="id-r-tri-p08-p09" xsi:type="Relationship" source="id-v-v10-n-p08" target="id-v-v10-n-p09">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-p09-p10-tri" relationshipRef="id-r-tri-p09-p10" xsi:type="Relationship" source="id-v-v10-n-p09" target="id-v-v10-n-p10">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-p10-p11-tri" relationshipRef="id-r-tri-p10-p11" xsi:type="Relationship" source="id-v-v10-n-p10" target="id-v-v10-n-p11">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-p11-ev_fin-tri" relationshipRef="id-r-tri-p11-ev_fin" xsi:type="Relationship" source="id-v-v10-n-p11" target="id-v-v10-n-ev_fin">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_sgp-p01-ser" relationshipRef="id-r-ser-ac_sgp-p01" xsi:type="Relationship" source="id-v-v10-n-ac_sgp" target="id-v-v10-n-p01">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_cbot-p04-ser" relationshipRef="id-r-ser-ac_cbot-p04" xsi:type="Relationship" source="id-v-v10-n-ac_cbot" target="id-v-v10-n-p04">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_cbot-p05-ser" relationshipRef="id-r-ser-ac_cbot-p05" xsi:type="Relationship" source="id-v-v10-n-ac_cbot" target="id-v-v10-n-p05">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_web-p06-ser" relationshipRef="id-r-ser-ac_web-p06" xsi:type="Relationship" source="id-v-v10-n-ac_web" target="id-v-v10-n-p06">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_web-p07-ser" relationshipRef="id-r-ser-ac_web-p07" xsi:type="Relationship" source="id-v-v10-n-ac_web" target="id-v-v10-n-p07">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_web-p08-ser" relationshipRef="id-r-ser-ac_web-p08" xsi:type="Relationship" source="id-v-v10-n-ac_web" target="id-v-v10-n-p08">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_onb-p10-ser" relationshipRef="id-r-ser-ac_onb-p10" xsi:type="Relationship" source="id-v-v10-n-ac_onb" target="id-v-v10-n-p10">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_correo-p11-ser" relationshipRef="id-r-ser-ac_correo-p11" xsi:type="Relationship" source="id-v-v10-n-ac_correo" target="id-v-v10-n-p11">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_sgp-2-p11-ser" relationshipRef="id-r-ser-ac_sgp-p11" xsi:type="Relationship" source="id-v-v10-n-ac_sgp-2" target="id-v-v10-n-p11">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_ing-p10-ser" relationshipRef="id-r-ser-ac_ing-p10" xsi:type="Relationship" source="id-v-v10-n-ac_ing" target="id-v-v10-n-p10">
          <style><lineColor r="64" g="64" b="64" /></style>
          <bendpoint x="1390" y="304" />
        </connection>
        <connection identifier="id-v-v10-c-ac_web-ac_back-flo-Solicitud--decisiones-HITL" relationshipRef="id-r-flo-ac_web-ac_back-solicitud-decisiones" xsi:type="Relationship" source="id-v-v10-n-ac_web" target="id-v-v10-n-ac_back">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_mas-ac_back-flo-Hallazgos-y-borrador" relationshipRef="id-r-flo-ac_mas-ac_back-hallazgos-y-borrador" xsi:type="Relationship" source="id-v-v10-n-ac_mas" target="id-v-v10-n-ac_back">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_srch-ac_mas-flo-Fragmentos-con-cita" relationshipRef="id-r-flo-ac_srch-ac_mas-fragmentos-con-cita" xsi:type="Relationship" source="id-v-v10-n-ac_srch" target="id-v-v10-n-ac_mas">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_mas-ac_cbot-flo-Respuesta-con-cita--AG-16-" relationshipRef="id-r-flo-ac_mas-ac_cbot-respuesta-con-cita-a" xsi:type="Relationship" source="id-v-v10-n-ac_mas" target="id-v-v10-n-ac_cbot">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_back-ac_ing-flo-Documento-aprobado" relationshipRef="id-r-flo-ac_back-ac_ing-documento-aprobado" xsi:type="Relationship" source="id-v-v10-n-ac_back" target="id-v-v10-n-ac_ing">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_ing-ac_srch-flo-Binario---metadatos--v-a-Blob-" relationshipRef="id-r-flo-ac_ing-ac_srch-binario-metadatos-v" xsi:type="Relationship" source="id-v-v10-n-ac_ing" target="id-v-v10-n-ac_srch">
          <style><lineColor r="64" g="64" b="64" /></style>
          <bendpoint x="1390" y="604" />
          <bendpoint x="670" y="604" />
        </connection>
        <connection identifier="id-v-v10-c-ac_gw-ac_ing-flo-Document--TMF667-" relationshipRef="id-r-flo-ac_gw-ac_ing-document-tmf667" xsi:type="Relationship" source="id-v-v10-n-ac_gw" target="id-v-v10-n-ac_ing">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
        <connection identifier="id-v-v10-c-ac_onb-ac_gw-flo-Documento--SOAP-" relationshipRef="id-r-flo-ac_onb-ac_gw-documento-soap" xsi:type="Relationship" source="id-v-v10-n-ac_onb" target="id-v-v10-n-ac_gw">
          <style><lineColor r="64" g="64" b="64" /></style>
        </connection>
      </view>
```

Cambios opcionales en elementos existentes (en la versión completa ya están aplicados):
- El paso 11 pasa a llamarse "11. Comunicación formal y cierre del ticket".
- Los componentes ahora tienen documentación con la descripción de la tabla anterior. En Archi aparece en la pestaña Properties → Documentation.
