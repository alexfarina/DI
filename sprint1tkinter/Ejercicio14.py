"""Ejercicio 14: Aplicación con clases
Reescribe la Aplicación de Registro de Usuarios (Ejercicio 12) empleando una clase
RegistroApp.
La clase debe:
1. Definirse como class RegistroApp:.
2. Crear todos los widgets dentro del método __init__(self, root).
3. Definir métodos para las acciones:
• añadir_usuario(self)
• eliminar_usuario(self)
• salir(self)
4. Crear la instancia con:
        root=tk.Tk()
        app=RegistroApp(root)
        root.mainloopt()
"""

import tkinter as tk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuarios")
        self.root.geometry("400x400")

        # Lista de usuarios
        self.usuarios = []

        # Entrada Nombre
        tk.Label(root, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(root, width=30)
        self.entry_nombre.pack(pady=5)

        # Scale Edad
        tk.Label(root, text="Edad:").pack()
        self.escala_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.escala_edad.pack(pady=5)

        # Género
        tk.Label(root, text="Género:").pack()
        self.genero = tk.StringVar(value="Otro")
        tk.Radiobutton(root, text="Masculino", variable=self.genero, value="Masculino").pack()
        tk.Radiobutton(root, text="Femenino", variable=self.genero, value="Femenino").pack()
        tk.Radiobutton(root, text="Otro", variable=self.genero, value="Otro").pack()

        # Listbox y Scrollbar
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10, fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(frame_lista, orient="vertical")
        self.listbox = tk.Listbox(frame_lista, yscrollcommand=self.scrollbar.set, width=50, height=8)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.pack(side="left", fill="both", expand=True)

        # Botones
        tk.Button(root, text="Añadir", command=self.anadir_usuario).pack(pady=5)
        tk.Button(root, text="Eliminar", command=self.eliminar_usuario).pack(pady=5)
        tk.Button(root, text="Salir", command=self.salir).pack(pady=5)

        # Menú
        menu_principal = tk.Menu(root)
        root.config(menu=menu_principal)

        menu_archivo = tk.Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        menu_archivo.add_command(label="Cargar Lista", command=self.cargar_lista)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.salir)

    # Métodos
    def anadir_usuario(self):
        nombre = self.entry_nombre.get().strip()
        edad = self.escala_edad.get()
        gen = self.genero.get()

        if nombre:
            usuario = f"{nombre} - {edad} años - {gen}"
            self.usuarios.append(usuario)
            self.listbox.insert(tk.END, usuario)
            self.entry_nombre.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "El nombre no puede estar vacío.")

    def eliminar_usuario(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            for i in reversed(seleccion):
                self.listbox.delete(i)
                self.usuarios.pop(i)
        else:
            messagebox.showwarning("Error", "Selecciona un usuario para eliminar.")

    def guardar_lista(self):
        messagebox.showinfo("Guardar Lista", "Lista guardada correctamente.")

    def cargar_lista(self):
        messagebox.showinfo("Cargar Lista", "Lista cargada correctamente.")

    def salir(self):
        self.root.destroy()

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()
