from data.crud import crear, leer, actualizar, eliminar

def crear_estudiante(conn, nombre, correo, nota):
    crear(conn, nombre, correo, nota)

def listar_estudiantes(conn):
    return leer(conn)

def actualizar_estudiante(conn, id_estudiante, nueva_nota):
    actualizar(conn, id_estudiante, nueva_nota)

def eliminar_estudiante(conn, id_estudiante):
    eliminar(conn, id_estudiante)