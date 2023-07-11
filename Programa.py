import os
import numpy as np
import Funciones as fn

matriz=np.empty((10,4),type(object))

rutArray=[]
llenado=1

for row in range(10):
    for column in range(4):
        matriz[row,column]=llenado
        llenado+=1

while(True):
    os.system("cls")
    print("""
    ============ Inmobiliaria Casa Feliz ============
    1. Comprar departamento
    2. Mostrar departamentos disponibles
    3. Ver listado de compradores
    4. Mostrar ganancias totales
    5. Salir
    """)

    opt=fn.ValidateOpt()
    if(opt==1):
        fn.BuyApartment(matriz,rutArray)
    if(opt==2):
        fn.ShowApartments(matriz)
    if(opt==3):
        fn.BuyerList(rutArray)
    if(opt==4):
        fn.CalculateTotal(matriz)
    if(opt==5):
        fn.optExit()
        break