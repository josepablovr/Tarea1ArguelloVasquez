import math  # Se importa la libreria de operaciones matematicas
import random  # Se importa la libreria de numeros aleatorios
from funciones import multiple_op, verify_array_op  # Se importan las funciones


# Prueba unitaria de un caso de exito de la funcion multiple_op
def test_multiple_op():
    n = random.randint(0, 100000)  # Se genera un numero entero aleatorio

    # Se verifica el resultado correcto de la funcion
    assert multiple_op(n) == [math.prod([n, n]), pow(2, n), math.factorial(n)]


# Prueba unitaria de un caso de exito de la funcion verify_array_op
def test_verify_array_op():
    # Se crean los arrays que alojaran los resultados de la prueba
    arrayPrueba = [0, 0, 0, 0, 0]
    arrayAssert = [0, 0, 0, 0, 0]

    for i in range(0, 5):  # Se crea un ciclo para calcular 5 elementos
        n = random.randint(0, 100000)  # Se genera un numero aleatorio
        arrayPrueba[i] = n  # Se guarda el numero en el array de prueba
        # Se inserta el array con las operaciones en el array de verificacion
        arrayAssert[i] = [math.prod([n, n]), pow(2, n), math.factorial(n)]

    # Se evalua el array de prueba en la funcion y se verifica el resultado
    assert verify_array_op(arrayPrueba) == arrayAssert


# Prueba unitaria de un casonegativo de la funcion multiple_op
def test_multiple_op_neg_case():
    # Se evalua un argumento invalido y se verifica el codigo de error
    assert multiple_op("a") == 0xA0


# Prueba unitaria de un casonegativo de la funcion verify_array_op
def test_verify_array_op_neg_case():
    # Se evalua un argumento invalido y se verifica el codigo de error
    assert verify_array_op(["a", "b", "c", "d"]) == 0xA0
