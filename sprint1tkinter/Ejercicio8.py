"""
Ejercicio 8: Frame
Diseña una interfaz dividida en dos Frame:
• El Frame superior debe contener dos etiquetas y un campo de entrada.
• El Frame inferior debe tener dos botones:
• Uno para mostrar el contenido del Entry en una etiqueta.
• Otro para borrar su contenido.

Puedes organizar los widgets con grid() dentro de cada Frame.*
"""

import tkinter as tk


def primer_frame():
    root = tk.Tk()
    root.title('Ventana Tkinter')
    root.geometry("300x300")

    # Frame superior
    frame_superior = tk.Frame(root, bg="lightgrey", bd=2, relief="sunken")
    frame_superior.pack(pady=10)

    label1 = tk.Label(frame_superior, text="etiqueta 1 del frame")
    label1.grid(row=0, column=0, padx=5, pady=5)

    label2 = tk.Label(frame_superior, text="etiqueta 2 del frame")
    label2.grid(row=1, column=0, padx=5, pady=5)

    entry = tk.Entry(frame_superior, width=30)
    entry.grid(row=2, rowspan=2, padx=5, pady=5)

    # Frame inferior
    frame_inferior = tk.Frame(root, bg="lightgrey", bd=2, relief="sunken")
    frame_inferior.pack(pady=10)

    lshowcontent = tk.Label(frame_inferior, text="")
    lshowcontent.grid(row=0, column=0, columnspan=2, pady=5)

    def show_content():
        lshowcontent.config(text=entry.get())

    def delete_content():
        entry.delete(0, tk.END)
        lshowcontent.config(text="")

    # Botones
    boton_show = tk.Button(frame_inferior, text="Mostrar", command=show_content)
    boton_show.grid(row=1, column=0, padx=10, pady=5)

    boton_delete = tk.Button(frame_inferior, text="Borrar", command=delete_content)
    boton_delete.grid(row=1, column=1, padx=10, pady=5)

    root.mainloop()

primer_frame()
