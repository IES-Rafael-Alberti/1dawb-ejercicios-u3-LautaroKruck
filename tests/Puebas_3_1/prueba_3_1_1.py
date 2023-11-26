import pytest
from src.practica_3_1.ej3_1_1 import dar_lista

def test_dar_lista():
    assert dar_lista(["Matemáticas", "Física", "Química", "Historia", "Lengua"]) == "Matemáticas-Física-Química-Historia-Lengua"

    assert dar_lista([]) == ""

    assert dar_lista(["Matemáticas"]) == "Matemáticas"