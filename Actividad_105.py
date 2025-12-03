import tkinter as tk


class PopMenu:
    """Menú contextual (clic derecho) para un widget de texto."""

    def __init__(self, widget):
        self.widget = widget
        self.menu = tk.Menu(self.widget, tearoff=False)
        self._build_menu()
        # botón derecho del ratón
        self.widget.bind("<Button-3>", self.popup)

    def _build_menu(self):
        self.menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.undo)
        self.menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.redo)
        self.menu.add_separator()
        self.menu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy)
        self.menu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste)
        self.menu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut)

    def popup(self, event):
        """Muestra el menú en la posición del cursor."""
        self.menu.tk_popup(event.x_root, event.y_root)

    def cut(self):
        self.widget.event_generate("<<Cut>>")

    def copy(self):
        self.widget.event_generate("<<Copy>>")

    def paste(self):
        self.widget.event_generate("<<Paste>>")

    def redo(self):
        self.widget.event_generate("<<Redo>>")

    def undo(self):
        self.widget.event_generate("<<Undo>>")


def set_center(root, w, h):
    """Centra la ventana en la pantalla."""
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = int((ws / 2) - (w / 2))
    y = int((hs / 2) - (h / 2))
    root.geometry(f"{w}x{h}+{x}+{y}")


def main():
    root = tk.Tk()
    root.title("Ventana principal")

    background = tk.Label(root, text="Contenido de la ventana")
    background.pack()

    set_center(root, 400, 300)

    text = tk.Text(root, width=60, height=10)
    text.pack(expand=True, fill="both", padx=10, pady=10)

    PopMenu(text)

    root.mainloop()


if __name__ == "__main__":
    main()
