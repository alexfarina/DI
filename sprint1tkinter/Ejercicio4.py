import tkinter as tk

def primeros_checkbutton():
    root = tk.Tk()
    root.title('Ventana Tkinter')
    root.geometry("300x150")

    # Variables
    var_leer = tk.IntVar()
    var_deporte = tk.IntVar()
    var_musica = tk.IntVar()

    # Etiqueta que mostrará las aficiones
    label = tk.Label(root, text="Aficiones seleccionadas: ")
    label.pack(pady=5)

    # Función para actualizar la etiqueta
    def actualizar():
        seleccionadas = []
        if var_leer.get() == 1:
            seleccionadas.append("Leer")
        if var_deporte.get() == 1:
            seleccionadas.append("Deporte")
        if var_musica.get() == 1:
            seleccionadas.append("Música")
        label.config(text="Aficiones seleccionadas: " + ", ".join(seleccionadas))

    # Checkbuttons
    cb_leer = tk.Checkbutton(root, text="Leer", variable=var_leer, command=actualizar)
    cb_deporte = tk.Checkbutton(root, text="Deporte", variable=var_deporte, command=actualizar)
    cb_musica = tk.Checkbutton(root, text="Música", variable=var_musica, command=actualizar)

    cb_leer.pack()
    cb_deporte.pack()
    cb_musica.pack()

    root.mainloop()

primeros_checkbutton()
