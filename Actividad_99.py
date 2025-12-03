# coding:utf-8
import traceback
from tkinter import Tk, Label, Button, Entry, StringVar, END, E, W
from functools import partial


def get_input(entry, arg):
    """Inserta un carácter en la entrada."""
    entry.insert(END, arg)


def backspace(entry):
    """Borra el último carácter."""
    input_len = len(entry.get())
    if input_len > 0:
        entry.delete(input_len - 1)


def clear(entry):
    """Limpia la entrada."""
    entry.delete(0, END)


def calc(entry, var):
    """Evalúa la expresión matemática."""
    text = entry.get()
    try:
        output = str(eval(text.strip()))
    except SyntaxError:
        output = "SyntaxError"
    except ZeroDivisionError:
        output = "ZeroDivisionError"
    except Exception as exc:  # cualquier otro error
        output = f"Error: {exc}"
    clear(entry)
    var.set(output)


def invoke(button):
    button.config(state="active")
    button.invoke()


def cal():
    """Ventana principal de la calculadora."""
    root = Tk()
    root.title("Calc")
    root.resizable(0, 0)

    var = StringVar()
    var.set("")

    label = Label(root, textvariable=var, anchor="e", width=30, font=("Arial", 16))
    label.grid(row=0, column=0, columnspan=4, sticky="nwse", padx=5, pady=2)

    entry = Entry(root, justify="right")
    entry.grid(row=1, column=0, columnspan=4, sticky="nwse", padx=5, pady=10)

    button_bg = "#e0f0e0"
    button_active_bg = "#f0e0f0"

    my_button = partial(
        Button, root, bg=button_bg, activebackground=button_active_bg, font=("Arial", 12)
    )

    button_list = [
        ("7", "<Key-7>", "<KeyRelease-7>"),
        ("8", "<Key-8>", "<KeyRelease-8>"),
        ("9", "<Key-9>", "<KeyRelease-9>"),
        ("+", "<plus>", "<KeyRelease-plus>"),
        ("4", "<Key-4>", "<KeyRelease-4>"),
        ("5", "<Key-5>", "<KeyRelease-5>"),
        ("6", "<Key-6>", "<KeyRelease-6>"),
        ("-", "<minus>", "<KeyRelease-minus>"),
        ("1", "<Key-1>", "<KeyRelease-1>"),
        ("2", "<Key-2>", "<KeyRelease-2>"),
        ("3", "<Key-3>", "<KeyRelease-3>"),
        ("*", "<asterisk>", "<KeyRelease-asterisk>"),
        ("0", "<Key-0>", "<KeyRelease-0>"),
        (".", "<period>", "<KeyRelease-period>"),
        ("/", "<slash>", "<KeyRelease-slash>"),
        ("<-", "<BackSpace>", "<KeyRelease-BackSpace>"),
        ("C", "<Delete>", "<KeyRelease-Delete>"),
        ("=", "<Return>", "<KeyRelease-Return>"),
    ]

    for i, triple in enumerate(button_list):
        text, key, key_release = triple

        row = (i // 4 + 2)
        column = (i % 4)
        columnspan = 1
        command = lambda text=text: get_input(entry, text)

        if text == "<-":
            command = lambda: backspace(entry)
        elif text == "C":
            command = lambda: clear(entry)
        elif text == "=":
            command = lambda: calc(entry, var)

        but = my_button(text=text, command=command)
        e_press_command = lambda event, but=but: invoke(but)
        e_release_command = lambda event, but=but: but.config(state="normal")
        root.bind(key, e_press_command)
        root.bind(key_release, e_release_command)
        but.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=3,
            pady=5,
            sticky=E + W,
        )

    root.mainloop()


if __name__ == "__main__":
    cal()
