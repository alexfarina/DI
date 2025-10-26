import tkinter as tk

if __name__ == '__main__':
    def primerosBotones():
        # Ventana principal
        root = tk.Tk()  # crea un objeto de la clase Tk
        root.title('Ventana Tkinter')
        root.geometry("300x150")

        # Etiqueta vacía donde aparecerá el mensaje secreto
        lmensaje = tk.Label(root, text="")
        lmensaje.pack(pady=10)

        # Función para mostrar el mensaje secreto
        def mostrar_mensaje_secreto():
            lmensaje.config(text="Mensaje secreto: and his name is John Cena!")

        # Botón para mostrar el mensaje secreto
        buttom = tk.Button(root, text="Ver el mensaje secreto", command=mostrar_mensaje_secreto)
        buttom.pack(pady=5)

        # Botón para cerrar ventana
        lclosewindow = tk.Button(root, text="Cerrar ventana", command=root.quit)
        lclosewindow.pack(pady=5)

        # Bucle principal
        root.mainloop()

    # Llamamos a la función
    primerosBotones()
