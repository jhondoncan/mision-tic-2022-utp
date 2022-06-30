# Ejercicio 1 VARIABLE DE INCREMENTO Y DECREMENTO

# Incrementando una variable
""" i = 1
i += 1
print("El valor de i es:", i)

# Decrementando una variable
i -= 1
print("El valor de i es:", i)
 """

# Ejercicio 2 CICLO WHILE

""" n = 5
while n > 0:
    print(n)
    n -= 1
 """

# WHILE CON ELSE

""" promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota del estudiante (-1 Para salir): "
grado = float(input(mensaje))
while grado != -1:
    total = total + grado
    contar += 1
    grado = float(input(mensaje))
else:
    promedio = total / contar
    print("El promedio de notas es:", round(promedio, 1))
    if promedio >= 3:
        print("El alumno aprobó")
    else:
        print("El alumno reprobó")
 """

# WHILE CON BREAK

""" variable = 10
while variable > 0:
    variable -= 1
    print("Valor actual de la variable:", variable)
    if variable == 5:
        break
 """


# WHILE CON CONTINUE
""" variable = 10
while variable > 0:
    variable -= 1
    if variable == 5:
        continue  # Salta el siguiente ciclo y continua con el siguiente
    print("Valor actual de la variable:", variable)  # No imprime el 5 """


# WHILE CICLO FOR (Se utiliza para recorer datos iterables como listas, tuplas, etc.)
""" rango = range(0, 11, 2)  # Se crea un rango de 0 a 10 con saltos de 2
for i in rango:
    print(i) """


# Imprimir numeros impares de 0 a 10 con ciclo for
""" rango = range(1, 11, 2)  # Se crea un rango de 0 a 10 con saltos de 2
for i in rango:
    print(i) """

# Imprimir la formula de FIBONACCI
""" n = int(input("Introduzca el numero de elementos de la serie: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b """


# LISTAS
# Diccionarios {key:value}
# Listas []

""" lista = [1, 2, 3, 4, 5, 3, 2, 2, 5]
listaString = ['a', 'b', 'c', 'd', 'e']
listaFloat = [1.2, 5.4, 3.5, 7.8]
listaLista = [1, 2, [2, 5], [3, 6], 2, "Doncan"]
 """

"""
print(listaLista)
print(listaString)
print(listaFloat)
print(listaLista)
# Imprimiendo el valor 6 de la lista
print(listaLista[3][1])
# Imprimiendo los valores de la lista desde la posicion 1 hasta la posicion 4
print(listaLista[1:5])
# Imprimiendo el ultimo valor de la lista (De derecha a izquierda)
print(listaLista[-1])
# Imprimiendo la lista de dos en dos
print(listaLista[0:1:2])
print(len(listaLista)) """


# METODOS
# METODO APPEND
""" print(listaLista)
listaLista.append("Hola mundo")  # Agrega un elemento al final de la lista
print(listaLista)
 """

# METODO COUNT
# Cuenta la cantidad de elementos de la lista
""" print(lista.count(2)) """


# METODO EXTEND
""" listaAdicional = [1, 2, 4, "Jhon"]
lista.extend(listaAdicional)  # Extiende la lista con otra lista
print(lista) """


# METODO INDEX
# Busca el indice de un elemento en la lista
""" print(f'Indice del Doncan: {listaLista.index("Doncan")}') """


# METODO INSERT
# Inserta un elemento en una posicion especifica
""" listaAdicional.insert(4, "Doncan")
print(listaAdicional) """


# METODO POP
# Elimina el ultimo elemento de la lista
""" listaAdicional.pop()
print(listaAdicional)
 """

# METODO REMOVE
# Elimina el primer elemento de la lista que coincida con el valor especificado
""" print(listaLista)
listaLista.remove(2)
print(listaLista)
 """

# METODO REVERSE
# Invierte el orden de los elementos de la lista
""" print(listaAdicional)
listaAdicional.reverse()
print(listaAdicional) """


# METODO SORT
# Ordena los elementos de la lista de menor a mayor
""" listaNumeros = [2, 10, 7, 9, 3, 8, 6, 4, 1, 5]
listaNumeros.sort()
print(listaNumeros) """


# METODO REVERSE
# Ordena los elementos de la lista de mayor a menor
""" listaNumeros.reverse()
print(listaNumeros) """


# LISTAS PARALELAS
# Ejercicio que guarda los nombres y las edades en listas diferentes e indica quienes son mayores de edad
"""
listaNombres = []
listaEdades = []
for i in range(5):
    nombre = input("Introduzca el nombre: ")
    listaNombres.append(nombre)
    edad = int(input("Introduzca la edad: "))
    listaEdades.append(edad)

for i in range(len(listaNombres)):
    if listaEdades[i] >= 18:
        print(listaNombres[i], "es mayor de edad")
 """

# LISTA COMPUESTAS
#
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# Diferentes formas de imprimir listas
# Imprimir lista
""" print(lista) """
# Imprimir una sublista
""" print(lista[1]) """
# Imprimir un elemento de la sublista
""" print(lista[1][2]) """

# Imprimiendo la lista contenida
""" print('La lista contenida en la posision [2] es:')
longitudLista = len(lista[2])
rango = range(0, longitudLista)
for i in rango:
    print(lista[2][i]) """

# Impriminedo toda la longitud de la lista
""" longitudListaP = len(lista)
rango = range(0, longitudListaP)
for i in rango:
    for j in range(0, len(lista[i])):
        print(lista[i][j])
 """

# Ejercicio que pide nombre de padre, madre cantidad de hijos nombre de los hijos e imprime el nombre del padre con la cantidad de hijos
""" padres = []
hijos = []
for i in range(3):
    nombrePadre = input("Introduzca el nombre del padre: ")
    nombreMadre = input("Introduzca el nombre de la madre: ")
    padres.append([nombrePadre, nombreMadre])
    cantidadHijos = int(input("Introduzca la cantidad de hijos: "))
    hijos.append([])  # Se debe indicar que se va a guardar una lista vacia
    for j in range(cantidadHijos):
        nombreHijo = input("Introduzca el nombre del hijo: ")
        hijos[i].append(nombreHijo)
# Imprimir el nombre del padre de la madre y de los hijos
for i in range(len(padres)):
    print(f'Nombre del padre: {padres[i][0]}')
    print(f'Nombre de la madre:{padres[i][1]}')
    for j in range(len(hijos[i])):
        print(f'Nombre del hijo: {hijos[i][j]}')
    print("------------")
# Contar los hijos que tiene cada padre
for i in range(len(padres)):
    print(f'{padres[i][0]} tiene {len(hijos[i])} hijo(s)') """


# TUPLAS
# Las tuplas son inmutables no se pueden cambiar en tiempo de ejecucion
""" tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuplaVocales = "a", "e", "i", "o", "u"  # Se pueden poner tuplas sin los ()
# Se pone la coma al final para definiarla como tupla y no str o tambien (),
TuplaElmento = "a",
print(tuplaVocales[1])  # Imprimir en posicion especifica
print(tuplaVocales[0:4])  # Imprimir tupla en rango """

# Convierte el contenido en un elemento en tupla
""" txt = "Python es mas facil de lo que pensaba"
palabra = txt.split()
print(palabra)
 """

# CONJUNTOS
# No se pueden poner objetos mutables como listas o diccionarios ni conjuntos dentro de conjuntos
# Los conjuntos son una coleccion de elementos que no se repiten
""" conjunto = {10, 7, 9, 8, 6, 5, 3, 4, 1, 2}
print(conjunto)

# Para crear un conjunto vacio se debe declarar con la variable set()
conjuntoA = set()
print(type(conjuntoA))
# Se puede definir un conjunto con una lista
conjuntoA = set([1, 2, 10, 4, 9, 6, 5, 3, 8, 9, 10, 7])
print(conjuntoA)

# Para acceder a los conjuntos se utiliza un for
for i in conjuntoA:
    print(i)

# MEtodos de los conjuntos
# add() agrega un elemento al conjunto
conjuntoA.add(11)
print(conjuntoA)

# remove() elimina un elemento del conjunto
conjuntoA.remove(11)
print(conjuntoA)

# clear() elimina todos los elementos del conjunto
conjuntoA.clear()
print(conjuntoA)

# intersection() devuelve un conjunto con los elementos que estan en ambos conjuntos
conjuntoA = set([1, 2, 10, 4, 9, 6, 5, 3, 8, 9, 10, 7])
conjuntoB = set([2,  4, 6,  8,  10])
print(conjuntoA.intersection(conjuntoB))

# diferrence() devuelve un conjunto con los elementos que estan en el conjunto A pero no en el conjunto B
print(conjuntoA.difference(conjuntoB)) """


# CONTENEORES DE DATOS O ARREGLOS O COLECCIONES
# Listas (Arreglos) - Listas mutables - Se pueden cambiar los elementos en tiempo de ejecucionde pendiendo si son mutables o inmutables

""" diccionarioEstudiantes = {
    'IES101023': {
        'nombre': 'Juan',
        'apellido': 'Perez',
        'acudiente': ['Maria', 'Jose'],
        'promedio': 5.0
    },
    'IES101024': {
        'nombre': 'Pedro',
        'apellido': 'Pardo',
        'acudiente': ['Doncan', 'Ana'],
        'promedio': 4.0
    },
    'IES101025': {
        'nombre': 'Andres',
        'apellido': 'Oso',
        'acudiente': ['Esposa'],
        'promedio': 4.3
    }
}

print(diccionarioEstudiantes['IES101023'])
print("-----------------")
print(diccionarioEstudiantes['IES101023']['nombre'])
print("-----------------")
print(diccionarioEstudiantes['IES101023']['acudiente'][0])

print("-----------------")
# Recorrer e imprimir los valores de un contenedor
for claves, valores in diccionarioEstudiantes.items():
    print(claves, valores)
    print(f'Codigo del estudiante: {claves}')
    print(f'Nombre del estudiante: {valores["nombre"]}')
print("-----------------")
# Recorrer e imprimir por claves
for claves in diccionarioEstudiantes.keys():

    print(f'Clave del estudiante: {claves}')
print("-----------------")
# Recorrer e imprimir por valores
for claves in diccionarioEstudiantes.values():

    print(f'La informacion del estudiante: {claves}')
print("-----------------")

 """
