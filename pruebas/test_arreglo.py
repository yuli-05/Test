import pytest
import arreglo as ar

array = [5,3,4,2,1]
diccionario = [
    {"nombre":"Julissa","edad":21},
    {"nombre":"Andy","edad":13},
    {"nombre":"Mar","edad":35}]

def test_arreglo():
    assert ar.ordenar(array) == [1,2,3,4,5]

def test_contar_mayores():
    assert ar.per_mayores(diccionario) == 2