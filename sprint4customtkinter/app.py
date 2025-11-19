# app.py
from controller.app_controller import AppController

def main():
    app_controller = AppController()
    app_controller.vista.mainloop()  # Ejecuta la app

if __name__ == "__main__":
    main()
