# view/main_view.py
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path


class AddUserView:
    def __init__(self, master, avatar_loader_callback):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("450x450")
        self.window.resizable(False, False)
        self.window.grab_set()

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=3)

        self.avatar_seleccionado = ctk.StringVar(value="avatar1.jpg")
        self.avatar_loader_callback = avatar_loader_callback

        ctk.CTkLabel(self.window, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.nombre_entry = ctk.CTkEntry(self.window)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self.window, text="Edad:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.edad_entry = ctk.CTkEntry(self.window)
        self.edad_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self.window, text="Género:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.genero_var = ctk.StringVar(value="hombre")

        gender_frame = ctk.CTkFrame(self.window)
        gender_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        ctk.CTkRadioButton(gender_frame, text="Hombre", variable=self.genero_var, value="hombre").pack(side="left",
                                                                                                       padx=10)
        ctk.CTkRadioButton(gender_frame, text="Mujer", variable=self.genero_var, value="mujer").pack(side="left",
                                                                                                     padx=10)

        ctk.CTkLabel(self.window, text="Avatar:").grid(row=3, column=0, padx=10, pady=5, sticky="nw")
        self.avatar_frame = ctk.CTkFrame(self.window)
        self.avatar_frame.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        self.setup_avatar_selection()

        self.guardar_button = ctk.CTkButton(self.window, text="Guardar Usuario")
        self.guardar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

    def setup_avatar_selection(self):
        avatar_files = [f"avatar{i}.jpg" for i in range(1, 5)]

        for i, filename in enumerate(avatar_files):
            btn = ctk.CTkRadioButton(
                self.avatar_frame,
                text=filename,
                variable=self.avatar_seleccionado,
                value=filename
            )
            btn.pack(anchor="w", pady=2)

    def get_data(self):
        return {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_entry.get(),
            "genero": self.genero_var.get(),
            "avatar": self.avatar_seleccionado.get(),
        }


class MainView:
    def __init__(self, master):
        self.master = master
        self.right_frame = None
        self.scrollable_frame = None
        self.botones_usuarios = []
        self.current_avatar_photo = None

        self.menubar = tk.Menu(master)
        master.config(menu=self.menubar)
        self.menu_archivo = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)

        self._setup_ui()

    def _setup_ui(self):
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=2)
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=0)


        self.header = ctk.CTkFrame(self.master, height=60)
        self.header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 5))

        header_label = ctk.CTkLabel(self.header, text="Header")
        header_label.pack(pady=10)

        self.left_container = ctk.CTkFrame(self.master)
        self.left_container.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.left_container.grid_rowconfigure(0, weight=1)
        self.left_container.grid_columnconfigure(0, weight=1)

        self.scrollable_frame = ctk.CTkScrollableFrame(self.left_container, label_text="Usuarios Registrados")
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)


        self.right_frame = ctk.CTkFrame(self.master)
        self.right_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.label_avatar_img = ctk.CTkLabel(self.right_frame, text="Avatar", width=150, height=150)
        self.label_avatar_img.pack(anchor="n", pady=(20, 10), padx=10)

        self.details_frame = ctk.CTkFrame(self.right_frame)
        self.details_frame.pack(fill="x", padx=20, pady=10)
        self.details_frame.columnconfigure(0, weight=1)

        self.label_nombre = ctk.CTkLabel(self.details_frame, text="Nombre: ---")
        self.label_nombre.grid(row=0, column=0, sticky="w", pady=5)

        self.label_edad = ctk.CTkLabel(self.details_frame, text="Edad: ---")
        self.label_edad.grid(row=1, column=0, sticky="w", pady=5)

        self.label_genero = ctk.CTkLabel(self.details_frame, text="Género: ---")
        self.label_genero.grid(row=2, column=0, sticky="w", pady=5)

        self.label_avatar = ctk.CTkLabel(self.details_frame, text="Archivo Avatar: ---")
        self.label_avatar.grid(row=3, column=0, sticky="w", pady=5)

        self.footer = ctk.CTkFrame(self.master, height=60)
        self.footer.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 5))

        self.add_button = ctk.CTkButton(self.footer, text="+ Añadir Usuario")
        self.add_button.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for btn in self.botones_usuarios:
            btn.destroy()
        self.botones_usuarios.clear()

        for i, u in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.scrollable_frame,
                text=u.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", pady=2)
            self.botones_usuarios.append(btn)

        if not usuarios:
            self.mostrar_detalles_usuario(None)

    def mostrar_detalles_usuario(self, usuario, image_loader_callback=None):
        if usuario is None:
            self.label_nombre.configure(text="Nombre: ---")
            self.label_edad.configure(text="Edad: ---")
            self.label_genero.configure(text="Género: ---")
            self.label_avatar.configure(text="Archivo Avatar: ---")
            self.label_avatar_img.configure(image=None, text="Avatar")
            self.current_avatar_photo = None
            return

        self.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.label_edad.configure(text=f"Edad: {usuario.edad}")
        self.label_genero.configure(text=f"Género: {usuario.genero}")
        self.label_avatar.configure(text=f"Archivo Avatar: {usuario.avatar}")

        if image_loader_callback and usuario.avatar:
            try:
                ctk_img, photo_img = image_loader_callback(usuario.avatar, size=(150, 150))

                if ctk_img:
                    self.label_avatar_img.configure(image=ctk_img, text="")
                    self.current_avatar_photo = photo_img
                else:
                    self.label_avatar_img.configure(image=None, text="Avatar no cargado")
                    self.current_avatar_photo = None
            except Exception:
                self.label_avatar_img.configure(image=None, text="Error de imagen")
                self.current_avatar_photo = None