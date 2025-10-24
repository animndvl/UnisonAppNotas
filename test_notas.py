import os
import pytest
from nota import ManejadorDeNotas

DB_TEST = "notasTestBD.db"

@pytest.fixture
def manejador():
    if os.path.exists(DB_TEST):
        os.remove(DB_TEST)

    manejador = ManejadorDeNotas(DB_TEST)

    yield manejador

    manejador.cerrar()
    if os.path.exists(DB_TEST):
        os.remove(DB_TEST)


def test_crear_nota(manejador):
    id_nota = manejador.crear_nota("Prueba", "Contenido de prueba")
    notas = manejador.leer_notas()
    assert len(notas) == 1
    assert notas[0].titulo == "Prueba"
    assert notas[0].contenido == "Contenido de prueba"


def test_leer_notas(manejador):
    manejador.crear_nota("Título A", "Texto A")
    manejador.crear_nota("Título B", "Texto B")
    notas = manejador.leer_notas()
    assert len(notas) == 2
    assert notas[0].titulo == "Título A"


def test_actualizar_nota(manejador):
    id_nota = manejador.crear_nota("Viejo", "Texto viejo")
    exito = manejador.actualizar_nota(id_nota, "Nuevo", "Texto nuevo")
    assert exito
    nota_actualizada = manejador.leer_notas()[0]
    assert nota_actualizada.titulo == "Nuevo"


def test_eliminar_nota(manejador):
    id_nota = manejador.crear_nota("Eliminar", "Borrar esto")
    exito = manejador.eliminar_nota(id_nota)
    assert exito
    notas = manejador.leer_notas()
    assert len(notas) == 0
