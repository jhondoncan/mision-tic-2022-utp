import pandas as pd
print("\x1Bc")

# CREAR ARCHIVO .csv
# 1 Crear DataFrame
""" dictDatos = {'Nombre': ['Juan', 'Pedro', 'Maria', 'Juan', 'Pedro', 'Maria'],
             'Apellidos': ['Perez', 'Lopez', 'Andrade', 'Guilombo', 'Culma', 'Hernandez'],
             'Edad': [20, 21, 19, 20, 21, 19],
             'Genero': ['M', 'M', 'F', 'M', 'M', 'F'],
             'Partido 1': ['7.5', '6.8', '5.4', '7.5', '6.8', '5.4'],
             'Partido 2': ['3.8', '3.6', '0.0', '2.5', '5.2', '4.5']} """

# 2 Crear DataFrame
""" deportistas = pd.DataFrame(dictDatos)
print(deportistas) """

# 3 Crear rchivo .csv
""" deportistas.to_csv('deportistas.csv', index=False)
print('Se ha creado el archivo deportistas.csv con exito')"""


# LEER ARCHIVO .CSV
"""

df = pd.read_csv('deportistas.csv')
print(df) """

""" try:
    deportistas.to_excel('deportistas.xlsx', index=False)
    print('Se ha creado el archivo deportistas.xlsx con exito')
except:
    print('No se ha podido crear el archivo') """


# LEER ARCHIVO .XLSX
""" df = pd.read_excel('deportistas.xlsx')
print(df) """


# Manejo de archivos de texto
""" x = open('text.txt', 'w')
lista = ['Juan', 'Pedro', 'Maria', 'Juan', 'Pedro', 'Maria', 'Doncan'] """

""" 
for i in lista:
    x.write(i + '\n')
x.close()
print('Se ha creado el archivo text.txt con exito') """

# Otra forma
""" x.writelines('%s\n' % item for item in lista)
x.close()
print('Se ha creado el archivo text.txt con exito') """

# Leer archivo de texto
archivoTexto = open('text.txt', 'r')
lineaALinea = archivoTexto.readlines()
print(lineaALinea)
archivoTexto.close()
# Eliminar saltos de linea
lineaALinea = [linea.strip() for linea in lineaALinea]
print(lineaALinea)


# Otra forma de leer 2
