import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Circle, Rectangle
import textwrap

BW, BH = 1.22, 0.74   # tamaño de tarea (unidades)
def draw(lanes, steps, edges, out, title, colw=1.3, laneh=1.0, p1_lanes=()):
    steps = {k: (v[0], v[1] * 1.12 if v[1] > 0 else -0.2) + tuple(v[2:]) for k, v in steps.items()}
    xs = [s[1] for s in steps.values()]
    X0, X1 = -1.75, max(xs) + 0.9
    H = len(lanes) * laneh
    fig = plt.figure(figsize=((X1 - X0) * 0.62, H * 0.62 + 0.45), dpi=220)
    ax = fig.add_axes([0, 0, 1, (H * 0.62) / (H * 0.62 + 0.45)])
    ax.set_xlim(X0, X1); ax.set_ylim(H, 0); ax.axis('off')
    fig.text(0.005, 0.995, title, ha='left', va='top', fontsize=9, weight='bold', color='#1F3864')
    for i, ln in enumerate(lanes):
        fc = '#EAF3FC' if i in p1_lanes else ('#FFFFFF' if i % 2 == 0 else '#F6F6F6')
        ax.add_patch(Rectangle((X0, i * laneh), X1 - X0, laneh, fc=fc, ec='#9E9E9E', lw=0.6))
        ax.add_patch(Rectangle((X0, i * laneh), 1.3, laneh, fc='#0078D4' if i in p1_lanes else '#1F3864', ec='#9E9E9E', lw=0.6))
        ax.text(X0 + 0.65, (i + 0.5) * laneh, '\n'.join(textwrap.wrap(ln, 15)), ha='center', va='center', fontsize=5.0, color='white', weight='bold')
    geo = {}
    for k, (lane, x, txt, kind, *dy) in steps.items():
        y = (lane + 0.5) * laneh + (dy[0] if dy else 0)
        if kind in ('start', 'end'):
            ax.add_patch(Circle((x, y), 0.14, fc='#FFFFFF' if kind == 'start' else '#1F3864', ec='#1F3864', lw=1.4 if kind == 'start' else 0.8, zorder=3))
            if kind == 'end': ax.add_patch(Circle((x, y), 0.09, fc='#1F3864', ec='white', lw=0.8, zorder=4))
            if txt: ax.text(x + 0.2, y, '\n'.join(textwrap.wrap(txt, 14)), ha='left', va='center', fontsize=4.3, color='#333')
            geo[k] = (x, y, 0.14, 0.14)
        elif kind == 'conn':
            ax.add_patch(Circle((x, y), 0.17, fc='#FFFFFF', ec='#C0392B', lw=1.2, zorder=3))
            ax.text(x, y, txt, ha='center', va='center', fontsize=6, weight='bold', color='#C0392B', zorder=4)
            geo[k] = (x, y, 0.17, 0.17)
        elif kind == 'dec':
            d = 0.27
            ax.add_patch(Polygon([(x - d, y), (x, y - d), (x + d, y), (x, y + d)], fc='#FFF7E0', ec='#C9A227', lw=0.9, zorder=3))
            ax.text(x, y - d - 0.03, txt, ha='center', va='bottom', fontsize=4.8, color='#5A4600')
            geo[k] = (x, y, d, d)
        else:
            fc = {'task': '#FFFFFF', 'p1': '#C2E0F7', 'sys': '#FFE9C7', 'part': '#F2F2F2'}[kind]
            ec = {'task': '#1F3864', 'p1': '#0078D4', 'sys': '#B7791F', 'part': '#9E9E9E'}[kind]
            ax.add_patch(FancyBboxPatch((x - BW / 2, y - BH / 2), BW, BH, boxstyle='round,pad=0,rounding_size=0.06', fc=fc, ec=ec, lw=0.9 if kind != 'part' else 0.6, ls='-' if kind != 'part' else (0, (2, 1.5)), zorder=3))
            ax.text(x, y, '\n'.join(textwrap.wrap(txt, 21)), ha='center', va='center', fontsize=4.4, zorder=4, wrap=True)
            geo[k] = (x, y, BW / 2, BH / 2)
    for e in edges:
        a, b = e[0], e[1]; lab = e[2] if len(e) > 2 else ''; st = e[3] if len(e) > 3 else 'seq'; via = e[4] if len(e) > 4 else None
        ax_, ay, aw, ah = geo[a]; bx, by, bw, bh = geo[b]
        if via is not None:   # retorno por debajo/encima: via = y del tramo horizontal
            pts = [(ax_, ay + (ah if via > ay else -ah)), (ax_, via), (bx, via), (bx, by + (bh if via > by else -bh))]
        elif abs(ay - by) < 1e-6:
            pts = [(ax_ + aw, ay), (bx - bw, by)] if bx > ax_ else [(ax_ - aw, ay), (bx + bw, by)]
        elif abs(ax_ - bx) < 1e-6:
            pts = [(ax_, ay + (ah if by > ay else -ah)), (bx, by + (-bh if by > ay else bh))]
        else:
            pts = [(ax_ + aw, ay), (bx, ay), (bx, by + (-bh if by > ay else bh))]
        col, ls, lw, head = {'seq': ('#303030', '-', 0.8, '-|>'), 'con': ('#0078D4', (0, (3, 2)), 0.8, '<|-|>'), 'par': ('#8A8A8A', (0, (1.5, 1.5)), 0.6, '-')}[st]
        xs_, ys_ = zip(*pts)
        ax.plot(xs_[:-1] + (xs_[-1],), ys_, color=col, ls=ls, lw=lw, zorder=2)
        if head != '-':
            ax.annotate('', xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle=head, color=col, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=5), zorder=5)
        if lab:
            mx, my = (pts[len(pts) // 2 - 1][0] + pts[len(pts) // 2][0]) / 2, (pts[len(pts) // 2 - 1][1] + pts[len(pts) // 2][1]) / 2
            ax.text(mx, my - 0.04, lab, ha='center', va='bottom', fontsize=4.3, color=col, bbox=dict(fc='white', ec='none', pad=0.3), zorder=6)
    fig.savefig(out, facecolor='white'); plt.close(fig)

def split(steps, edges, keys, conns):
    """keys: pasos incluidos; conns: {nombre: (lane, x, letra)}; aristas cuyo extremo quede fuera se redirigen al conector indicado."""
    st = {k: v for k, v in steps.items() if k in keys}
    for c, (lane, x, letra) in conns.items(): st[c] = (lane, x, letra, 'conn')
    ed = []
    for e in edges:
        a, b = e[0], e[1]
        if a in keys and b in keys: ed.append(e)
        elif a in keys and ('out_' + b) in conns: ed.append((a, 'out_' + b) + tuple(e[2:3]))
        elif b in keys and ('in_' + a) in conns: ed.append(('in_' + a, b) + tuple(e[2:3]))
    xmin = min(v[1] for v in st.values())
    st = {k: (v[0], v[1] - xmin + 0.3) + tuple(v[2:]) for k, v in st.items()}
    return st, ed
# ======================= AS-IS =======================
L = ['Solicitante (cualquier usuario)', 'Ingeniero de Procesos', 'Jefe de Ingeniería de Procesos', 'Áreas involucradas', 'Gerentes de las áreas',
     'Gerencias (Procesos, Operaciones e involucradas)', 'OnBase']
S = {'s': (0, -0.6, '', 'start'),
     'a1': (0, 0.8, '1. Genera ticket en SGP con la solicitud', 'task'),
     'a2': (1, 1.9, '2. Valida si la solicitud es real y procede', 'task'),
     'd2': (1, 3.0, '¿Procede?', 'dec'),
     'e0': (1, 3.0, 'Solicitud no procede', 'end', 0.36),
     'a3': (2, 4.1, '3. Asigna la solicitud a un Ingeniero de Procesos', 'task'),
     'a4': (1, 5.4, '4. Reunión con áreas: identifica áreas, procesos y manuales a modificar', 'task'),
     'p4': (3, 5.4, 'Participan en la reunión', 'part'),
     'a5': (1, 6.7, '5. Sesiones de levantamiento: necesidad, cambios, situación actual', 'task'),
     'p5': (3, 6.7, 'Usuarios y áreas participan', 'part'),
     'a6': (1, 8.0, '6. Analiza el manual y redacta el borrador manualmente', 'task'),
     'a7': (3, 9.3, '7. Revisan que los cambios reflejen lo acordado', 'task'),
     'a8': (4, 10.6, '8. Aprueban el documento', 'task'),
     'a9': (5, 11.9, '9. Socialización: cambios, procesos, áreas e impacto', 'task'),
     'a10': (6, 13.2, '10. Publicación del documento actualizado', 'sys'),
     'a11': (1, 14.5, '11. Correo formal comunicando la actualización', 'task'),
     'e': (1, 15.5, 'Documento actualizado y comunicado', 'end')}
Eg = [('s', 'a1'), ('a1', 'a2'), ('a2', 'd2'), ('d2', 'e0', 'No'), ('d2', 'a3', 'Sí'), ('a3', 'a4'), ('a4', 'p4', '', 'par'), ('a4', 'a5'), ('a5', 'p5', '', 'par'),
      ('a5', 'a6'), ('a6', 'a7'), ('a7', 'a8'), ('a8', 'a9'), ('a9', 'a10'), ('a10', 'a11'), ('a11', 'e')]
k1 = ['s','a1','a2','d2','e0','a3','a4','p4','a5','p5']
st, ed = split(S, Eg, k1, {'out_a6': (1, 7.9, 'A')})
draw(L, st, ed, '/home/claude/add/diag/asis_1.png', 'AS-IS (1/2) – pasos 1 a 5 (sin Process One)')
k2 = ['a6','a7','a8','a9','a10','a11','e']
st, ed = split(S, Eg, k2, {'in_a5': (1, 6.9, 'A')})
draw(L, st, ed, '/home/claude/add/diag/asis_2.png', 'AS-IS (2/2) – pasos 6 a 11 (sin Process One)')

# ======================= TO-BE =======================
L2 = ['Solicitante (cualquier usuario)', 'Ingeniero de Procesos', 'Jefe de Ingeniería de Procesos', 'Process One – Chatbot (Copilot Studio · AG-16)',
      'Process One – Análisis documental (multiagente + backend)', 'Áreas involucradas', 'Gerentes de las áreas', 'Gerencias (Procesos, Operaciones e involucradas)', 'OnBase']
S2 = {'s': (0, -0.6, '', 'start'),
      'a1': (0, 0.8, '1. Genera ticket en SGP con la solicitud', 'task'),
      'a2': (1, 1.9, '2. Valida si la solicitud es real y procede', 'task'),
      'd2': (1, 3.0, '¿Procede?', 'dec'),
      'e0': (1, 3.0, 'Solicitud no procede', 'end', 0.36),
      'a3': (2, 4.1, '3. Asigna la solicitud a un Ingeniero de Procesos', 'task'),
      'a4': (1, 5.4, '4. Reunión con áreas: identifica áreas, procesos y manuales a modificar', 'task'),
      'c4': (3, 5.4, 'Consulta manuales relacionados e identifica documentos potencialmente afectados', 'p1'),
      'p4': (5, 5.4, 'Participan en la reunión', 'part'),
      'a5': (1, 6.7, '5. Sesiones de levantamiento: necesidad, cambios, situación actual', 'task'),
      'c5': (3, 6.7, 'Consulta información de los manuales durante las sesiones', 'p1'),
      'p5': (5, 6.7, 'Usuarios y áreas participan', 'part'),
      'a6': (1, 8.0, '6. Solicita el análisis del manual a actualizar', 'task'),
      'm6': (4, 9.3, 'Analiza: correcciones, inconsistencias, cumplimiento de normas, mejoras → genera borrador', 'p1'),
      'r6': (1, 10.6, 'Revisa el borrador (Human in the Loop)', 'task'),
      'd6': (1, 11.7, '¿Aprobado?', 'dec'),
      'm7': (4, 12.8, 'Genera el documento actualizado aprobado', 'p1'),
      'a7': (5, 14.1, '7. Revisan que los cambios reflejen lo acordado', 'task'),
      'a8': (6, 15.4, '8. Aprueban el documento', 'task'),
      'a9': (7, 16.7, '9. Socialización: cambios, procesos, áreas e impacto', 'task'),
      'm10': (4, 18.0, '10. Carga el documento aprobado a OnBase (no sustituye la versión vigente)', 'p1'),
      'o10': (8, 19.3, 'Publicación como versión vigente según el flujo de OnBase', 'sys'),
      'a11': (1, 20.6, '11. Correo formal comunicando la actualización', 'task'),
      'e': (1, 21.6, 'Documento actualizado y comunicado', 'end')}
E2 = [('s', 'a1'), ('a1', 'a2'), ('a2', 'd2'), ('d2', 'e0', 'No'), ('d2', 'a3', 'Sí'), ('a3', 'a4'), ('a4', 'c4', 'consulta', 'con'), ('a4', 'p4', '', 'par'),
      ('a4', 'a5'), ('a5', 'c5', 'consulta', 'con'), ('a5', 'p5', '', 'par'), ('a5', 'a6'), ('a6', 'm6'), ('m6', 'r6'), ('r6', 'd6'),
      ('d6', 'm6', 'No: observaciones / ajustes directos', 'seq', 4.95), ('d6', 'm7', 'Sí'), ('m7', 'a7'), ('a7', 'a8'), ('a8', 'a9'), ('a9', 'm10'),
      ('m10', 'o10'), ('o10', 'a11'), ('a11', 'e')]
k1 = ['s','a1','a2','d2','e0','a3','a4','c4','p4','a5','c5','p5','a6','m6','r6','d6']
st, ed = split(S2, E2, k1, {'out_m7': (1, 12.7, 'B')})
draw(L2, st, ed, '/home/claude/add/diag/tobe_1.png', 'TO-BE (1/2) – pasos 1 a 6 con Process One', p1_lanes=(3, 4))
k2 = ['m7','a7','a8','a9','m10','o10','a11','e']
st, ed = split(S2, E2, k2, {'in_d6': (1, 11.8, 'B')})
draw(L2, st, ed, '/home/claude/add/diag/tobe_2.png', 'TO-BE (2/2) – pasos 7 a 11 con Process One', p1_lanes=(3, 4))
