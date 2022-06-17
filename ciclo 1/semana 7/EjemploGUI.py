import tkinter as tk
from tkinter import ttk

# Crear una ventana
ventana = tk.Tk()
ventana.title("Tareas CRUD v1.0")
ventana.geometry("600x400")
boton1 = ttk.Button(ventana, text="Agregar")
boton1.pack()
ventana.mainloop()
