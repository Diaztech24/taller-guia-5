class Estudiante:
    def __init__(self, id: int, nombre: str, correo: str, nota: float):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.nota = nota

    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.correo} | {self.nota}"