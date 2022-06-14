import pandas as pd
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'


def listaPeliculas(rutaFileCsv: str) -> str:
    if rutaFileCsv.split('.')[-1] != 'csv':
        try:
            csv = pd.read_csv(rutaFileCsv)
            subConjuntoPeliculas = csv[[
                'Country', 'Language', 'Gross Earnings']]
            subConjuntoFinal = subConjuntoPeliculas.pivot_table(
                index=['Country', 'Language'])
            return subConjuntoFinal.head(10)
        except:
            print('Error al leer el archivo de datos.')
    else:
        print('Extensión invalida.')


print(listaPeliculas(rutaFileCsv))
