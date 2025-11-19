# controller/app_controller.py
from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, AddUserView
from pathlib import Path
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ctk


class AppController:
    def __init__(self, master_app: ctk.CTk):
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"
        self.DATA_PATH = self.BASE_DIR / "usuarios.csv"
        self.master = master_app

        self.gestor_usuarios = GestorUsuarios(data_path=self.DATA_PATH)

        self.vista = MainView(master=self.master)

        self.avatar_images = {}

        self.vista.menu_archivo.add_command(label="Guardar", command=self.guardar_usuarios)
        self.vista.menu_archivo.add_command(label="Cargar", command=self.cargar_usuarios)

        self.vista.add_button.configure(command=self.abrir_ventana_añadir)

        self.cargar_usuarios()

    def guardar_usuarios(self):
        self.gestor_usuarios.guardar_csv()
        messagebox.showinfo("Éxito", "Datos guardados correctamente en usuarios.csv.")

    def cargar_usuarios(self):
        self.gestor_usuarios.cargar_csv()
        self.refrescar_lista_usuarios()
        messagebox.showinfo("Éxito", "Datos cargados.")

    def refrescar_lista_usuarios(self):
        usuarios = self.gestor_usuarios.listar()
        self.vista.actualizar_lista_usuarios(
            usuarios,
            on_seleccionar_callback=self.seleccionar_usuario
        )

    def seleccionar_usuario(self, indice):
        usuario = self.gestor_usuarios.obtener_usuario(indice)
        if usuario:
            self.vista.mostrar_detalles_usuario(usuario, self.cargar_imagen_avatar)

    def cargar_imagen_avatar(self, filename: str, size: tuple = (150, 150)):

        cache_key = (filename, size)
        if cache_key in self.avatar_images:
            return self.avatar_images[cache_key]

        ruta_imagen = self.ASSETS_PATH / filename

        if not ruta_imagen.exists():
            return None

        try:
            pil_image = Image.open(ruta_imagen)
            pil_image = pil_image.resize(size)

            ctk_image = ctk.CTkImage(light_image=pil_image, size=size)
            photo_image = ImageTk.PhotoImage(pil_image)

            self.avatar_images[cache_key] = (ctk_image, photo_image)
            return ctk_image, photo_image

        except Exception:
            return None

    def abrir_ventana_añadir(self):
        add_view = AddUserView(self.master, avatar_loader_callback=self.cargar_imagen_avatar)

        add_view.guardar_button.configure(
            command=lambda: self.añadir_usuario(add_view)
        )

    def añadir_usuario(self, add_view: AddUserView):
        data = add_view.get_data()

        if not data['nombre'] or not data['edad']:
            messagebox.showerror("Error de Validación", "El nombre y la edad son obligatorios.")
            return

        try:
            edad = int(data['edad'])
            if edad < 0 or edad > 120:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error de Validación", "La edad debe ser un número entero válido (0-120).")
            return

        nuevo_usuario = Usuario(
            nombre=data['nombre'],
            edad=edad,
            genero=data['genero'],
            avatar=data['avatar']
        )
        self.gestor_usuarios.agregar(nuevo_usuario)

        self.refrescar_lista_usuarios()
        add_view.window.destroy()
        messagebox.showinfo("Éxito", f"Usuario '{nuevo_usuario.nombre}' registrado.")