import sqlite3

conexion = sqlite3.connect("libros.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS  categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria_id INTEGER,
    stock INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
    )
""")

conexion.commit()
conexion.close()

print("Basae creada correctamente")