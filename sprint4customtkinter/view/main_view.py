# view/main_view.py
import customtkinter as ctk

class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Usuarios")
        self.geometry("800x600")

        # Grid principal: 2 columnas
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # columna izquierda
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.botones_usuarios = []

        # columna derecha
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.label_nombre = ctk.CTkLabel(self.right_frame, text="Nombre: ")
        self.label_nombre.pack(anchor="w", pady=5, padx=10)

        self.label_edad = ctk.CTkLabel(self.right_frame, text="Edad: ")
        self.label_edad.pack(anchor="w", pady=5, padx=10)

        self.label_genero = ctk.CTkLabel(self.right_frame, text="Género: ")
        self.label_genero.pack(anchor="w", pady=5, padx=10)

        self.label_avatar = ctk.CTkLabel(self.right_frame, text="Avatar: ")
        self.label_avatar.pack(anchor="w", pady=5, padx=10)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for btn in self.botones_usuarios:
            btn.destroy()
        self.botones_usuarios.clear()

        for u in usuarios:
            btn = ctk.CTkButton(self.scrollable_frame,text=u.nombre,command=lambda u=u: on_seleccionar_callback(u))
            btn.pack(fill="x", pady=2)
            self.botones_usuarios.append(btn)

    def mostrar_detalles_usuario(self, usuario):
        self.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.label_edad.configure(text=f"Edad: {usuario.edad}")
        self.label_genero.configure(text=f"Género: {usuario.genero}")
        self.label_avatar.configure(text=f"Avatar: {usuario.avatar}")
