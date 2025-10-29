"""Ejercicio 12: Aplicación de Registro de Usuarios
Desarrolla una aplicación de registro de usuarios que contenga:
1. Campo Entry para el nombre.
2. Scale para la edad (0–100 años).
3. Tres Radiobutton para el género (masculino, femenino, otro).
4. Botón “Añadir” para guardar un usuario en una lista.
5. Listbox con todos los usuarios registrados (nombre, edad y género).
6. Scrollbar vertical para la lista.
7. Botón “Eliminar” para borrar el usuario seleccionado.
8. Botón “Salir” para cerrar la aplicación.
9. Menú con opciones “Guardar Lista” y “Cargar Lista” que muestren un messagebox.
Puedes empezar construyendo la interfaz paso a paso, probando que cada parte
funcione antes de continuar.
"""

import tkinter as tk
from tkinter import messagebox

def registrar_usuarios():
    root = tk.Tk()
    root.title("Registro de Usuarios")
    root.geometry("400x400")

    # Lista de usuarios
    usuarios = []

    # Entrada Nombre
    tk.Label(root, text="Nombre:").pack()
    entry_nombre = tk.Entry(root, width=30)
    entry_nombre.pack(pady=5)

    # Scale Edad
    tk.Label(root, text="Edad:").pack()
    escala_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
    escala_edad.pack(pady=5)

    # Género
    tk.Label(root, text="Género:").pack()
    genero = tk.StringVar(value="Otro")
    tk.Radiobutton(root, text="Masculino", variable=genero, value="Masculino").pack()
    tk.Radiobutton(root, text="Femenino", variable=genero, value="Femenino").pack()
    tk.Radiobutton(root, text="Otro", variable=genero, value="Otro").pack()

    # Listbox y Scrollbar
    frame_lista = tk.Frame(root)
    frame_lista.pack(pady=10, fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_lista, orient="vertical")
    listbox = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, width=50, height=8)
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="right", fill="y")
    listbox.pack(side="left", fill="both", expand=True)

    # Funciones
    def anadir_usuario():
        nombre = entry_nombre.get().strip() # .strip elimina espacios en blanco
        edad = escala_edad.get()
        gen = genero.get()
        if nombre:
            usuario = f"{nombre} - {edad} años - {gen}"
            usuarios.append(usuario)
            listbox.insert(tk.END, usuario)
            entry_nombre.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "El nombre no puede estar vacío.")

    def eliminar_usuario():
        seleccion = listbox.curselection()
        if seleccion:
            for i in reversed(seleccion):
                listbox.delete(i)
                usuarios.pop(i)
        else:
            messagebox.showwarning("Error", "Selecciona un usuario para eliminar.")

    def salir():
        root.destroy()

    def guardar_lista():
        messagebox.showinfo("Guardar Lista", "Lista guardada correctamente.")

    def cargar_lista():
        messagebox.showinfo("Cargar Lista", "Lista cargada correctamente.")

    # Botones
    tk.Button(root, text="Añadir", command=anadir_usuario).pack(pady=5)
    tk.Button(root, text="Eliminar", command=eliminar_usuario).pack(pady=5)
    tk.Button(root, text="Salir", command=salir).pack(pady=5)

    # Menú
    menu_principal = tk.Menu(root)
    root.config(menu=menu_principal)

    menu_archivo = tk.Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
    menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
    menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=salir)

    root.mainloop()

# Ejecutar aplicación
if __name__ == "__main__":
    registrar_usuarios()
