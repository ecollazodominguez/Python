from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, Spacer, SimpleDocTemplate

guion = []

fila1 = ['', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
fila2 = ['Mañana', 'Clases', 'Deporte', 'medico', '', 'Clases', 'Estudio', 'Faojfokai']
fila3 = ['Tarde', 'Trabajo', 'Trabajo', 'Trabajo', 'Piscina', 'Estudio', 'Estudio', '']
fila4 = ['Noche', '', '', '', 'Trabajo', '', 'Mdoahasdh', '']

tabla = Table([fila1, fila2, fila3, fila4])
tabla.setStyle([('TEXTCOLOR', (1, 0), (7, 0), colors.red),
                ('TEXTCOLOR', (0, 0), (0, 3), colors.blue),
                ('BACKGROUND', (1, 1), (-1, -1), colors.lightgrey),
                ('INNERGRID', (1, 1), (-1, -1), 0.25, colors.gray),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black)])
guion.append(tabla)

datos = [
    ['Arriba\nIzquierda', '', '02', '03', '04'],
    ['', '', '12', '13', '44'],
    ['20', '21', '12', 'Abajo\nDerecha', ''],
    ['30', '31', '32', '', '']
]

estilo = [
    ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
    ('BACKGROUND', (0, 0), (-1, -1), colors.palegreen),
    ('SPAN', (0, 0), (1, 1)),
    ('BACKGROUND', (-2, -2), (-1, -1), colors.pink),
    ('SPAN', (-2, -2), (-1, -1))
]

guion.append(Spacer(0, 40))

tabla2 = Table(datos, style=estilo)
guion.append(tabla2)

doc = SimpleDocTemplate("ejemploTabla2Platypus.pdf", pagesize=A4, showBoundary=0)

doc.build(guion)
