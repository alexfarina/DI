import tkinter as tk

def primer_canvas():
    root = tk.Tk()
    root.title('Canvas interactivo')
    root.geometry("600x700")

    # Canvas fijo
    canvas_width = 400
    canvas_height = 400
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack(pady=10)

    # Labels y Entradas
    tk.Label(root, text="x1:").pack()
    entry_x1 = tk.Entry(root)
    entry_x1.pack()

    tk.Label(root, text="y1:").pack()
    entry_y1 = tk.Entry(root)
    entry_y1.pack()

    tk.Label(root, text="x2:").pack()
    entry_x2 = tk.Entry(root)
    entry_x2.pack()

    tk.Label(root, text="y2:").pack()
    entry_y2 = tk.Entry(root)
    entry_y2.pack()

    # Función para dibujar
    def dibujar():
        try:
            x1 = int(entry_x1.get())
            y1 = int(entry_y1.get())
            x2 = int(entry_x2.get())
            y2 = int(entry_y2.get())
        except ValueError:
            return  # si no son números, no hace nada

        canvas.delete("all")  # limpia el canvas antes de dibujar
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
        canvas.create_oval(x1, y1, x2, y2, fill="red")

    # Botón para dibujar
    tk.Button(root, text="Dibujar", command=dibujar).pack(pady=10)

    root.mainloop()

primer_canvas()
