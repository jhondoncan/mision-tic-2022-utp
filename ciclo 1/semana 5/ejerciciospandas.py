
import pandas
import numpy
print("\x1Bc")
# Indice impliicito y explicito
""" print("\nIndice implicito y explicito")


serie = pandas.Series(['Habilidades', 'Ingles', 'Programacion'], index=[
                      '001H', '002I', '003P'])  # Los indices son inmutables
print(serie)

# Mostrar elementos
print("\nMostrar elementos")
print(serie[0])
print(serie['001H'])
print('Tipo de dato:\n', type(serie['001H']))
print('Index:\n', serie.index)
print('Valores:\n', serie.values)

# Mostrar Rango
print("\nMostrar Rango")
print(serie[0:3])
print(serie['001H':'003P'])

 """
# Mostrar con metodos loc y iloc
""" serieD = pandas.Series(['Habilidades', 'Programacion', 'Programacion'], index=[
    '001H', '002P', '003P']) """  # Los indices son inmutables

""" print("\nMostrar con metodos loc y iloc")
print(serieD.loc['003P'])  # Busqueda por '003p'
print(serieD.iloc[0])  # Busqueda por indice explicito
print(serieD.loc['001H':'003P'])  # Busqueda por rango
print(serieD.iloc[0:3])  # Busqueda por rango explicito
print('Buscar de forma aleatoria')
print(serieD.sample(1, random_state=0))
 """

# ELIMINAR ELEMENTOS
""" serie = pandas.Series(['Habilidades', 'Ingles', 'Programacion'], index=[
                      '001H', '002I', '003P'])  # Los indices son inmutables
print("nELIMINAR ELEMENTOS")
print(serie)
print(serie.pop([0]))
print(serie)
# Eliminar por el indice
print(serie.drop('002I'))
print(serie.drop(serie.index[0]))   # Eliminar por indice explicito
print(serie)

 """

""" serie = pandas.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(serie)
print(serie > 5)

print('Imprimir una lista')
print(serie[serie > 5])
serie.index.name = 'Numero'
print(serie)
serie.name = 'Nombre Serie'
print(serie)

print('Atributo Axes')
print(serie.axes)

print('Dimension')
print(serie.shape)

print('Editar serie')
serie[0] = -1
print(serie)

print('Editar srie por rango')
serie[0:10] = -1
print(serie)

print('Eliminar por pocisiones')
print(serie.drop(serie.index[0, 1, 2, 3, 4]))  # Eliminar por indices
print('Eliminar por rangos')
print(serie.drop(serie.index[10:15]))  # Eliminar por rangos
 """

# Metodo Where
""" serie = pandas.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(serie)
print('Imprimir numeros pares con where')
resultado = serie.where(serie % 2 == 0)
print(resultado)
# Tamaño de la serie
print('Tamaño de la serie')
print(serie.shape)
print(len(serie))

a = []
for i in range(resultado.shape[0]):
    if not(pandas.isna(resultado[i])):
        a.append(resultado[i])
print(a)

a2 = []
for i in range(len(resultado)):
    if not(pandas.isna(resultado[i])):
        a2.append(resultado[i])
print(a2)
 """

# DATAFRAME
# Conjunto de datos que se pueden ordenar, filtrar y agrupar como una tabla
# Se pueden agregar columnas y filas
# Se pueden eliminar columnas y filas


# Con diccionarios
""" print('Reporte ventas de frutas:\n')
ventasFrutas = {'Manzanas': [3, 2, 0, 1, 5],
                'Naranjas': [0, 3, 7, 2, 2], 'Peras': [5, 2, 3, 0, 7]}
frutasVendidas = pandas.DataFrame(
    ventasFrutas, index=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'])
print(frutasVendidas)
print('Atributo values')
print(frutasVendidas.values)
print('Atributo shape -- Trae la diemsion')
print(frutasVendidas.shape)
 """

# DataFrame con arrays
""" x = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
numeros = pandas.DataFrame(x)
print(numeros)
 """

# Dataframe con varios diccionarios

# Crear un dataFrame sobre la cantidad de elementos quimicos que se estan dando en un experimento
""" print('Reporte ventas de elementos quimicos:\n')
elementos2021 = {'Hidrogeno': 2.5,
                 'Helio': 7.8,
                 'Oxygeno': 3.1,
                 'Nitrogeno': 5.4,
                 'Sodio': 1.2,
                 'Magnesio': 2.7,
                 'Calcio': 1.5,
                 'Fosforo': 2.3,
                 'Azufre': 1.1,
                 'Argon': 0.9,
                 'Kripton': 0.8,
                 'Xenon': 0.7,
                 'Radon': 0.6, }
elementos2022 = {'Hidrogeno': 4.5,
                 'Helio': 5.8,
                 'Oxygeno': 2.3,
                 'Nitrogeno': 4.4,
                 'Sodio': 3.2,
                 'Magnesio': 5.7,
                 'Calcio': 1.5,
                 'Fosforo': 4.3,
                 'Azufre': 2.1,
                 'Argon': 7.9,
                 'Kripton': 6.8,
                 'Xenon': 1.7,
                 'Radon': 5.6, }

elementosQuimicos = pandas.DataFrame(
    [elementos2021, elementos2022], index=['2021', '2022'])
print(elementosQuimicos)
 """


# Lista de productos de un almacen
""" print('Lista de productos de un almacen:\n')
entradas = pandas.Series([45, 65, 76, 45, 67, 43, 89, 54, 98, 43, 65, 89], index=[
                         'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
salidas = pandas.Series([25, 45, 56, 25, 17, 3, 49, 34, 58, 13, 55, 39], index=['Enero', 'Febrero', 'Marzo',
                        'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
inventario = pandas.DataFrame({'Entradas': entradas, 'Salidas': salidas})
print(inventario) """


""" print('Traer solo los 10 primeros elementos de lal ista')
print(inventario.head(10))
print('Traer solo los 5 ultimos elementos de lal ista')
print(inventario.tail())
print('Traer elementos aleatorios')
print(inventario.sample(5))
print('Traer informacion estadistica')
print(inventario.describe())
print('Traer informacion basica')
print(inventario.info())
print('Traer conteo con value_counts')
print(inventario.value_counts())
print('Traer conteo con groupby')
print(inventario.groupby('Entradas').value_counts())"""


""" dFrame = pandas.DataFrame(numpy.arange(18).reshape(6, 3), columns=[
                          'a', 'b', 'c'], index=['A', 'B', 'C', 'D', 'E', 'F']) """

""" print(dFrame)
print('Indicie por su etiqueta o indice explicito')
print(dFrame.loc[['a']])
print('Indicie implicito dataframe')
print(dFrame.iloc['1'])
print('Por rango')
print(dFrame.iloc[3:5])
print('Por rango y columnas')
print(dFrame.iloc[3:5, 1:3])
print('Por rango y columnas y filas')
print(dFrame.iloc[3:5, 1:3, 'A'])
 """

# Por metodo loc e iloc
""" print('Por metodo loc e iloc')
print('Editar por posision del index')
dFrame.iloc[0, 0] = 100
print(dFrame)
print('Editar por etiqueta')
dFrame.loc['A', 'a'] = 200
print(dFrame)
print('Editar toda una fila')
dFrame.iloc[0:] = 14
print(dFrame)
print('Editar una sola fila')
dFrame.iloc[0:1, 0:3] = 7
print(dFrame)

print('Editar la fila C')
dFrame.loc['C'] = [1, 2, 3]
print(dFrame)
 """

# Metodo where
df = pandas.DataFrame(numpy.arange(1, 19).reshape(6, 3), columns=[
    'A', 'B', 'C'], index=['a', 'b', 'c', 'd', 'e', 'f'])
df2 = pandas.DataFrame(numpy.arange(1, 13).reshape(4, 3), columns=[
    'A', 'B', 'C'], index=['a', 'b', 'c', 'd'])
print(df)
print(df2)
""" print('Metodo where')
# Saber cuales son pares
print(df.where(df % 2 == 0))
par = df.where(df % 2 == 0)
print(par)
# Saber cuales son impares
print(df.where(df % 2 != 0))
impar = df.where(df % 2 != 0)
print(impar)
lista = []
for i in range(par.shape[0]):
    for j in range(par.shape[1]):
        if not(pandas.isna(par.iloc[i, j])):
            lista.append(par.iloc[i, j])
print(lista)


lista2 = []
for i in range(impar.shape[0]):
    for j in range(impar.shape[1]):
        if not(pandas.isna(impar.iloc[i, j])):
            lista2.append(impar.iloc[i, j])
print(lista2)
 """

# Eliminar por filas
print('Eliminar por filas')
print(df.drop(['c', 'd']))
print('Eliminar por columna')
print(df.drop(columns=['B']))

# Funcion concat
print('Funcion concat')
union = pandas.concat([df, df2])
print(union)
