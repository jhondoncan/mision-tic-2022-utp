def AutoPartes(ventas: list):
    diccionario = {}
    for i in range(len(ventas)):
        diccionario[i] = [ventas[i]]
    return diccionario


def consultaRegistro(ventas: dict, idProducto: int):
    nuvoDiccionario = {}
    respuesta = ''
    for i in range(len(ventas)):
        if ventas[i][0][0] == idProducto:
            nuvoDiccionario[i] = ventas[i]

    if len(nuvoDiccionario) == 0:
        respuesta = 'No hay registro de venta de ese producto'

    for valoresDic in nuvoDiccionario.values():
        for idProducto, dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in valoresDic:
            respuesta += (f'Producto consultado : {idProducto}  Descripción  {dProducto}  #Parte  {pnProducto}  Cantidad vendida  {cvProducto}  Stock  {sProducto}  Comprador {nComprador}  Documento  {cComprador}  Fecha Venta  {fVenta}\n')
    print(respuesta)


consultaRegistro(AutoPartes([
    (2001, 'rosca', 'PT29872', 2, 45, 'Luis Molero', 3456, '12/06/2020'),
    (2010, 'bujía', 'MS9512', 4, 15, 'Carlos Rondon', 1256, '12/06/2020'),
    (2010, 'bujía', 'ER6523', 9, 36, 'Pedro Montes', 1243, '12/06/2020'),
    (3578, 'tijera', 'QW8523', 1, 128, 'Pedro Faria', 1456, '12/06/2020'),
    (9251, 'piñón', 'EN5698', 2, 8, 'Juan Peña', 565, '12/06/2020')]), 2010)


""" print('Autopartes')
print(AutoPartes([
    (2001, 'rosca', 'PT29872', 2, 45, 'Luis Molero', 3456, '12/06/2020'),
    (2010, 'bujía', 'MS9512', 4, 15, 'Carlos Rondon', 1256, '12/06/2020'),
    (2010, 'bujía', 'ER6523', 9, 36, 'Pedro Montes', 1243, '12/06/2020'),
    (3578, 'tijera', 'QW8523', 1, 128, 'Pedro Faria', 1456, '12/06/2020'),
    (9251, 'piñón', 'EN5698', 2, 8, 'Juan Peña', 565, '12/06/2020')]), 2010) """


# Copiado de plataforma
"""def AutoPartes(ventas:list):
    diccionario = {}
    for i in range(len(ventas)):
        diccionario[i] = [ventas[i]]
    return diccionario
   
def consultaRegistro(ventas,idProducto):
    diccionario = {}
    respuesta=''
    for i in range(len(ventas)) :
        if ventas[i][0][0] == idProducto:
            diccionario[i] = ventas[i]
          
    if len(diccionario) == 0:
        respuesta = 'No hay registro de venta de ese producto'
    
    for valoresDic in diccionario.values(): 
        for idProducto,dProducto,pnProducto,cvProducto,sProducto,nComprador,cComprador,fVenta in valoresDic:
            respuesta += (f'Producto consultado : {idProducto}  Descripción  {dProducto}  #Parte  {pnProducto}  Cantidad vendida  {cvProducto}  Stock  {sProducto}  Comprador {nComprador}  Documento  {cComprador}  Fecha Venta  {fVenta}\n')      
    print(respuesta)"""
