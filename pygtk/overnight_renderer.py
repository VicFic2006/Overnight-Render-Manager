import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from widgets import create_label, create_entry, create_button, \
create_file_chooser_dialog

class MainWindow(Gtk.Window):
    grid = Gtk.Grid(column_spacing=12, row_spacing=12)

    location_entry = create_entry(False)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_default_size(600, 800)
        self.set_title("Blender Overnight Renderer")
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
    
        self.create_content()

    def create_content(self):
        location_label = create_label("Path to .blend file")
        self.location_entry.set_width_chars(30)
        location_button = create_button("Browse")
        location_button.connect("clicked", self.on_location_clicked)

        self.add(self.grid)
        self.grid.set_halign(Gtk.Align.CENTER)
        self.grid.set_valign(Gtk.Align.CENTER)
        self.grid.attach(location_label, 0, 0, 1, 1)
        self.grid.attach(self.location_entry, 1, 0, 1, 1)
        self.grid.attach(location_button, 2, 0, 1, 1)

    def on_location_clicked(self, button: Gtk.Button):
        file_chooser_dialog = create_file_chooser_dialog(self)

        self.add_filters(file_chooser_dialog)

        response = file_chooser_dialog.run()

        if response == Gtk.ResponseType.OK:
            print(file_chooser_dialog.get_filename())
            self.location_entry.set_text(file_chooser_dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Canceled")

        file_chooser_dialog.destroy()

    def add_filters(self, dialog: Gtk.FileChooserDialog):
        filter_blend = Gtk.FileFilter()
        filter_blend.set_name(".blend files")
        filter_blend.add_pattern("*.blend")
        filter_blend.add_pattern("*.blend1")
        dialog.add_filter(filter_blend)


main_window = MainWindow()
main_window.connect("delete-event", Gtk.main_quit)
main_window.show_all()
Gtk.main()
