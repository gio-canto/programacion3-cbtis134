import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Label: Hello Tkinter")
    window.geometry("300x200")

    greeting = tk.Label(window, text="Hello, Tkinter", font=("Arial", 16))
    greeting.pack(pady=40)

    window.mainloop()


if __name__ == "__main__":
    main()
