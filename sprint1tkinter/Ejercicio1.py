"""Ejercicio 1: Label
Crea una ventana que muestre tres etiquetas (Label):
1. La primera debe mostrar un mensaje de bienvenida.
2. La segunda debe mostrar tu nombre completo.
3. La tercera debe cambiar su texto cuando se presione un botón.
Usa config(text="nuevo texto") dentro de la función asociada al botón."""

import tkinter as tk

if __name__ == '__main__':
    def primerasEtiquetas():
        # Ventana principal
        root = tk.Tk()  # crea un objeto de la clase Tk
        root.title('Ventana Tkinter')
        root.geometry("300x150")

        # Etiquetas
        lwelcome = tk.Label(root, text="¡Bienvenido!")
        lname = tk.Label(root, text="Alex Fariña Caamaño")
        ledittext = tk.Label(root, text="Texto viejo")

        def cambiar_texto():
            ledittext.config(text="Nuevo texto")

        # Botón para cambiar el texto
        boton = tk.Button(root, text="Cambiar texto", command=cambiar_texto)

        # Mostrar los elementos en la ventana
        lwelcome.pack()
        lname.pack()
        ledittext.pack()
        boton.pack()

        # Bucle principal
        root.mainloop()

    # Llamamos a la función
    primerasEtiquetas()
