import os
import numpy as np
precio=0
def ValidateOpt():
    while(True):
        try:
            opt=int(input("Ingrese opción: "))
            if(opt>0 and opt<6):
                break
            else:
                print("ERROR: Debe ser una de las opciones del menú.")
        except ValueError:
            print("ERROR: ValueError")
    return opt

def BuyApartment(matrizReceive,rutReceive):
    os.system("cls")
    matrizCopy=matrizReceive[::-1]
    print("     TIPO")
    print("  A  B  C  D")
    print(matrizCopy)
    while(True):
        try:
            piso=int(input("Ingrese el piso en el que desea comprar departamento. Son 10 pisos: "))
            if(piso>0 and piso<11):
                break
            else:
                print("ERROR: Debe ser un piso existente. Entre 1 y 10.")
        except ValueError:
            print("ERROR. ValueError")
    while(True):
        tipo=""
        print("TIPO: A  B  C  D")
        tipo=input("Ingrese el tipo de departamento que desea comprar: ").upper()
        if(tipo=="A" or tipo=="B" or tipo=="C" or tipo=="D"):
            break
        else:
            print("ERROR: Debe ser uno de los tipos señalados.")
    
    if(tipo=="A"):
        if(matrizReceive[piso-1,0]=="X"):
            print("No esta disponible.")
            os.system("pause")
            return
        else:
            matrizReceive[piso-1,0]="X"
            precio==3800
    elif(tipo=="B"):
        if(matrizReceive[piso-1,1]=="X"):
            print("No esta disponible.")
            os.system("pause")
            return
        else:
            matrizReceive[piso-1,1]="X"
            precio==3000
    elif(tipo=="C"):
        if(matrizReceive[piso-1,2]=="X"):
            print("No esta disponible.")
            os.system("pause")
            return
        else:
            matrizReceive[piso-1,2]="X"
            precio==2800
    elif(tipo=="D"):
        if(matrizReceive[piso-1,3]=="X"):
            print("No esta disponible.")
            os.system("pause")
            return
        else:
            matrizReceive[piso-1,3]="X"
            precio==3500
    while(True):
        try:
            rut=int(input("Ingrese su RUT sin código verificador. Mínimo 8 números: "))
            if(len(str(rut))==8):
                rutReceive.append(rut)
                break
            else:
                print("ERROR: Debe ser un RUT válido.")
        except ValueError:
            print("ERROR: ValueError")
    print("Venta realizada exitosamente.")
    os.system("pause")

def ShowApartments(matrizReceive):
    os.system("cls")
    matrizCopy=matrizReceive[::-1]
    print("     TIPO")
    print("  A  B  C  D")
    print(matrizCopy)
    os.system("pause")

def BuyerList(rutReceive):
    os.system("cls")
    print("Listado de RUTs de compradores, de menor a mayor.")
    Swap=True
    while(Swap==True):
        Swap=False
        for turn in range(len(rutReceive)-1):
            if(rutReceive[turn]>rutReceive[turn+1]):
                rutReceive[turn],rutReceive[turn+1]=rutReceive[turn+1],rutReceive[turn]
                Swap=True
    print(rutReceive)
    os.system("pause")

def CalculateTotal(matrizReceive):
    os.system("cls")
    totalA=0
    cantA=0
    totalB=0
    cantB=0
    totalC=0
    cantC=0
    totalD=0
    cantD=0
    totaldetotales=0
    cantTotal=0
    print("Tipo de Departamento    Cantidad    Total")
    for row in range (10):
        for column in range(4):
            if(matrizReceive[row,column]=="X"):
                if(matrizReceive[row,0]=="X"):
                    totalA+=3800
                    cantA+=1
                    totaldetotales+=3800
                    cantTotal+=1
                elif(matrizReceive[row,1]=="X"):
                    totalB+=3000
                    cantB+=1
                    totaldetotales+=3000
                    cantTotal+=1
                elif(matrizReceive[row,2]=="X"):
                    totalC+=2800
                    cantC+=1
                    totaldetotales+=2800
                    cantTotal+=1
                elif(matrizReceive[row,3]=="X"):
                    totalD+=3500
                    cantD+=1
                    totaldetotales+=3500
                    cantTotal+=1
    print("Tipo A 3.800 UF",cantA,totalA,sep="          ")
    print("Tipo B 3.000 UF",cantB,totalB,sep="          ")
    print("Tipo C 2.800 UF",cantC,totalC,sep="          ")
    print("Tipo D 3.500 UF",cantD,totalD,sep="          ")
    print("TOTAL          ",cantTotal,totaldetotales,sep="          ")
    os.system("pause")

def optExit():
    os.system("cls")
    print("Ha salido del programa.")
    print("Felipe Andres Madariaga Navarro. 11/7/2023")
    


