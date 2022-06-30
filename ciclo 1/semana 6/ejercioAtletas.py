import json
print("\x1Bc")
### ARCHIVOS .JSON
# Ejercicio 1
""" atletas = {

}
atletas['datos_basicos'] = []
atletas['datos_basicos'].append(
    {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 20, 'genero': 'M', 'partidos': 7, 'partidos_ganados': 3, 'partidos_perdidos': 4})

atletas['datos_basicos'].append(
    {'nombre': 'Richard', 'apellido': 'Andrade', 'edad': 22, 'genero': 'M', 'partidos': 6, 'partidos_ganados': 4, 'partidos_perdidos': 2})

atletas['datos_basicos'].append(
    {'nombre': 'Jan', 'apellido': 'Bonilla', 'edad': 24, 'genero': 'M', 'partidos': 3, 'partidos_ganados': 3, 'partidos_perdidos': 3})
atletas['datos_basicos'].append(
    {'nombre': 'Julian', 'apellido': 'Romero', 'edad': 20, 'genero': 'M', 'partidos': 10, 'partidos_ganados': 6, 'partidos_perdidos': 4})

print(atletas)

# Exportar a archivo JSON
with open('atletas.json', 'w') as archivo:
    json.dump(atletas, archivo)
    print('Se ha creado el archivo atletas.json con exito') """

# Abrir archivo JSON
with open('atletas.json') as archivo:
    atletas = json.load(archivo)
    print(atletas)
    print('Se ha cargado el archivo atletas.json con exito')

# Leer archivo JSON
for atleta in atletas['datos_basicos']:
    print('Nombres:', atleta['nombre'])
    print('Apellidos:', atleta['apellido'])
    print('Edad:', atleta['edad'])
    print('Genero:', atleta['genero'])
    print('Partidos:', atleta['partidos'])
    print('Partidos ganados:', atleta['partidos_ganados'])
    print('Partidos perdidos:', atleta['partidos_perdidos'])
    print('\n')
