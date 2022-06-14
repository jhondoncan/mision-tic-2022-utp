def cliente(informacion: dict) -> dict:

    apt = False
    atr = 'N/A'
    vr = 'N/A'

    if informacion['edad'] > 18:
        apt = True
        atr = 'X-Treme'
        if informacion['primer_ingreso']:
            vr = 19000.0
        else:
            vr = 20000

    if informacion['edad'] >= 15 and informacion['edad'] <= 18:
        apt = True
        atr = 'Carros chocones'
        if informacion['primer_ingreso']:
            vr = 4650.0
        else:
            vr = 5000

    if informacion['edad'] >= 7 and informacion['edad'] < 15:
        apt = True
        atr = 'Sillas voladoras'
        if informacion['primer_ingreso']:
            vr = 9500.0
        else:
            vr = 10000

    respuesta = {}
    respuesta['nombre'] = informacion['nombre']
    respuesta['edad'] = informacion['edad']
    respuesta['atraccion'] = atr
    respuesta['apto'] = apt
    respuesta['primer_ingreso'] = informacion['primer_ingreso']
    respuesta['total_boleta'] = vr

    return respuesta


informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 2,
    'primer_ingreso': True
}
print(cliente(informacion))
