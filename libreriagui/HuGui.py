import tkinter as tk
from tkinter import messagebox

class HuGui:

    def __init__(self):
        self.root = None

    def crear_ventana_main(self, a, b, c):
        self.root = tk.Tk()
        self.root.configure(bg=a)
        self.root.geometry(b)
        self.root.title(c)

    def mostrar_mensaje_gui_info(self, a, b):
        messagebox.showinfo(a, b)

    def mostrar_mensaje_gui_advertencia(self, a, b):
        messagebox.showwarning(a, b)

    def mostrar_mensaje_gui_error(self, a, b):
        messagebox.showerror(a, b)

    def preguntar_si_no(self, a, b, c, d, e, f, g):
        pregunta = messagebox.askyesno(a, b, icon=c)
        if pregunta:
            messagebox.showinfo(d, e)
        else:
            messagebox.showinfo(f, g)