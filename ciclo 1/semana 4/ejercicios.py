print("\x1Bc")
# Conversion entre contenerdores
# convercion de cadenas

# De cadenas a listas
""" cadena = 'aeiou'
lista = list(cadena)
print(lista)
cadena2 = "Jhon Arlem Silva Andrade" """
# Cada vez que encueentra un espacio en la cadena lo convierte en una lista
""" lista2 = cadena2.split()
print(lista2)
 """


# DE CADENAS A TUPLAS
""" cadena = 'aeiou'
cadenaTupla = tuple(cadena)
print(cadenaTupla)
 """

# DE CADENA A CONJUNTO
""" cadena = 'aaieiou'
cadenaConjunto = set(cadena)
print(cadenaConjunto)
 """

# CONVERSION DE LISTAS

# DE LISTAS A CADENA
""" lista = ['a', 'b', 'c', 'd', 'e']
cadena = ''.join(lista)
print(cadena) """

# DE LISTAS A TUPLAS
""" lista2 = ['a', 'b', 'c', 'd', 'e']
tupla = tuple(lista2)
print(tupla) """

# DE LISTAS A CONJUNTO
""" lista3 = ['a', 'b', 'c', 'd', 'e']
conjunto = set(lista3)
print(conjunto) """


# CONVERSION DE TUPLAS

# DE TUPLAS A CADENA
""" tupla = ('a', 'v', 'i', 'o', 'n')
cadena = ''.join(tupla)
print(cadena) """

# DE TUPLAS A LISTAS
""" tupla2 = ('a', 'v', 'i', 'o', 'n')
lista = list(tupla2)
print(lista) """

# DE TUPLAS A CONJUNTO
""" tupla3 = ('a', 'v', 'i', 'o', 'n')
conjunto = set(tupla3)
print(conjunto)
 """

# CONVERSION DE CONJUNTOS

# DE CONJUNTOS A CADENA
""" conjunto = {'a', 'v', 'i', 'o', 'n'}
cadena = ''.join(conjunto)
print(cadena) """

# DE CONJUNTOS A TUPLAS
""" conjunto2 = {'a', 'v', 'i', 'o', 'n'}
tupla = tuple(conjunto2)
print(tupla) """

# DE CONJUNTOS A LISTAS
""" conjunto3 = {'a', 'v', 'i', 'o', 'n'}
lista = list(conjunto3)
print(lista) """


# CONVERCION A DICCIONARIOS

# DE CADENA A DICCIONARIO
""" cadena = "hola"
diccionario = dict(zip(cadena, cadena))
print(diccionario)


rango = range(len(cadena))
diccionario2 = dict(zip(rango, cadena))
print(diccionario2)
 """

# DE LISTA A DICCIONARIO
""" lista = ['h', 'o', 'l', 'a']
diccionario3 = dict(zip(lista, lista))
print(diccionario3) """


# DE TUPLA A DICCIONARIO
""" tupla = ('h', 'o', 'l', 'a')
diccionario4 = dict(zip(tupla, tupla))
print(diccionario4) """


# DE CONJUNTO A DICCIONARIO
""" conjunto = {'h', 'o', 'l', 'a'}
diccionario5 = dict(zip(conjunto, conjunto))
print(diccionario5)
 """


# CONVERCION DESDE DICCIONARIOS

# DE DICCIONARIO A CADENA
""" dciccionario = {'0': 'a', '1': 'e', '2': 'i', '3': 'o', '4': 'u'}
cadena = ''.join(dciccionario.values())
print(cadena) """


# DE DICCIONARIO A LISTA
""" diccionario = {'0': 'a', '1': 'e', '2': 'i', '3': 'o', '4': 'u'}
lista = list(diccionario.values())
print(lista) """


# DE DICCIONARIO A TUPLA
""" diccionario = {'0': 'a', '1': 'e', '2': 'i', '3': 'o', '4': 'u'}
tupla = tuple(diccionario.values())
print(tupla)
 """

# DE DICCIONARIO A CONJUNTO
""" diccionario = {'0': 'a', '1': 'e', '2': 'i', '3': 'o', '4': 'u'}
conjunto = set(diccionario.values())
print(conjunto)
 """


############### PROGRAMACION IMPERACTIVA ########

# Programacion imperactiva
""" def suma(v1, v2):
    return v1+v2


print('La suma de las varaiables es: ', suma(10, 20))


# Programacion funcional
# Envoltura de funciones

def operacion(funcion, v1, v2):
    return funcion(v1, v2)


funcion_suma = suma
resultado = operacion(funcion_suma, 10, 20)
print('Funcion suma: ', funcion_suma)
print('Funcion suma: ', resultado)
 """

# Ejemplo 2 Envoltura de funciones
""" 

def crear_funcion(operador):
    if operador == '+':
        def suma(v1, v2):
            return v1+v2
        return suma
    elif operador == '-':
        def resta(v1, v2):
            return v1-v2
        return resta
    elif operador == '*':
        def multiplicacion(v1, v2):
            return v1*v2
        return multiplicacion
    elif operador == '/':
        def division(v1, v2):
            return v1/v2
        return division


def operacion(funcion, v1, v2):
    return funcion(v1, v2)


funcion_suma = crear_funcion('+')
funcion_resta = crear_funcion('-')
funcion_multiplicacion = crear_funcion('*')
funcion_division = crear_funcion('/')
resultado = operacion(funcion_suma, 10, 20)
resultado2 = operacion(funcion_resta, 10, 20)
resultado3 = operacion(funcion_multiplicacion, 10, 20)
resultado4 = operacion(funcion_division, 10, 20)
print('Funcion suma: ', funcion_suma)
print('Funcion resta: ', funcion_resta)
print('Funcion multiplicacion: ', funcion_multiplicacion)
print('Funcion division: ', funcion_division)


 """

# FUNCIONES ANONIMAS
# Ejercicio 3 Funciones Lambda

""" print("\x1Bc")


def funcionlambda(v1, v2): return v1+v2


def resultado(v1, v2): return v1+v2


def resultado(v1, v2): return v1+v2


print('La suma es: ', resultado(10, 20))
print(funcionlambda(10, 20))


def resultado(v1, v2): return v1+v2
 """


# Ejercicio 4 Envoltura de funciones anonimas
""" def suma(v1, v2): return v1+v2
def operacion(operacion, v1, v2): return operacion(v1, v2)


print(operacion(suma, 10, 20))
 """


# FUNCION MAP
# Funciona con una funcion y luego el objeto iterable
# Cuadrados de una lista

""" def cuadrado(elemento): return elemento**2


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(map(cuadrado, lista))
print(resultado)

resultado2 = list(map(lambda elemento: elemento**2, lista))
print(resultado2)
 """


# MAP PARA DEVOLVER LA POTENCIA
""" print("\x1Bc")
bases = [2, 3, 4]
exponentes = [3, 2, 4]
potencia = list(map(pow, bases, exponentes))

print("Lista de bases: ", bases)
print("Lista de exponentes: ", exponentes)
print("Lista de potencias: ", potencia)
 """


# FUNCION FILTER
# Enviamos la funcion a aplicar y el objeto iterable

""" tupla = (5, 2, 10, 15, 20, 1)


def mayores(elemento): return elemento > 5


resultado = list(filter(mayores, tupla))
print("La tupla es: ", tupla)
print("Los numeros mayores a 5 son: ", resultado)
print("La cantidad de numeros mayores son: ", len(resultado))


resultadoLambda = tuple(filter(lambda elemento: elemento > 5, tupla))
print("Resutado con lambda: ", resultadoLambda)
print("La cantidad de numeros con lambda mayores son: ", len(resultadoLambda))
resultadoLambda2 = len(tuple(filter(lambda elemento: elemento > 5, tupla)))
print("Resutado con lambda: ", resultadoLambda2)
 """


# Funcion filter Numeros pares
""" pares = []
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in items:
    if i % 2 == 0:
        pares.append(i)
print(f'Los numeros pares de la lista: {items} son: {pares}')


# Programacion funcional
pares = list(filter(lambda elemento: elemento % 2 == 0, items))
print(f'Los numeros pares de la lista: {items} son: {pares} con lambda')
 """


# FUNCION REDUCE
# 1 LA FUNCION A APLICAR 2 EL OBJETO ITERABLE

# sUMATORIA DE LOS ELEMENTOS DE UNA LISTA
""" from functools import reduce
print("\x1Bc")
lista = [1, 2, 3, 4, 5]

# forma imperactiva
suma = 0
for i in lista:
    suma += i
print(f'La suma de los numeros de la lista {lista} es: {suma}')

# forma funcional
suma = reduce(lambda x, y: x+y, lista)
print(f'La suma de los numeros de la lista {lista} es: {suma}')
 """

# FUNCION ZIP
# funcion para reorganizar los elementos de una lista

# Unir Listas
"""
nombres = ['Juan', 'Pedro', 'Maria', 'Ana']
apellidos = ['Perez', 'Gomez', 'Lopez', 'Garcia']
nombreApellido = list(zip(nombres, apellidos))
print(nombreApellido)
 """


# DECICIONES GENERALIZADAS
""" 
informacion = [int(input('Digite un numero: ')), input(
    'Digite numeros separados por espacio: ').split(' ')]
print(informacion)
print('True' if all(
    list(map(lambda x: x > 0, list(map(int, informacion[1]))))) and any(list(map(lambda x: x[0] == x[1] or x[0] == '5', list(zip(informacion[1], list(map(lambda x: x[-1:(len(x)+1)*-1:-1], informacion[1]))))))) else 'False')
 """


# isupper() Me devuelve si la cadena esta en mayuscula
# islower() Me devuelve si la cadena esta en minuscula
# isalpha() Me devuelve si la cadena esta formada por letras
# isdigit() Me devuelve si la cadena esta formada por numeros
# isalnum() Me devuelve si la cadena esta formada por letras y numeros
# isdecimal() Me devuelve si la cadena esta formada por numeros 53800

# Ejercicio all y any

""" uids = ['B1CD102354', 'B1CDEF2354']

for uid in uids:
    condicion = []
    # POR LO MENOS DOS LETRAS MAYUSCULAS
    condicion.append(len(list(filter(lambda x: x.isupper(), list(uid)))) >= 2)
    # POR LO MENOS TRES NUMEROS
    condicion.append(len(list(filter(lambda x: x.isdigit(), list(uid)))) >= 3)
    # SOLO DIGITOS ALFANUMERICOS
    condicion.append(
        len(list(filter(lambda x: not(x.isalnum()), list(uid)))) == 0)
    # SIN NUMEROS REPETIDOS
    condicion.append(len(uid) == len(set(uid)))
    condicion.append(len(uid) == 10)
    # print(condicion)


if all(condicion):
    print(f'{uid} es un UID valido')
else:
    print(f'{uid} no es un UID valido')
    
print(f'{uid} es un UID valido') if all(
    condicion) else print(f'{uid} no es un UID valido')
 """
