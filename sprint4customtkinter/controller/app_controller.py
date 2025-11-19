# controller/app_controller.py
from model.usuario_model import GestorUsuarios
from view.main_view import MainView

class AppController:
    def __init__(self):
        # Instanciar el modelo
        self.gestor_usuarios = GestorUsuarios()

        # Instanciar la vista
        self.vista = MainView()

        # Llamada inicial para poblar la lista
        self.refrescar_lista_usuarios()

    # AppController
    def refrescar_lista_usuarios(self):
        usuarios = self.gestor_usuarios.listar()
        self.vista.actualizar_lista_usuarios(
            usuarios,
            on_seleccionar_callback=self.seleccionar_usuario  # recibe el objeto Usuario
        )

    def seleccionar_usuario(self, usuario):
        # usuario ya es un objeto Usuario
        self.vista.mostrar_detalles_usuario(usuario)

