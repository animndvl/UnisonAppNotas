import sqlite3
import os

class Nota:
    def __init__(self, id, titulo, contenido):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido

    def __repr__(self):
        return f"Nota(id={self.id}, titulo={self.titulo}, contenido={self.contenido})"

class ManejadorDeNotas:
    def __init__(self, db_name="notasBD.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._crear_tabla()

    def _crear_tabla(self):
        """Crea la tabla 'notas' si no existe"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                contenido TEXT NOT NULL
            )
        """)
        self.conn.commit()

#Crear nota
    def crear_nota(self, titulo, contenido):
        self.cursor.execute(
            "INSERT INTO notas (titulo, contenido) VALUES (?, ?)",
            (titulo, contenido)
        )
        self.conn.commit()
        return self.cursor.lastrowid

#Leer notas
    def leer_notas(self):
        self.cursor.execute("SELECT id, titulo, contenido FROM notas")
        filas = self.cursor.fetchall()
        return [Nota(id, titulo, contenido) for id, titulo, contenido in filas]

#Actualizar nota
    def actualizar_nota(self, id, nuevo_titulo, nuevo_contenido):
        self.cursor.execute(
            "UPDATE notas SET titulo = ?, contenido = ? WHERE id = ?",
            (nuevo_titulo, nuevo_contenido, id)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

#Eliminar nota
    def eliminar_nota(self, id):
        self.cursor.execute(
            "DELETE FROM notas WHERE id = ?",
            (id,)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

#Cerrar conexion
    def cerrar(self):
        self.conn.close()
