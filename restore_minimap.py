from gi.repository import GObject, Gedit, GtkSource, Gtk, Pango, PeasGtk, Gio
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
SCHEMAS_PATH = os.path.join(BASE_PATH, 'schemas')

try:
    schema_source = Gio.SettingsSchemaSource.new_from_directory(
        SCHEMAS_PATH,
        Gio.SettingsSchemaSource.get_default(),
        False)
    schema = schema_source.lookup(
        'org.gnome.gedit.plugins.restore_minimap',
        False)
    settings = Gio.Settings.new_full(
        schema,
        None,
        '/org/gnome/gedit/plugins/restore_minimap/')
except:
    settings = None

class RestoreMinimapPluginPreferences(GObject.Object, Gedit.WindowActivatable, PeasGtk.Configurable):

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_create_configure_widget(self):
        if not settings:
            return Gtk.Label(label='Error: could not load settings schema')

        check = Gtk.CheckButton.new_with_label('Display minimap on the left side')
        check2 = Gtk.CheckButton.new_with_label('Show separator')
        flag = Gio.SettingsBindFlags.DEFAULT
        settings.bind('display-on-left', check, 'active', flag)
        settings.bind('show-separator', check2, 'active', flag)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, border_width=10)
        box.pack_start(check, False, True, 0)
        box.pack_start(check2, False, True, 0)
        return box

class RestoreMinimapPlugin(GObject.Object, Gedit.ViewActivatable):

    view = GObject.property(type=Gedit.View)

    def __init__(self):
        GObject.Object.__init__(self)

    def update_display_on_left(self):
        display_on_left = False
        if settings is not None:
            display_on_left = settings.get_boolean('display-on-left')

        if display_on_left:
            self.tab.set_direction(Gtk.TextDirection.LTR)
        else:
            self.tab.set_direction(Gtk.TextDirection.RTL)

    def on_display_on_left_changed(self, *args):
        self.update_display_on_left()

        # force the tab to redraw
        self.tab.hide()
        self.tab.show()

    def on_separator_changed(self, *args):
        show_separator = True
        if settings is not None:
            show_separator = settings.get_boolean('show-separator')
        if show_separator: self.sep.show()
        else: self.sep.hide()

    def do_activate(self):
        self.tab = self.view.get_parent().get_parent().get_parent()
        self.tab.set_orientation(Gtk.Orientation.HORIZONTAL)

        # hide vertical scrollbar
        self.scrolled = self.view.get_parent()
        self.scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.EXTERNAL)

        self.source_map = GtkSource.Map()
        self.source_map.set_view(self.view)
        self.source_map.set_property('font-desc', Pango.FontDescription('BuilderBlocks 1'))
        self.source_map.show()

        self.sep = Gtk.Separator()
        self.tab.pack_end(self.sep, False, True, 0)
        self.tab.pack_end(self.source_map, False, True, 0)

        self.update_display_on_left()
        self.on_separator_changed()
        if settings is not None:
            self.settings_handlers = [
                settings.connect('changed::display-on-left', self.on_display_on_left_changed),
                settings.connect('changed::show-separator', self.on_separator_changed)
            ]

    def do_deactivate(self):
        self.tab.remove(self.source_map)
        self.tab.remove(self.sep)
        self.tab.set_orientation(Gtk.Orientation.VERTICAL)
        self.scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        if settings is not None:
            for handler in self.settings_handlers:
                settings.disconnect(handler)
