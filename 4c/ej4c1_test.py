"""
Enunciado:
Desarrolla un test para la función implementada calculate_rectangle_area, la función recibe dos parámetros ancho y
alto, y devuelve el área del rectángulo, calculada como ancho * alto. utilizando el enfoque de Desarrollo Guiado
por Pruebas (TDD).

Instrucciones de Implementación:
- Realizar los test considerando los distintos casos de prueba descritos a continuación.
- Ejecutar las pruebas y verificar que la implementación sea correcta.

Casos de Prueba:
    Prueba con valores enteros positivos para ancho y alto.
    Prueba con ancho/alto negativo.
    Prueba con ancho/alto no numérico.

Ejemplo:
    area = calcular_area_rectangulo(5, a)
    print("Área del rectángulo:", area)

"""

import pytest
from ej4c1 import calculate_rectangle_area

def test_calculate_rectangle_area(): 
    # Prueba con valores enteros positivos para ancho y alto.   
    # Write here your code

    # Change the following line
    assert calculate_rectangle_area(5, 10) == 50
    
def test_value_error_calculate_rectangle_area():
    # Prueba con ancho/alto negativo.
    # Write here your code
    
    # Change the following line
    with pytest.raises(ValueError, match="Width and height must be non-negative."):
        calculate_rectangle_area(-5, 10)
    

def test_type_error_calculate_rectangle_area():
    # Prueba con ancho/alto no numérico.
    # Write here your code
    
    # Change the following line
    with pytest.raises(TypeError, match="Width and height must be numbers."):
        calculate_rectangle_area("five", 10)