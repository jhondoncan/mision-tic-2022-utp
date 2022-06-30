import CRUD
import interfazGUI as iGUI
import tkinter as tk
from tkinter import ttk
import sys


# Cargar el archivo JSON con las tareas
tareas = CRUD.Read()
if not(tareas):
    sys.exit()


# Cargaar Interfaz grafica
m = iGUI.ventanaMenuPrincipal(tareas)
# Mostrar ventana
m.mainloop()
