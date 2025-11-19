# app.py (Código Corregido)
import customtkinter as ctk
# Asegúrate de que esta importación sea correcta
from controller.app_controller import AppController

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Registro de Usuarios (CTk + MVC)")
    root.geometry("800x500")


    controller = AppController(root)

    root.mainloop()