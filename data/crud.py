"""
Módulo de operaciones CRUD para la gestión de estudiantes.
Contiene funciones para crear , consultar , actualizar y eliminar
registros en la base de datos SQLite.
"""
import sqlite3

def crear(conn: sqlite3.Connection , nombre: str , correo: str , nota: float)-> None:
    """
    Inserta un nuevo estudiante en la base de datos.
    conn: conexión activa a la base de datos
    nombre: nombre del estudiante
    correo: correo electrónico del estudiante
    nota: nota del estudiante
    """
    conn.execute(
        "INSERT INTO estudiantes (nombre , correo , nota) VALUES (?, ?, ?)",
        (nombre , correo , nota)
    )
    conn.commit ()

def leer(conn: sqlite3.Connection) -> list:
    """
    Consulta todos los estudiantes registrados.
    conn: conexión activa a la base de datos
    retorna: lista de tuplas con los registros encontrados
    """
    cursor = conn.execute("SELECT * FROM estudiantes")
    return cursor.fetchall ()

def actualizar(conn: sqlite3.Connection , id_estudiante: int , nueva_nota:
float) -> None:
    """
    Actualiza la nota de un estudiante existente.
    conn: conexión activa a la base de datos
    id_estudiante: identificador del estudiante
    nueva_nota: nueva nota a asignar
    """
    conn.execute(
        "UPDATE estudiantes SET nota=? WHERE id=?",
        (nueva_nota , id_estudiante)
    )
    conn.commit ()

def eliminar(conn: sqlite3.Connection , id_estudiante: int) -> None:
    """
    Elimina un estudiante de la base de datos.
    conn: conexión activa a la base de datos
    id_estudiante: identificador del estudiante a eliminar
    """
    conn.execute(
        "DELETE FROM estudiantes WHERE id=?",
        (id_estudiante ,)
    )
    conn.commit ()