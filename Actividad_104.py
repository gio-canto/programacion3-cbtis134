#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR = BASE_DIR / "img"
DATA_FILE = BASE_DIR / "usr_info.pickle"


def center_window(window: tk.Tk | tk.Toplevel, w: int, h: int) -> None:
    """Centra la ventana en la pantalla."""
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()
    x = int((screen_w - w) / 2)
    y = int((screen_h - h) / 2)
    window.geometry(f"{w}x{h}+{x}+{y}")


def ensure_user_db() -> dict:
    """Carga el archivo de usuarios o lo crea si no existe."""
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("rb") as f:
                data = pickle.load(f)
                if isinstance(data, dict):
                    return data
        except Exception:
            pass

    users = {"admin": "admin"}
    with DATA_FILE.open("wb") as f:
        pickle.dump(users, f)
    return users


def save_user_db(users: dict) -> None:
    """Guarda el diccionario de usuarios."""
    with DATA_FILE.open("wb") as f:
        pickle.dump(users, f)


def create_main_window():
    window = tk.Tk()
    window.title("Bienvenido al sistema de aprendizaje")
    center_window(window, 500, 310)
    window.wm_attributes("-topmost", 1)

    # Fondo
    canvas = tk.Canvas(window, height=300, width=500)
    try:
        bg_image = tk.PhotoImage(file=str(IMG_DIR / "1.png"))
        canvas.background_image = bg_image  # Evitar GC
        canvas.create_image(0, 0, anchor="nw", image=bg_image)
    except Exception:
        pass
    canvas.pack(side="top")

    # Labels usuario / contraseña
    tk.Label(window, text="Nombre de usuario:").place(x=100, y=150)
    tk.Label(window, text="Contraseña:").place(x=100, y=190)

    var_usr_name = tk.StringVar()
    var_usr_pwd = tk.StringVar()

    entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
    entry_usr_name.place(x=220, y=150)

    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show="*")
    entry_usr_pwd.place(x=220, y=190)

    def usr_sign_quit():
        window.destroy()

    def show_info():
        window.withdraw()
        info_window = tk.Toplevel(window)
        center_window(info_window, 500, 658)
        info_window.wm_attributes("-topmost", 1)
        info_window.title("Bienvenido al mundo mágico")

        canvas_info = tk.Canvas(info_window, height=658, width=500)
        try:
            bg_info_image = tk.PhotoImage(file=str(IMG_DIR / "3.png"))
            canvas_info.background_image = bg_info_image
            canvas_info.create_image(0, 0, anchor="nw", image=bg_info_image)
        except Exception:
            pass
        canvas_info.pack(side="top")

        text_msg = "No matter how far you may fly, never forget where you come from."
        tk.Label(info_window, text=text_msg).place(x=25, y=100)
        tk.Label(info_window, text=text_msg).place(x=25, y=140)
        tk.Label(info_window, text=text_msg).place(x=25, y=180)

        tk.Button(info_window, text="Salir", command=usr_sign_quit).place(x=430, y=10)

        def on_close():
            window.destroy()

        info_window.protocol("WM_DELETE_WINDOW", on_close)

    def usr_sign_up():
        sign_window = tk.Toplevel(window)
        sign_window.title("Interfaz de registro")
        center_window(sign_window, 500, 310)
        sign_window.wm_attributes("-topmost", 1)

        canvas_sign = tk.Canvas(sign_window, height=300, width=500)
        try:
            bg_sign_image = tk.PhotoImage(file=str(IMG_DIR / "f1.png"))
            canvas_sign.background_image = bg_sign_image
            canvas_sign.create_image(0, 0, anchor="nw", image=bg_sign_image)
        except Exception:
            pass
        canvas_sign.pack(side="top")

        new_name = tk.StringVar()
        new_pwd = tk.StringVar()
        new_pwd_confirm = tk.StringVar()

        tk.Label(sign_window, text="Nombre de usuario:").place(x=100, y=100)
        tk.Entry(sign_window, textvariable=new_name).place(x=260, y=100)

        tk.Label(sign_window, text="Contraseña:").place(x=100, y=140)
        tk.Entry(sign_window, textvariable=new_pwd, show="*").place(x=260, y=140)

        tk.Label(sign_window, text="Confirmar contraseña:").place(x=100, y=180)
        tk.Entry(sign_window, textvariable=new_pwd_confirm, show="*").place(
            x=260, y=180
        )

        def signtowcg():
            nn = new_name.get().strip()
            np = new_pwd.get()
            npf = new_pwd_confirm.get()

            users = ensure_user_db()

            if nn in users:
                messagebox.showerror("Error", "El nombre de usuario ya existe")
            elif not nn or not np:
                messagebox.showerror("Error", "Nombre de usuario o contraseña vacíos")
            elif np != npf:
                messagebox.showerror("Error", "Las contraseñas no coinciden")
            else:
                users[nn] = np
                save_user_db(users)
                messagebox.showinfo("Bienvenido", "Registro exitoso")
                sign_window.destroy()

        tk.Button(sign_window, text="Confirmar registro", command=signtowcg).place(
            x=260, y=220
        )

    def usr_log_in():
        usr_name = var_usr_name.get().strip()
        usr_pwd = var_usr_pwd.get()

        users = ensure_user_db()

        if not usr_name or not usr_pwd:
            messagebox.showerror("Error", "Nombre de usuario o contraseña vacíos")
            return

        if usr_name in users:
            if usr_pwd == users[usr_name]:
                show_info()
            else:
                messagebox.showerror("Error", "Contraseña incorrecta")
        else:
            is_signup = messagebox.askyesno(
                "Bienvenido", "No estás registrado, ¿deseas registrarte ahora?"
            )
            if is_signup:
                usr_sign_up()

    tk.Button(window, text="Iniciar sesión", command=usr_log_in).place(x=140, y=230)
    tk.Button(window, text="Registrarse", command=usr_sign_up).place(x=230, y=230)
    tk.Button(window, text="Salir", command=usr_sign_quit).place(x=340, y=230)

    entry_usr_name.focus_set()
    return window


if __name__ == "__main__":
    app = create_main_window()
    app.mainloop()
