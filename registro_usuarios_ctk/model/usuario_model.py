# model/usuario_model.py
import csv
from pathlib import Path

class Usuario:
    def __init__(self, nombre, edad, genero, avatar):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "genero": self.genero,
            "avatar": self.avatar,
        }

class GestorUsuarios:
    def __init__(self, data_path: Path):
        self._usuarios = []
        self.data_path = data_path
        self.cargar_csv()

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana", 22, "mujer", "avatar1.jpg"))
        self._usuarios.append(Usuario("Alberto", 33, "hombre", "avatar3.jpg"))
        self._usuarios.append(Usuario("Maria", 60, "mujer", "avatar2.jpg"))
        self._usuarios.append(Usuario("Elena", 25, "mujer", "avatar4.jpg"))



    def cargar_csv(self):
            self._usuarios.clear()
            try:
                with open(self.data_path, mode='r', newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)

                    for row in reader:
                        try:
                            usuario = Usuario(
                                row['nombre'],
                                int(row['edad']),
                                row['genero'],
                                row['avatar']
                            )
                            self._usuarios.append(usuario)
                        except ValueError:
                            pass
                        except KeyError:
                            pass

            except FileNotFoundError:
                self._cargar_datos_de_ejemplo()
            except Exception:
                self._cargar_datos_de_ejemplo()

    def guardar_csv(self):
        fieldnames = ['nombre', 'edad', 'genero', 'avatar']
        try:
            with open(self.data_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for usuario in self._usuarios:
                    writer.writerow(usuario.to_dict())
        except Exception as e:
            pass

    def listar(self):
        return self._usuarios

    def obtener_usuario(self, indice):
        if 0 <= indice < len(self._usuarios):
            return self._usuarios[indice]
        return None

    def agregar(self, usuario):
        self._usuarios.append(usuario)
        self.guardar_csv()

    def eliminar_por_objeto(self, usuario_obj):
        try:
            self._usuarios.remove(usuario_obj)
        except ValueError:
            print("No se pudo eliminar el usuario con nombre '{usuario_obj.nombre}' porque no se encontró el objeto en la lista.")