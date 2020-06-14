import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from typing import Union, List

class NumberEntry(Gtk.Entry):
    def __init__(self):
        Gtk.Entry.__init__(self)
        self.connect("changed", self.on_changed)

    def on_changed(self, *args) -> None:
        text = self.get_text().strip()
        self.set_text("".join([i for i in text if i in "0123456789"]))


def create_label(text: str) -> Gtk.Label:
    label = Gtk.Label(label=text)
    label.set_halign(Gtk.Align.START)
    return label


def create_entry(numbers_only: bool=True) -> Union[NumberEntry, Gtk.Entry]:
    if numbers_only:
        entry = NumberEntry()
    else:
        entry = Gtk.Entry()
    entry.set_width_chars(30)
    return entry


def create_button(text: str) -> Gtk.Button:
    button = Gtk.Button(label=text)
    return button


def create_file_chooser_dialog(self, action: Gtk.FileChooserAction, button: Gtk) -> Gtk.FileChooserDialog:
    file_chooser_dialog = Gtk.FileChooserDialog(
        "",
        self,
        action,
        (
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            button,
            Gtk.ResponseType.OK
        )
    )
    return file_chooser_dialog


def create_combo_box(model: Gtk.ListStore=None, labels: List[str]=None) -> Gtk.ComboBox:
    if model is None:
        model = Gtk.ListStore(str)
    if labels is not None:
        for i in range(len(labels)):
            model.append([labels[i]])
    combo_box = Gtk.ComboBox.new_with_model(model)
    renderer_text = Gtk.CellRendererText()
    combo_box.pack_start(renderer_text, True)
    combo_box.add_attribute(renderer_text, "text", 0)
    combo_box.set_active(0)
    return combo_box

def create_check_button() -> Gtk.CheckButton:
    check_button = Gtk.CheckButton()
    return check_button
