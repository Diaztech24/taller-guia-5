"""
Módulo principal del sistema de gestión de estudiantes.
Permite ejecutar un sistema CRUD sobre una base de datos SQLite
mediante un menú en consola.
"""
from database.conexion import conectar , crear_tabla
from data.crud import crear , leer , actualizar , eliminar

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
