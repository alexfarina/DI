"""Ejercicio 10: Scrollbar
Crea un Text con un texto largo (varios párrafos) y añade una barra de desplazamiento
vertical (Scrollbar).
Recuerda conectar ambos widgets con yscrollcommand y command:
scroll.config(command=texto.yview) y texto.config(yscrollcommand=scroll.set)."""
import tkinter
import tkinter as tk

def primera_scrollbar():
        def insertar_texto():
            for i in range(1, 101):
                cuadro_texto.insert(tk.END, f"Linea {i}\n")

        root = tk.Tk()
        root.title('Ventana Tkinter')
        root.geometry("400x300")

        frame=tk.Frame(root)
        frame.pack(fill="both", expand=True)

        cuadro_texto=tkinter.Text(frame ,wrap="none")
        cuadro_texto.grid(row=0, column=0 ,sticky="nsew")

        scroll_ver=tk.Scrollbar(frame, orient="vertical",command=cuadro_texto.yview)
        scroll_ver.grid(row=0,column=1,sticky="ns")
        cuadro_texto.config(yscrollcommand=scroll_ver.set)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        insertar_texto()

        root.mainloop()

primera_scrollbar()