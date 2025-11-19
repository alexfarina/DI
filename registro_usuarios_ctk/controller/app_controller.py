from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, AddUserView
from pathlib import Path
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import threading
import time


class AppController:
    def __init__(self, master_app: ctk.CTk):
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"
        self.DATA_PATH = self.BASE_DIR / "usuarios.csv"
        self.master = master_app

        self.usuario_seleccionado = None
        self.avatar_images = {}

        # --- de Hilo de Auto-guardado ---
        self.auto_save_thread = None
        self.stop_thread_event = threading.Event()
        self.auto_save_interval = 10
        self.save_in_progress = False

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.gestor_usuarios = GestorUsuarios(data_path=self.DATA_PATH)
        self.vista = MainView(master=self.master)

        # conexión de Callbacks de la View
        self.vista.filtrar_callback = self.filtrar_usuarios
        self.vista.add_button.configure(command=self.abrir_ventana_añadir)
        self.vista.delete_button.configure(command=self.eliminar_usuario_seleccionado)
        self.vista.auto_save_button.configure(command=self.toggle_auto_save)

        # menú
        self.vista.menu_archivo.add_command(label="Guardar", command=self.guardar_usuarios)
        self.vista.menu_archivo.add_command(label="Cargar", command=self.cargar_usuarios)
        self.vista.menu_archivo.add_command(label="Salir", command=self.on_closing)

        self.cargar_usuarios()
        self.vista.update_auto_save_button("DESACTIVADO")

    # --- métodos de Control de Hilo ---

    def start_auto_save_thread(self):
        """Inicia el hilo de auto-guardado."""
        if self.auto_save_thread is None or not self.auto_save_thread.is_alive():
            self.stop_thread_event.clear()
            self.auto_save_thread = threading.Thread(target=self._auto_save_loop, daemon=True)
            self.auto_save_thread.start()
            self.vista.update_auto_save_button("ACTIVO")
            self.vista.actualizar_barra_estado(len(self.gestor_usuarios.listar()),
                                               f" - Auto-guardado iniciado ({self.auto_save_interval}s)")

    def stop_auto_save_thread(self):
        if self.auto_save_thread and self.auto_save_thread.is_alive():
            self.stop_thread_event.set()
            self.vista.update_auto_save_button("DESACTIVADO")
            self.vista.actualizar_barra_estado(len(self.gestor_usuarios.listar()), " - Auto-guardado detenido")
            self.auto_save_thread.join(timeout=1)

    def toggle_auto_save(self):
        if self.auto_save_thread and self.auto_save_thread.is_alive():
            self.stop_auto_save_thread()
        else:
            self.start_auto_save_thread()

    def _auto_save_loop(self):
        while not self.stop_thread_event.is_set():
            self.stop_thread_event.wait(self.auto_save_interval)

            if not self.stop_thread_event.is_set():
                self.save_in_progress = True
                self.gestor_usuarios.guardar_csv()
                self.save_in_progress = False

                self.master.after(0, self._notify_save_complete)

    def _notify_save_complete(self):
        self.vista.actualizar_barra_estado(len(self.gestor_usuarios.listar()), " - Auto-guardado OK")

    def on_closing(self):
        self.stop_auto_save_thread()
        self.master.destroy()


    def guardar_usuarios(self):
        if self.save_in_progress:
            self.vista.actualizar_barra_estado(len(self.gestor_usuarios.listar()),
                                               " - Esperando a que termine el auto-guardado...")
            self.master.after(500, self.guardar_usuarios)
            return

        self.gestor_usuarios.guardar_csv()
        self.vista.actualizar_barra_estado(len(self.gestor_usuarios.listar()), " - Guardado MANUAL OK")

    def cargar_usuarios(self):
        self.gestor_usuarios.cargar_csv()
        self.refrescar_lista_usuarios()
        self.vista.actualizar_barra_estado(len(self.gestor_usuarios.listar()), " - Datos cargados")

    def refrescar_lista_usuarios(self):
        usuarios = self.gestor_usuarios.listar()
        self.vista.usuarios = usuarios
        self.vista.actualizar_lista_usuarios(
            usuarios,
            on_seleccionar_callback=self.seleccionar_usuario
        )
        if usuarios:
            self.seleccionar_usuario(0)
        else:
            self.vista.mostrar_detalles_usuario(None)

    # ⬅️ LÓGICA DE SELECCIÓN CORREGIDA
    def seleccionar_usuario(self, indice: int):
        """Muestra los detalles del usuario y guarda el OBJETO seleccionado."""

        if 0 <= indice < len(self.vista.usuarios):
            usuario = self.vista.usuarios[indice]

            self.usuario_seleccionado = usuario

            self.vista.mostrar_detalles_usuario(usuario, self.cargar_imagen_avatar)
        else:
            self.vista.mostrar_detalles_usuario(None)
            self.usuario_seleccionado = None

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
        self.vista.actualizar_barra_estado(len(self.gestor_usuarios.listar()),
                                           f" - Usuario '{nuevo_usuario.nombre}' registrado")

    def filtrar_usuarios(self, genero="Todos", texto_busqueda=""):
        texto_busqueda = texto_busqueda or ""
        usuarios_filtrados = [
            u for u in self.gestor_usuarios.listar()
            if (genero == "Todos" or u.genero.lower() == genero.lower())
               and texto_busqueda.lower() in u.nombre.lower()
        ]
        self.vista.usuarios = usuarios_filtrados
        self.vista.actualizar_lista_usuarios(
            usuarios_filtrados,
            self.seleccionar_usuario
        )
        self.vista.actualizar_barra_estado(len(usuarios_filtrados))
        self.usuario_seleccionado = None  # Deseleccionar al filtrar

    def eliminar_usuario_seleccionado(self):

        usuario_a_eliminar = self.usuario_seleccionado

        if usuario_a_eliminar is None:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un usuario para eliminar.")
            return

        if messagebox.askyesno(
                "Confirmar Eliminación",
                f"¿Estás seguro de que quieres eliminar a '{usuario_a_eliminar.nombre}'?"
        ):
            try:
                self.gestor_usuarios.eliminar_por_objeto(usuario_a_eliminar)
            except AttributeError:
                messagebox.showerror("Error de Modelo",
                                     "El modelo 'GestorUsuarios' necesita el método 'eliminar_por_objeto'.")
                return

            self.usuario_seleccionado = None

            self.refrescar_lista_usuarios()
            self.vista.actualizar_barra_estado(
                len(self.gestor_usuarios.listar()),
                f" - Usuario '{usuario_a_eliminar.nombre}' ELIMINADO"
            )