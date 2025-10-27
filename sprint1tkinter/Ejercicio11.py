"""Ejercicio 11: Scale
Crea una barra deslizante (Scale) que permita al usuario seleccionar un número entre 0 y
100.
El valor seleccionado debe mostrarse en tiempo real en una etiqueta.
Usa command=funcion en la Scale para actualizar la etiqueta cada vez que se mueva el
control.*"""

import tkinter as tk

def primera_scale():

    root = tk.Tk()
    root.title('Ventana Tkinter')
    root.geometry("400x300")

    def actualizar_valor(val):
        etiqueta.config(text=f"Valor: {val}")

    scale=tk.Scale(root, from_=0,to=100, orient="horizontal", command=actualizar_valor)
    scale.pack()

    etiqueta=tk.Label(root, text="valor: 0")
    etiqueta.pack(pady=10)

    root.mainloop()

primera_scale()