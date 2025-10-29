"""Ejercicio 13: Eventos de teclado y ratón (nuevo)
Crea una ventana con un Canvas que dibuje un círculo en la posición donde el usuario
haga clic con el ratón.
Además, si el usuario presiona la tecla “c”, el Canvas debe borrarse.
• Usa canvas.bind("<Button-1>", funcion) para detectar clics.
• Obtén las coordenadas con event.x y event.y.
• Usa canvas.delete("all") para limpiar."""

import tkinter as tk

root = tk.Tk()
root.title('Eventos de teclado y ratón')
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=10)


def click(event):
    x, y = event.x, event.y
    radio = 15
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="red")

def limpiar(event):
    if event.char.lower() == "c":
        canvas.delete("all")

# Asociar eventos
canvas.bind("<Button-1>", click)  # clic izquierdo
root.bind("<Key>", limpiar)

root.mainloop()
