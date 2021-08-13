import math  # Se importa la libreria de operaciones matematicas
ERROR_BAD_ARGUMENTS = 0xA0  # Se establece el codigo de error


# Descripcion: funcion que realiza 3 operaciones distintas
# Entrada: un numero entero
# Salida: un arreglo con los 3 resultados
# Restricciones: la entrada debe ser un entero positivo
def multiple_op(X):
    resultado = [0, 0, 0]  # Se define un arreglo de 3 elementos

    # Se verifica que el argumento sea un entero positivo
    if type(X) == int and X >= 0:
        # Se añaden las operaciones al arreglo de salida
        resultado[0] = X * X
        resultado[1] = 2**X
        resultado[2] = math.factorial(X)
        return resultado  # Se retorna el arreglo resultante

    # En caso de que el argumento no sea un entero positivo:
    else:
        # Se notifica al usuario del error
        print("El dato ingresado no es valido")
        # Se retorna el codigo de error correspondiente
        return ERROR_BAD_ARGUMENTS


# Descripcion: funcion que realiza 3 operaciones distintas a un array
# Entrada: un array con 3 numeros
# Salida: un array de arrays con los 3 resultados
# Restricciones: la entrada debe ser un array de enteros positivos
def verify_array_op(arrayN):
    resultado = []  # Se inicializa el array
    if isinstance(arrayN, list):  # Se verifica que la entrada sea un array
        for n in arrayN:  # Se hace un ciclo para analizar cada elemento
            # Se verifica que el elemento sea un entero positivo
            if type(n) == int and n >= 0:
                # Se evalua el elemento en multiple_op y se añade al array
                resultado.append(multiple_op(n))

            # En caso de que el elemento no sea un entero positivo:
            else:
                # Se notifica al usuario del error:
                print("El array ingresado no es valido")
                # Se establece el codigo de error como resultado
                resultado = ERROR_BAD_ARGUMENTS
                break

    # En caso de que la entrada no sea un array:
    else:
        # Se notifica al usuario del error:
        print("No se ha ingresado un array")
        # Se establece el codigo de error como resultado
        resultado = ERROR_BAD_ARGUMENTS

    return resultado  # Se retorna el array resultante o el codigo de error
