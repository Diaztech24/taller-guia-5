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