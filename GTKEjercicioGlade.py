import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class Fiestra (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Exemplocon GTKHeaderBAr")
        self.set_default_size(400,200)

        caixaV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL)
        caixaH1 = Gtk.Box ()
        builder = Gtk.Builder()
        builder.add_from_file("exercicioPyInterface.glade")
        grdGlade = builder.get_object("grdGlade")
        self.txtData = builder.get_object("txtData")
        sinais = {"on_txtData_activate": self.on_txtData_activate,
                  "on_rbts_toggle": self.on_rbts_toggle(),
                  "on_chkPrioridade_toggled": self.on_chkProridade_toggled()}
        builder.connect_signals(sinais)


        """
        grid = Gtk.Grid()
        lblData = Gtk.Label ("Data: ")
        grid.add(lblData)
        lblDende =Gtk.Label ("Dende: ")
        grid.attach_next_to(lblDende, lblData, Gtk.PositionType.BOTTOM, 1, 1)
        lblAta = Gtk.Label ("Ata: ")
        grid.attach (lblAta, 0, 2,1,1)
        txtData = Gtk.Entry()
        grid.attach_next_to(txtData, lblData, Gtk.PositionType.RIGHT, 1, 1)
        cmbDende = Gtk.ComboBox()
        grid.attach_next_to(cmbDende, lblDende, Gtk.PositionType.RIGHT, 1, 1)
        cmbAta = Gtk.ComboBox()
        grid.attach_next_to(cmbAta, lblAta, Gtk.PositionType.RIGHT, 1, 1)
"""
        frmOpcions = Gtk.Frame()
        frmOpcions.set_label("Opcions")
        caixaFrm = Gtk.Box (orientation = Gtk.Orientation.VERTICAL)
        frmOpcions.add(caixaFrm)
        self.rbtPrimeira = Gtk.RadioButton("Primeira clase")
        self.rbtNegocios = Gtk.RadioButton ("Negocios")
        self.rbtTurista = Gtk.RadioButton ( "Turista")
        self.rbtNegocios.join_group(self.rbtPrimeira)
        self.rbtTurista.join_group(self.rbtPrimeira)
        self.rbtPrimeira.connect("toggled",self.on_rbts_toggle,"Primeira")
        self.rbtNegocios.connect("toggled", self.on_rbts_toggle, "Negocios")
        self.rbtTurista.connect("toggled", self.on_rbts_toggle, "Turista")
        caixaFrm.pack_start(self.rbtPrimeira, True, True, 0)
        caixaFrm.pack_start(self.rbtNegocios, True, True, 0)
        caixaFrm.pack_start(self.rbtTurista, True, True, 0)
        #grid.attach (frmOpcions, 2,0,1,3)


       # caixaH1.pack_start(grid, True, True, 0)
        caixaH1.pack_start (grdGlade, True, True, 0)
        caixaH1.pack_start(frmOpcions, True, True, 0)
        caixaV.pack_start(caixaH1, True, True, 0)

        frame2 = Gtk.Frame()
        caixaV.pack_start(frame2, True, True, 0)
        frame2.set_label("Voos disponibles")
        txvVoosDisponibles = Gtk.TextView ()
        self.txvBuffer = txvVoosDisponibles.get_buffer()
        frame2.add(txvVoosDisponibles)


        caixaH3 = Gtk.Box()
        caixaV.pack_start(caixaH3, True, True, 0)
        btnBuscar = Gtk.Button("Buscar")
        btnMercar = Gtk.Button("Mercar")
        btnSair = Gtk.Button("Sair")
        caixaH3.pack_start(btnBuscar, False, True, 0)
        caixaH3.pack_start(btnMercar, False, True, 0)
        caixaH3.pack_start(btnSair,False, True, 0)


        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_txtData_activate(self, control):
        fin = self.txvBuffer.get_end_iter()
        self.txvBuffer.insert_markup(fin, "<b>"+ self.txtData.get_text()+"</b>",-1)
        self.txvBuffer.insert (fin, "\n", -1)

    def on_rbts_toggle (self, control, nome):

        if control.get_active():
            fin = self.txvBuffer.get_end_iter()
            self.txvBuffer.insert(fin,"Activado o RadioButton: "+nome+"\n")

    def on_chkProridade_toggled (self, control):
        texto = self.txtData.get_text() + "\n"
        indice = self.cmbDende.get_active_iter()
        if indice is not None:
            destino = self.cmbDende.get_model()[indice][1]
        if self.rbtPrimeira.get_active():
            clase = "Primeira"
        elif self.rbtNegocios.get_active():
            clase = "Negocios"
        else:
            clase = "Turista"

        texto = texto + destino + "\n"+ "Clase: "+clase + "\n"+ "Prioridade na entrada"
        self.txvBuffer(texto)

if __name__ == "__main__":
    Fiestra()
    Gtk.main()