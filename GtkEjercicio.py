import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class Fiestra(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Reseva de voos")
        self.set_default_size(600,400)

        grid = Gtk.Grid()
        self.add(grid)

        caixa = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=25)
        etiqueta = Gtk.Label()
        etiqueta2 = Gtk.Label()
        etiqueta3 = Gtk.Label()
        etiqueta.set_text("Data:")
        etiqueta2.set_text("Dende:")
        etiqueta3.set_text("Ata:")
        etiqueta2.set_margin_left(10)


        caixa.pack_start(etiqueta, True,True, 0)
        caixa.pack_start(etiqueta2, True, True, 0)
        caixa.pack_start(etiqueta3, True, True, 0)


        caixa2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)


        txt = Gtk.Entry()
        Combo = Gtk.ComboBoxText()
        Combo1 = Gtk.ComboBoxText()
        txt.set_margin_left(100)
        Combo.set_margin_left(100)
        Combo1.set_margin_left(100)
        Combo.append_text("New York")
        Combo1.append_text("London")

        caixa2.pack_start(txt, True, True, 0)
        caixa2.pack_start(Combo, True, True, 0)
        caixa2.pack_start(Combo1, True, True, 0)


        Frame = Gtk.Frame()

        Frame.set_label ("Opcións")
        Frame.set_margin_left(100)

        caixaFrame = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)

        radio = Gtk.RadioButton("Primeira clase")
        radio1 = Gtk.RadioButton("Negocios")
        radio2 = Gtk.RadioButton("Turista")

        caixaFrame.pack_start(radio, True, True, 0)
        caixaFrame.pack_start(radio1, True, True, 0)
        caixaFrame.pack_start(radio2, True, True, 0)

        Frame.add(caixaFrame)

        Frame2 = Gtk.Frame()
        Frame2.set_label ("Voos disponibles")
        cuadrotxt = Gtk.TextView()
        Frame2.set_margin_left(10)
        cuadrotxt.set_margin_left(10)
        cuadrotxt.set_size_request(400,200)
        Frame2.add(cuadrotxt)

        grid.add(caixa)
        grid.attach(caixa2,2,0,1,1)
        grid.add(Frame)
        grid.attach_next_to(Frame2,caixa,Gtk.PositionType.BOTTOM,4,1)

        caixabotons = Gtk.Box()
        boton1 = Gtk.Button(label="Boton")
        boton2 = Gtk.Button(label="Boton")
        boton3 = Gtk.Button(label="Boton")
        caixabotons.set_margin_left(15)

        caixabotons.pack_start(boton1, True, True, 0)
        caixabotons.pack_start(boton2, True, True, 0)
        caixabotons.pack_start(boton3, True, True, 0)

        grid.attach_next_to(caixabotons,Frame2,Gtk.PositionType.BOTTOM,4,1)






        self.connect("destroy", Gtk.main_quit)
        self.show_all()


Fiestra()
Gtk.main()