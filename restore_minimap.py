from gi.repository import GObject, Gedit, GtkSource, Gtk, Pango

class RestoreMinimapPlugin(GObject.Object, Gedit.ViewActivatable):

    view = GObject.property(type=Gedit.View)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        self.tab = self.view.get_parent().get_parent().get_parent()
        self.tab.set_orientation(Gtk.Orientation.HORIZONTAL)

        # move the minimap to the right
        self.tab.set_direction(Gtk.TextDirection.RTL)

        # hide vertical scrollbar
        self.scrolled = self.view.get_parent()
        self.scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.EXTERNAL)

        self.source_map = GtkSource.Map()
        self.source_map.set_view(self.view)
        self.source_map.set_property('font-desc', Pango.FontDescription('BuilderBlocks 1'))
        self.source_map.show()

        self.sep = Gtk.Separator()
        self.sep.show()
        self.tab.pack_end(self.sep, False, True, 0)
        self.tab.pack_end(self.source_map, False, True, 0)

    def do_deactivate(self):
        self.tab.remove(self.source_map)
        self.tab.remove(self.sep)
        self.tab.set_orientation(Gtk.Orientation.VERTICAL)
        self.scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
