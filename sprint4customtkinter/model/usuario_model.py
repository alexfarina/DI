class Usuario:
    def __init__(self, nombre, edad, genero, avatar):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

class GestorUsuarios:
    def __init__(self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana", 22, "mujer", "avatar1.png"))
        self._usuarios.append(Usuario("Maria", 60, "mujer", "avatar2.png"))
        self._usuarios.append(Usuario("Alberto", 33, "hombre", "avatar3.png"))
        self._usuarios.append(Usuario("Jose", 27, "hombre", "avatar4.png"))

    def listar(self):
        return self._usuarios
