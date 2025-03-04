import pytest
from app import calcular_promedio, calcular_desviacion_estandar

def test_calcular_promedio():
    datos = [10, 20, 30, 40, 50]
    assert calcular_promedio(datos) == 30

def test_calcular_desviacion_estandar():
    datos = [10, 20, 30, 40, 50]
    assert round(calcular_desviacion_estandar(datos), 2) == 14.14

