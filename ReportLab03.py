import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer

follaEstilo = getSampleStyleSheet()

guion = []

cabecera = follaEstilo['Heading4']
cabecera.pageBreakBefore = 1
cabecera.keepWithNext = 3
cabecera.backColor = colors.lightgrey

parrafo = Paragraph("Cabecera de doc", cabecera)
guion.append(parrafo)

cadena = "Cadena de texto para ampliar el contenido.  " * 400

estilo = follaEstilo["BodyText"]
parrafo2 = Paragraph(cadena, estilo)
guion.append(parrafo2)

guion.append(Spacer(0, 20))
fich_imagen = "/home/local/DANIELCASTELAO/fsancheztemprano/Imágenes/triforce.jpg"
imagen_logo = Image(os.path.realpath(fich_imagen), width=400)
guion.append(imagen_logo)

doc = SimpleDocTemplate("ejemploInformePlatypus.pdf", pagesize=A4, showBoundary=0)

doc.build(guion)
