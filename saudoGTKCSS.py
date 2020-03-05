import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class FiestraPrincipal (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Exemplo saudo con GTK")

        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path('./estilos.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen,cssProvider,Gtk.STYLE_PROVIDER_PRIORITY_USER)

        caixa = Gtk.Box (spacing = 6, orientation=Gtk.Orientation.VERTICAL)

        self.btnSaudar = Gtk.Button (label = "Saudo")
        self.btnSaudar.connect ("clicked",self.on_btnSaudar_clicked)
        caixa.pack_start(self.btnSaudar, False, False, 6)

        self.txtNome = Gtk.Entry ()
        self.txtNome.set_text("Escribe aqui o teu nome")
        self.txtNome.connect("activate",self.on_txtNome_activate)
        caixa.pack_start(self.txtNome,True,True,6)

        self.lblSaudo = Gtk.Label()
        self.lblSaudo.set_text ("Ola a todos")
        caixa.pack_start(self.lblSaudo,True,True,6)

        self.add (caixa)
        self.connect ("destroy",Gtk.main_quit)




        self.show_all()


    def on_btnSaudar_clicked(self,boton):
        """método que maneja la señal clicked de btnSaudar"""

        nome = self.txtNome.get_text()
        if nome == "":
            Gtk.Label.set_markup(self.lblSaudo,"<span color='red'>Escriba o nome </span>")
        else:
            self.lblSaudo.set_text("ola " + nome)

    def on_txtNome_activate(self, cadrotexto):
        self.on_btnSaudar_clicked(cadrotexto)

if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()