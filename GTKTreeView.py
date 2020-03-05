import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class Fiestra(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo con Gtk.TreeView")
        self.set_default_size(400, 200)

        #Creamos caja vertical
        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        #Creamos modelo
        modelo = Gtk.ListStore(str,str,float,bool,int)
        #Añadimos datos
        modelo.append(["Hotel Melia", "García Barbón 48", 75.38, True, 1])
        modelo.append(["Hotel Galeones", "Avda Madrid", 80.88, False, 2])
        modelo.append(["Hotel Baiha", "Paseo as avenidas 55", 60.38, True, 5])

        #Creamos a vista e añadimos directamente o modelo
        vista = Gtk.TreeView(model=modelo)
        #Añadimos a vista a caixa
        boxV.pack_start(vista, True, True, 0)

        #Creamos un Cellrenderer para as casillas de texto
        celdaText = Gtk.CellRendererText()
        celdaDireccion = Gtk.CellRendererText()
        #Con esta propiedad en false imposibilita que se pueda editar
        celdaText.set_property("editable", False)
        celdaDireccion.set_property("editable", True)
        #Engadímoslle un evento para modificar a casilla Direccion
        celdaDireccion.connect("edited", self.on_celdaDireccion_edited,modelo)

        #Creamos un Cellrenderer para as casillas booleanas
        celdaCheck = Gtk.CellRendererToggle()
        #Engadímoslle un evento para poder modificar as casillas e o modelo que recibirá
        celdaCheck.connect("toggled", self.on_celdaCheck_toggled, modelo)

        #Creamos un Cellrenderer para as casillas numéricas para mostrar o progreso
        celdaOcupacion = Gtk.CellRendererProgress()

        #Creamos un TreeViewColumn (Forma parte do TreeView) e indicamos un nome a visualicacion (Cellrenderer)
        # e co text/active indicamos a posicion da lista a mostrar
        columnaHotel = Gtk.TreeViewColumn('Aloxamento',celdaText, text = 0)
        columnaDireccion = Gtk.TreeViewColumn('Direccion',celdaDireccion, text = 1)
        columnaOcupacion = Gtk.TreeViewColumn('Ocupacion', celdaOcupacion, value=2)
        columnaMascotas = Gtk.TreeViewColumn('Mascotas', celdaCheck, active=3)
        #Esto é o mismo co da arriba | columnaMascotas.add_attribute(celdaCheck, "active", 3)
        columnaCategoria = Gtk.TreeViewColumn('Categoria', celdaText, text=4)

        #Engadimos a columna ao TreeView
        vista.append_column(columnaHotel)
        vista.append_column(columnaDireccion)
        vista.append_column(columnaOcupacion)
        vista.append_column(columnaMascotas)
        vista.append_column(columnaCategoria)

        ######################################################
        #Creamos una caja horizontal y añadimos los botones para poder añadir al modelo de hoteles
        boxH = Gtk.Box(spacing=6)
        self.entryHotel= Gtk.Entry()
        self.entryDir = Gtk.Entry()
        self.entryOcup = Gtk.Entry()
        self.checkMascotas =Gtk.CheckButton()
        self.comboCat = Gtk.ComboBox()
        Novobtn = Gtk.Button(label="NOVO")

        boxV.pack_start(boxH, True, True, 0)
        boxH.pack_start(self.entryHotel, True, True, 0)
        boxH.pack_start(self.entryDir, True, True, 0)
        boxH.pack_start(self.entryOcup, True, True, 0)
        boxH.pack_start(self.checkMascotas, True, True, 0)
        boxH.pack_start(self.comboCat, True, True, 0)
        boxH.pack_start(Novobtn, True, True, 0)
        #añadimos evento al boton
        Novobtn.connect("clicked", self.on_Novobtn_clicked, modelo)
        #Creamos un modelo para el combo box de categoria
        modeloCat = Gtk.ListStore(str, int)
        modeloCat.append(["*",1])
        modeloCat.append(["**", 2])
        modeloCat.append(["***", 3])
        modeloCat.append(["****", 4])
        modeloCat.append(["*****", 5])
        self.comboCat.set_model(modeloCat)
        self.comboCat.pack_start(celdaText,True)
        self.comboCat.add_attribute(celdaText, "text",0)

        #Engadimos as caixas ao Window
        self.add(boxV)



        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    # Método para cambiar casillas booleanas
    def on_celdaCheck_toggled(self, control, fila, modelo):
        #fila sería a posición do punteiro ao clickar e contrariamos o contido
        modelo[fila][3] =  not modelo [fila][3]

    # Método para cambiar a casilla de texto
    def on_celdaDireccion_edited(self, control,fila, texto, modelo):
        modelo[fila][1] = texto
    # Método para añadir una linea entera al modelo de hoteles
    # para texto get_text
    # para numeros float(get_text)
    # para booleans get_active
    # para combobox get_model(), get_active_iter() y accedes con modCat[indice][0]
    def on_Novobtn_clicked(self, control,modelo):
        modCat = self.comboCat.get_model()
        indice = self.comboCat.get_active_iter()
        modelo.append([self.entryHotel.get_text(),self.entryDir.get_text(),float(self.entryOcup.get_text()),self.checkMascotas.get_active(),modCat[indice][1]])

if __name__ == "__main__":
    Fiestra()
    Gtk.main()