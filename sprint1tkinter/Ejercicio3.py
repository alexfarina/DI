"""Ejercicio 3: Entry
Crea una interfaz con un campo de entrada (Entry) donde el usuario escriba su nombre.
Al hacer clic en un botón, debe mostrarse un saludo personalizado en una etiqueta.
Prueba a usar entrada.get() para obtener el texto del usuario."""

import tkinter as tk

if __name__ == '__main__':
    def primera_entrada():
        root = tk.Tk()  # crea un objeto de la clase Tk
        root.title('Ventana Tkinter')
        root.geometry("300x150")

        def obtener_texto():
            text=entry.get()
            lres.config(text=f"Buenas  {text} !")

        #widgets
        lname = tk.Label(root, text="Cúal es tu nombre: ")
        lname.pack()

        entry=tk.Entry(root, width=30)
        entry.pack()

        buttom=tk.Button(root ,text="Ver nombre" , command=obtener_texto)
        buttom.pack()

        lres = tk.Label(root, text="")
        lres.pack()

        #Ejecutar el bucle principal
        root.mainloop()

primera_entrada()

