import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class Fiestra(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Cabeceira")
        self.set_default_size(600,400)

        cabeceira = Gtk.HeaderBar()
        cabeceira.set_show_close_button(True)
        cabeceira.props.title ="Mostra de uso de HeaderBar"
        self.set_titlebar(cabeceira)

        boton= Gtk.Button()
        icon = Gio.ThemedIcon (name='mail-send-receive-symbolic')
        imaxe = Gtk.Image.new_from_gicon (icon, Gtk.IconSize.BUTTON)
        boton.add(imaxe)
        cabeceira.pack_end(boton)

        caixa = Gtk.Box()
        Gtk.StyleContext.add_class (caixa.get_style_context(), "linked")

        boton2 = Gtk.Button()
        boton2.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        caixa.add(boton2)

        boton3 = Gtk.Button()
        boton3.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        caixa.add(boton3)

        cabeceira.pack_start(caixa)

        self.add (Gtk.TextView())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


Fiestra()
Gtk.main()