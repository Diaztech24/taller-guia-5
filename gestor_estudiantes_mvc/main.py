import sqlite3
def conectar ():
    return sqlite3.connect("estudiantes.db")

def crear_tabla(conn):
    conn.execute("""CREATE TABLE IF NOT EXISTS estudiantes(
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        nombre TEXT ,
        correo TEXT ,
        nota REAL
    )
    """)
    conn.commit ()

"""
Módulo de operaciones CRUD para la gestión de estudiantes.
Contiene funciones para crear , consultar , actualizar y eliminar
registros en la base de datos SQLite.
"""
import sqlite3

def crear(conn: sqlite3.Connection , nombre: str , correo: str , nota: float)
-> None:
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

"""
Módulo principal del sistema de gestión de estudiantes.
Permite ejecutar un sistema CRUD sobre una base de datos SQLite
mediante un menú en consola.
"""
from database import conectar , crear_tabla
from crud import crear , leer , actualizar , eliminar

def menu() -> None:
    """
    Muestra el menú principal del sistema.
    """

print("\n--- SISTEMA DE ESTUDIANTES ---")
print("1. Crear estudiante")
print("2. Listar estudiantes")
print("3. Actualizar nota")
print("4. Eliminar estudiante")
print("5. Salir")

def main() -> None:
    """
    Ejecuta el flujo principal del programa.
    Establece la conexión con la base de datos , crea la tabla si no existe
    y gestiona la interacción con el usuario a través de un menú.
    """
    conn = conectar ()
    crear_tabla(conn)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            nota = float(input("Nota: "))
            crear(conn , nombre , correo , nota)

        elif opcion == "2":
            estudiantes = leer(conn)
            for estudiante in estudiantes:
                print(estudiante)

        elif opcion == "3":
            id_estudiante = int(input("ID: "))
            nueva_nota = float(input("Nueva nota: "))
            actualizar(conn , id_estudiante , nueva_nota)

        elif opcion == "4":
            id_estudiante = int(input("ID: "))
            eliminar(conn , id_estudiante)

        elif opcion == "5":
            break

        else:
            print("Opción no válida.")

    conn.close ()

if __name__ == "__main__":
    main()
