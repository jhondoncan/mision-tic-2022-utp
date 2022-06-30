import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Librería para interactuar con el backend
import CRUD


def ventanaMenuPrincipal(tareas):
    m = tk.Tk()
    m.title("Tareas CRUD v1.0")
    m.geometry("800x600")

    # Crear un frame para la tabla
    frameTabla = tk.Frame(m, borderwidth=2, relief="sunken")
    frameTabla.config(width=600, height=300)
    frameTabla.config(bg="lightblue")
    frameTabla.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")
    # Crear un frame para la imagen
    frameImagen = tk.Frame(m, borderwidth=2, relief="sunken")
    frameImagen.config(width=200, height=300)
    frameImagen.config(bg="lightblue")
    frameImagen.grid(row=0, column=2, rowspan=2, sticky="nsew")
    # Crear un frame para el crud
    frameCRUD = tk.Frame(m, borderwidth=2, relief="sunken")
    frameCRUD.config(width=600, height=300)
    frameCRUD.config(bg="lightblue")
    frameCRUD.grid(row=2, column=0, columnspan=2, sticky="nsew")
    # Crear un frame para los botones
    frameBotones = tk.Frame(m, borderwidth=2, relief="sunken")
    frameBotones.config(width=200, height=300)
    frameBotones.config(bg="lightblue")
    frameBotones.grid(row=2, column=2, sticky="nsew")

    return m
