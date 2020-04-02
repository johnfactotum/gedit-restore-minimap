from gi.repository import GObject, Gedit, GtkSource, Gtk

class RestoreMinimapPlugin(GObject.Object, Gedit.ViewActivatable):

    view = GObject.property(type=Gedit.View)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        self.tab = self.view.get_parent().get_parent().get_parent()
        self.tab.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.source_map = GtkSource.Map()
        self.source_map.set_view(self.view)
        self.source_map.show()
        self.tab.pack_end(self.source_map, False, True, 0)

    def do_deactivate(self):
        self.tab.remove(self.source_map)
