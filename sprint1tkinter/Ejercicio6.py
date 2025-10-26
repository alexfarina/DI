"""Ejercicio 6: Listbox
Crea una lista (Listbox) con varias frutas: “Manzana”, “Banana”, “Naranja”.
Al seleccionar una fruta y pulsar un botón, muestra el nombre de la fruta seleccionada en
una etiqueta.
Usa curselection() y get() para obtener el elemento activo."""

import tkinter as tk


def primera_listbox():
    root = tk.Tk()
    root.title('Ventana Tkinter')
    root.geometry("300x300")

    def show_selects():
        select=listbox.curselection()
        elements=[listbox.get(i) for i in select]
        label.config(text="Seleccionaste: " + ", ".join(elements))

    fruits=["Manzana", "Banana", "Naranja"]

    #Crear Listbox
    listbox=tk.Listbox(root,selectmode=tk.MULTIPLE)
    for fruit in fruits:
        listbox.insert(tk.END,fruit)

    listbox.pack()

    buttom=tk.Button(root, text="Mostrar selección", command=show_selects)
    buttom.pack()

    label=tk.Label(root, text="Seleccionaste: Ninguno")
    label.pack()

    root.mainloop()

primera_listbox()