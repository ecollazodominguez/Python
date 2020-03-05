import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

#USAMOS GLib


class Fiestra(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo con Gtk.ProgressBar")
        self.set_default_size(400, 200)
        self.modoActivo = False

        caixaV = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing=6)

        #creamos barra progreso y lo añadimos a la caja
        self.barraProgreso = Gtk.ProgressBar()
        caixaV.pack_start (self.barraProgreso, True, True, 0)

        #creamos checkbutton y relacionamos su accion
        self.chkTexto = Gtk.CheckButton("Mostra texto")
        self.chkTexto.connect ("toggled", self.on_chkTexto_toggled)
        caixaV.pack_start (self.chkTexto, True, True, 0)

        #Creamos checkbutton y relacionamos su accion

        self.chkModoActivo = Gtk.CheckButton("Modo activo")
        self.chkModoActivo.connect ("toggled", self.on_chkModoActivo_toggled)
        caixaV.pack_start (self.chkModoActivo, True, True, 0)

        #Creamos checkbutton y relacionamos su accion

        self.chkEsquerdaDereita = Gtk.CheckButton("Esquerda a dereita")
        self.chkEsquerdaDereita.connect ("toggled", self.on_chkEsquerdaDereita_toggled)
        caixaV.pack_start (self.chkEsquerdaDereita, True, True, 0)

        #Creamos temporizador

        self.timeout_id = GLib.timeout_add (100, self.on_timeout, None)

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


        #si se activa el mostrar texto se muestra en la barra de progreso

    def on_chkTexto_toggled(self, control):
        mostra_texto = control.get_active()
        if mostra_texto:
            texto = "Mensaxe a mostrar"
        else:
            texto = None
        #aumentar porcentaje barra
        self.barraProgreso.set_fraction(0.56)
        #Añadir el texto
        self.barraProgreso.set_text(texto)
        #Mostrar texto si mostra texto está activo
        self.barraProgreso.set_show_text(mostra_texto)

        # si se activa ModoActivo actualiza la barra de progreso
    def on_chkModoActivo_toggled(self, control):
        self.modoActivo = control.get_active()
        if self.modoActivo:
            #Actualiza regularmente la barra de progreso
            self.barraProgreso.pulse()
        else:
            #Resetea la barra
            self.barraProgreso.set_fraction (0.0)

        #cambia de direccion la barra
    def on_chkEsquerdaDereita_toggled(self, control):
        esquerdaDereita = control.get_active()
        self.barraProgreso.set_inverted(esquerdaDereita)


        # Temporizador que se va activando cada cierto tiempo y aumenta la barra
    def on_timeout(self, datos_usuario):
        if self.modoActivo:
            self.barraProgreso.pulse()
        else:
            novo_valor = self.barraProgreso.get_fraction() + 0.01
            if novo_valor > 1:
                novo_valor = 0
            self.barraProgreso.set_fraction(novo_valor)
        return True



if __name__ == "__main__":
    Fiestra()
    Gtk.main()
