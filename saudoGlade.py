import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class FiestraPrincipal ():
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file ("gladeExemploGtk.glade")

        fiestraPrincipal = builder.get_object("fiestraPrincipal")
        self.txtNome = builder.get_object("txtNome")
        self.lblSaudo = builder.get_object("lblSaudo")
        self.btnSaudar = builder.get_object("btnSaudar")

        sinais = {
            "on_btnSaudar_clicked" : self.on_btnSaudar_clicked,
            "on_txtNome_activate": self.on_txtNome_activate,
            "on_fiestraPrincipal_destroy": Gtk.main_quit

        }
        builder.connect_signals(sinais)

        fiestraPrincipal.show_all()


    def on_btnSaudar_clicked(self,boton):
        """método que maneja la señal clicked de btnSaudar"""

        nome = self.txtNome.get_text()
        self.lblSaudo.set_text("ola " + nome)

    def on_txtNome_activate(self, cadrotexto):
        self.on_btnSaudar_clicked(cadrotexto)

if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()