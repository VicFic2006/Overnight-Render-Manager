import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class NumberEntry(Gtk.Entry):
    def __init__(self):
        Gtk.Entry.__init__(self)
        self.connect("changed", self.on_changed)

    def on_changed(self, *args):
        text = self.get_text().strip()
        self.set_text("".join([i for i in text if i in "0123456789"]))


def create_label(text: str):
    label = Gtk.Label(label=text)
    label.set_halign(Gtk.Align.CENTER)
    return label


def create_entry(numbers_only=True):
    if numbers_only:
        entry = NumberEntry()
    else:
        entry = Gtk.Entry()
    entry.set_halign(Gtk.Align.CENTER)
    return entry


def create_button(text: str):
    button = Gtk.Button(label=text)
    button.set_halign(Gtk.Align.CENTER)
    return button


def create_file_chooser_dialog(self):
    file_chooser_dialog = Gtk.FileChooserDialog(
        "Choose a .blend file",
        self,
        Gtk.FileChooserAction.OPEN,
        (
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK
        )
    )
    return file_chooser_dialog

