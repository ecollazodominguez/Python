from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Image, Drawing
from reportlab.lib.pagesizes import A4

guion = []
imagen = Image(400, 10, 596, 133, "/home/local/DANIELCASTELAO/fsancheztemprano/Imágenes/triforce.jpg")

dibujo = Drawing(30, 30)
dibujo.add(imagen)
dibujo.translate(0, 600)
guion.append(dibujo)

dibujo = Drawing(30, 30)
dibujo.add(imagen)
dibujo.rotate(45)
dibujo.scale(1.5, 0.5)
dibujo.translate(-90, 300)
guion.append(dibujo)

dibujo = Drawing(30, 30)
dibujo.add(imagen)
dibujo.rotate(90)
dibujo.translate(-20, -100)
guion.append(dibujo)

dibujo = Drawing(A4[0], A4[1])
for deb in guion:
    dibujo.add(deb)

renderPDF.drawToFile(dibujo, "prueba2.pdf")
