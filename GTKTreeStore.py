import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Fiestra (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='Exemplo con TreeStore')
        modeloTreeStore = Gtk.TreeStore(str,int)

        for avo in range(5):
            punteiroAvo = modeloTreeStore.append(None,['Avo',avo])
            for pai in range(4):
                punteiroPai = modeloTreeStore.append(punteiroAvo,['Pai',pai])
                for fillo in range(3):
                    punteiroFillo = modeloTreeStore.append(punteiroPai,['Fillo',fillo])

        vista = Gtk.TreeView(modeloTreeStore)
        tvcolumna = Gtk.TreeViewColumn('Parentesco')
        vista.append_column(tvcolumna)
        celda = Gtk.CellRendererText()
        tvcolumna.pack_start(celda, True)
        tvcolumna.add_attribute(celda,'text',0)

        tvcolumna = Gtk.TreeViewColumn('Orde')
        vista.append_column(tvcolumna)
        celda = Gtk.CellRendererText()
        tvcolumna.pack_start(celda, True)
        tvcolumna.add_attribute(celda,'text',1)

        self.add(vista)

        self.show_all()
        self.connect('destroy', Gtk.main_quit)

if __name__ == "__main__":
    Fiestra()
    Gtk.main()