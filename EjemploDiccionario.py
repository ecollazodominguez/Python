diccionario = {"Verde" : "#229954",
               "Vermello" : "#c0392b",
               "Azul" : "#2471a3"
               }
print (diccionario["Verde"])

diccionario ["Verde"]= "#a9dbdf"

print (diccionario.get ("Amarelo", "#00000"))

if "Amarelo" in diccionario: #no Py2 é hash_key("Amarelo")
    print("Existe")
else:
    print("Non existe")

print (diccionario.items())
print (diccionario.keys())
print (diccionario.values())
diccionario.pop("Verde")
print (diccionario.items())
diccionario ["Violeta"] = "#rawera2"
print (diccionario.items())