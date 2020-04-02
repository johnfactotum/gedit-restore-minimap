from gi.repository import GObject, Gedit, GtkSource, Pango

class RestoreMinimapPlugin(GObject.Object, Gedit.WindowActivatable):

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        self.source_map = GtkSource.Map()
        self.source_map.show()
        self.panel = self.window.get_side_panel()
        self.panel.add_titled(self.source_map, 'minimap', 'Minimap')
        self._update_view()

    def do_deactivate(self):
        self.panel.remove(self.source_map)

    def do_update_state(self):
        self._update_view()

    def _update_view(self):
        view = self.window.get_active_view()
        if view is not None:
            self.source_map.set_view(view)
