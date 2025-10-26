import tkinter as tk

def primeros_radiobutton():
    root = tk.Tk()
    root.title('Ventana Tkinter')
    root.geometry("300x150")

    # Variable compartida para los radiobuttons
    color_var = tk.StringVar()
    color_var.set(None)

    # Función para actualizar el color de fondo
    def actualizar():
        color = color_var.get()
        if color:
            root.config(bg=color)
            rb_rojo.config(bg=color)
            rb_verde.config(bg=color)
            rb_azul.config(bg=color)

    # Radiobuttons
    rb_rojo = tk.Radiobutton(root, text="Rojo", variable=color_var, value="red", command=actualizar)
    rb_verde = tk.Radiobutton(root, text="Verde", variable=color_var, value="green", command=actualizar)
    rb_azul = tk.Radiobutton(root, text="Azul", variable=color_var, value="blue", command=actualizar)

    rb_rojo.pack()
    rb_verde.pack()
    rb_azul.pack()

    root.mainloop()

primeros_radiobutton()
