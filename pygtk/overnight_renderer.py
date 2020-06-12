import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import os
import time

from widgets import create_label, create_entry, create_button, \
create_file_chooser_dialog, create_combo_box, create_check_button

class MainWindow(Gtk.Window):
    grid = Gtk.Grid(column_spacing=12, row_spacing=12)

    blend_file_entry = None
    output_type_combo_box = None
    shutdown_check_button = None
    output_file_entry = None

    blend_file = ""
    output_type = ""
    output_file = ""
    shutdown = False


    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_default_size(600, 800)
        self.set_title("Blender Overnight Renderer")
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        self.create_content()

    def create_content(self) -> None:
        blend_file_label = create_label("Path to .blend file")
        self.blend_file_entry = create_entry(False)
        blend_file_button = create_button("Browse")
        blend_file_button.connect("clicked", self.on_blend_file_clicked)

        output_type_label = create_label("Choose an output type")
        output_types = ["Animation", "Single Frame"]
        self.output_type_combo_box = create_combo_box(output_types)

        output_file_label = create_label("Output path")
        self.output_file_entry = create_entry(False)
        output_file_button = create_button("Browse")
        output_file_button.connect("clicked", self.on_output_file_clicked)

        shutdown_label = create_label("Shutdown after rendering is finished")
        self.shutdown_check_button = create_check_button()

        render_button = create_button("Render")
        render_button.connect("clicked", self.on_render_clicked)

        self.add(self.grid)
        self.grid.set_halign(Gtk.Align.CENTER)
        self.grid.set_valign(Gtk.Align.CENTER)
        self.grid.attach(blend_file_label, 0, 0, 1, 1)
        self.grid.attach(self.blend_file_entry, 1, 0, 1, 1)
        self.grid.attach(blend_file_button, 2, 0, 1, 1)
        self.grid.attach(output_type_label, 0, 1, 1, 1)
        self.grid.attach(self.output_type_combo_box, 1, 1, 1, 1)
        self.grid.attach(output_file_label, 0, 2, 1, 1)
        self.grid.attach(self.output_file_entry, 1, 2, 1, 1)
        self.grid.attach(output_file_button, 2, 2, 1, 1)
        self.grid.attach(shutdown_label, 0, 3, 1, 1)
        self.grid.attach(self.shutdown_check_button, 1, 3, 1, 1)
        self.grid.attach(render_button, 0, 4, 3, 1)

    def on_blend_file_clicked(self, button: Gtk.Button) -> None:
        file_chooser_dialog = create_file_chooser_dialog(self, Gtk.FileChooserAction.OPEN, Gtk.STOCK_OPEN)
        self.add_blend_filters(file_chooser_dialog)

        response = file_chooser_dialog.run()

        if response == Gtk.ResponseType.OK:
            self.blend_file_entry.set_text(file_chooser_dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            pass

        file_chooser_dialog.destroy()

    def on_output_file_clicked(self, button: Gtk.Button) -> None:
        file_chooser_dialog = create_file_chooser_dialog(self, Gtk.FileChooserAction.SAVE, Gtk.STOCK_SAVE)
        file_chooser_dialog.set_current_name("Render")

        response = file_chooser_dialog.run()

        if response == Gtk.ResponseType.OK:
            self.output_file_entry.set_text(file_chooser_dialog.get_filename())
        else:
            pass

        file_chooser_dialog.destroy()

    def add_blend_filters(self, dialog: Gtk.FileChooserDialog) -> None:
        filter_blend = Gtk.FileFilter()
        filter_blend.set_name(".blend files")
        filter_blend.add_pattern("*.blend")
        filter_blend.add_pattern("*.blend1")
        dialog.add_filter(filter_blend)

    def on_render_clicked(self, button: Gtk.Button) -> None:
        self.blend_file = self.blend_file_entry.get_text()
        output_type_iter = self.output_type_combo_box.get_active_iter()
        if output_type_iter is not None:
            model = self.output_type_combo_box.get_model()
            self.output_type = model[output_type_iter][0]
        self.output_file = self.output_file_entry.get_text()
        self.shutdown = self.shutdown_check_button.get_active()
        self.render()

    def render(self) -> None:
        os.chdir(os.path.dirname(self.blend_file))
        if self.output_type == "Animation":
            print("Rendering animation of {} \n".format(self.blend_file))
            os.system("blender -b {} -o {} -a".format(os.path.basename(self.blend_file), self.output_file))
        elif self.output_type == "Single Frame":
            print("Rendering frame 1 of {} \n".format(self.blend_file))
            os.system("blender -b {} -o {} -f 1".format(os.path.basename(self.blend_file), self.output_file))

        print("Rendering complete!")
        if self.shutdown:
            os.system("notify-send 'Rendering {} complete. Shutting down in 30 seconds'".format(os.path.basename(self.blend_file)))
            time.sleep(30)
            print("Shutting down...")
            os.system("poweroff")
        else:
            os.system("notify-send 'Rendering {} complete.'".format(os.path.basename(self.blend_file)))


main_window = MainWindow()
main_window.connect("delete-event", Gtk.main_quit)
main_window.show_all()
Gtk.main()
