from reportlab.pdfgen import canvas

aux = canvas.Canvas("prueba.pdf")
aux.drawString(0, 0, "Pos (x,y) = (0,0)")
aux.drawString(50, 100, "Pos (x,y) = (50,100)")
aux.drawString(150, 50, "Pos (x,y) = (150,50)")

aux.showPage()
aux.save()
