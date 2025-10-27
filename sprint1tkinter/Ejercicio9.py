"""Ejercicio 9: Menú
Crea una barra de menú en la ventana con los siguientes elementos:
• Menú “Archivo” → opciones “Abrir” y “Salir”.
• Menú “Ayuda” → opción “Acerca de”.
La opción “Salir” debe cerrar la aplicación, y “Acerca de” debe mostrar un mensaje en una
ventana emergente.
Usa messagebox.showinfo("Acerca de", "texto") para mostrar el cuadro de diálogo.
"""

import tkinter as tk
from tkinter import messagebox

def crear_menu():
    root = tk.Tk()
    root.title('Ventana Tkinter')
    root.geometry("300x300")

    # Funciones de las opciones del menú
    def abrir_archivo():
        messagebox.showinfo("Abrir", "Abrir archivo seleccionado.")

    def salir_aplicacion():
        root.quit()

    def mostrar_acerca_de():
        messagebox.showinfo("Acerca de", "Aplicación de ejemplo.")

    # Crear barra de menú principal
    menu_principal = tk.Menu(root)
    root.config(menu=menu_principal)

    # Menú "Archivo"
    menu_archivo = tk.Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
    menu_archivo.add_command(label="Abrir", command=abrir_archivo)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=salir_aplicacion)

    # Menú "Ayuda"
    menu_ayuda = tk.Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
    menu_ayuda.add_command(label="Acerca de", command=mostrar_acerca_de)

    root.mainloop()

crear_menu()
