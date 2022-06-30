import json
#Consultar la información de todas las tareas (Read)


def Read(rutaArchivo='/home/doncan/Documentos/utp/mision-tic-2022-utp/ciclo 1/semana 7/tareasCRUD/appTareas/listadoTareas.json'):


    #Cargar el listado de tareas a un diccionario desde la capa de datos (archivo JSON)    
    diccionarioTareas = {}#Contenedor del listado de tareas que gestiona la App
    try:    
        with open(rutaArchivo) as archivo:
            diccionarioTareas = json.load(archivo)
    except:
        print("No se pudo cargar la información de la capa de datos")
        return False #Reportar fallo en la carga


    #Retornar el contenedor o colección obtenido
    return diccionarioTareas