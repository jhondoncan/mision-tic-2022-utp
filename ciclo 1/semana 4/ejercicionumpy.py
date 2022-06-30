import numpy
print("\x1Bc")
# Array de una dimension o unidimencionales o rango 1
""" m1D = numpy.array([1, 2, 3, 4, 5])
print(m1D) """


# Array de dos dimensiones o array de rango 2 2x3
""" m2D = numpy.array([[1, 2, 3], [4, 5, 6]])
print(m2D)
 """

# Array de dos dimensiones o array de rango 2 3x2 por listas
""" m2D = numpy.array([[1, 2], [3, 4], [5, 6]])
print(m2D)
 """

# Array de tres demensiones o de rango 3 3x3
""" m3D = numpy.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]])
print(m3D)
#print(m3D[0, 2])
print(m3D.shape)  # Cuenta el numero de filas y columnas """


""" print("Matriz con numeros aleatorios")
matrizAleatoria = numpy.random.rand(3, 3)
print(matrizAleatoria)

# Matriz con numeros ramdon con los numeros que uno indica
print("Matriz aleatrrios con rango")
matrizAleatoria = numpy.random.randint(1, 10, size=(3, 3))
print(matrizAleatoria)


# MAtriz de numeros aleatorios pero sin cedimales
print("Con Round y numeros aleatorios")
matrizR = numpy.round(numpy.random.rand(3, 3))
print(matrizR)

print("Matriz de ceros")
matrizZeros = numpy.zeros((3, 3))
print(matrizZeros)

print("Matriz de unos")
matrizUnos = numpy.ones((3, 3))
print(matrizUnos)

# MAtriz Contstante
print("Matriz Constante")
matrizConstante = numpy.full((3, 3), 14)
print(matrizConstante)


print("Matriz de Identidad")  # Siempre son cuadradas 3x3 4x4
matrizIdentidad = numpy.eye(3)
print(matrizIdentidad)
 """


# Revanada de matrices
""" a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a[0:2, 1:3])


print('Invertir filas')
# Matriz invertida

print(a)
print(numpy.flip(a))
 """

# Indexacion de matrices booleanas
""" a = numpy.array([[1, 2], [3, 4], [5, 6]])
print(a)
# Imprime si es falso o verdadera la condicion dada
boleano = (a > 3)
print(boleano)
print("Imprime una lista con los valores verdaderos")
print(a[boleano])

print("Todo en una sola linea")
print(a[a > 3])
 """

# Tipos de datos
# Cambiar tipo cee datos
""" x = numpy.array([1, 2], dtype=numpy.int64)
print(x)
print(x.dtype)
 """

# CALCULADORA DE MATRICES
""" x = numpy.array([[1, 2], [3, 4]])
y = numpy.array([[5, 6], [7, 8]])
print("Suma de matrices forma 1")
print(x+y)
print("Suma de matrices forma 2")
print(numpy.add(x, y))
print("Resta de matrices forma 1")
print(x-y)
print("Resta de matrices forma 2")
print(numpy.subtract(x, y))
print("Multiplicacion de matrices forma 1")
print(x*y)
print("Multiplicacion de matrices forma 2")
print(numpy.multiply(x, y))
print("Division de elementos de matrices forma 1")
print(x/y)
print("Division de elementos de matrices forma 2")
print(numpy.divide(x, y))
print(numpy.round(x/y), 1)
print("Multiplicacion de matrices ")
print(numpy.dot(x, y))
print("Multiplicacion de matrices forma 2")
print(numpy.matmul(x, y))
print("Transpuesta de matrices")
print(numpy.transpose(x)) """


####
print("Broadcasting de matrices")
print("Sumar un vector a una atriz")
x = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(x)
vector = numpy.array([1, 8, 2])
print(vector)
y = numpy.empty_like(x)  # Crea una matriz del mismo tamaño dela matriz x
print(y)
# Recorrer matriz
for i in range(4):
    for j in range(3):
        y[i, j] = x[i, j] + vector[j]
print(y)
