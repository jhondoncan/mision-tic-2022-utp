def cliente(informacion):
    informacion = {
        'id_cliente': 1,
        'nombre': 'Johana Fernandez',
        'edad': 20,
        'primer_Ingreso': True
    }
    print(cliente(informacion))

    if informacion['edad'] > 18:
        informacion['atraccion'] = 'X-Treme'
        informacion['apto'] = True
        if informacion['primer_Ingreso'] == True:
            informacion['total_boleta'] = 20000 - (20000 * 0.05)
        else:
            informacion['total_boleta'] = 20000

    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        informacion['atraccion'] = 'Carros chocones'
        informacion['apto'] = True
        if informacion['primer_Ingreso'] == True:
            informacion['total_boleta'] = 5000-(5000 * 0.07)
        else:
            informacion['total_boleta'] = 5000

    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        informacion['atraccion'] = "Sillas voladoras"
        informacion['apto'] = True
        if informacion['primerIngreso'] == True:
            informacion['total_boleta'] = 10000 - (10000 * 0.05)
        else:
            informacion['total_boleta'] = 10000
    else:
        informacion['atraccion'] = "N/A"
        informacion['apto'] = False
        informacion['total_boleta'] = "N/A"


def cliente(salida):
    salida = {
        'nombre':	['nombre'],
        'edad': ['edad'],
        'atraccion': ['atraccion'],
        'apto': ['apto'],
        'primer_Ingreso': ['primer_Ingreso'],
        'total boleta': ['total_boleta']
    }
    print(salida)
