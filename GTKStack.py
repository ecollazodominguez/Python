import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Fiestra(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo con Stack")

        caixa = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.add (caixa)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        casinhaVerificacion = Gtk.CheckButton('Pulsame')
        stack.add_titled (casinhaVerificacion, "check", "Casiña verificacion")

        etiqueta = Gtk.Label()
        etiqueta.set_markup ("<big>Unha etiqueta simple</big>")
        stack.add_titled (etiqueta, "etiqueta", "Unha etiqueta")

        panel = Panel()
        stack.add_titled(panel, "panel", "O panel")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)

        caixa.pack_start(stack_switcher, True, True, 0)
        caixa.pack_start(stack, True, True, 0)




        self.connect("destroy", Gtk.main_quit)
        self.show_all()



class Panel(Gtk.Grid):


    def __init__(self):
        Gtk.Grid.__init__(self)


        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")
        button7 = Gtk.Button(label="Button 7")
        button8 = Gtk.Button(label="Button 8")
        button9 = Gtk.Button(label="Button 9")

        self.add(button1)
        self.attach(button2, 1, 0, 2, 1)
        self.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
      #   grid.attach(button5, 1, 2, 1, 1)
       # grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

        caixa = Gtk.Box()
        caixa.pack_start (button7, True, True, 0)
        caixa.pack_start(button8, True, True, 0)
        caixa.pack_start(button9, True, True, 0)
        self.attach_next_to(caixa, button3, Gtk.PositionType.BOTTOM, 2, 1)


Fiestra()
Gtk.main()

