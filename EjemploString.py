cadea = "Esta é unha cadea de caracteres"
cadea2 = 'Pódese definir cos dous tipos de comilla'

print (cadea + "." + cadea2)

#Cuenta cuantos caracteres CA hay, puedes indicar por donde empieza y donde termina
print (cadea.count("ca",13,15))

#Index de dónde se atopa
print (cadea.find ("Es"))
#Concatenación
print (cadea.join(cadea2))
#particiona palabras
print (cadea.partition("é unha cadea"))
#Hace una lista por palabras
print (cadea.split())
# reemplaza
print (cadea.replace (' ', '-*-'))