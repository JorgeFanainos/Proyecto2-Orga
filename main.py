import time
import json
nombres = ["cuadro1", "cuadro2", "cuadro3", "cuadro4", "cuadro5", "cuadro6", "cuadro7", "cuadro8", "cuadro9", "cuadro10"]
cotas = ["cota1234", "cota1334", "cota1434", "cota1534","cota1634", "cota1734", "cota1834", "cota1934", "cota2034", "cota2134"]
precios=[1234,15468,74846,48646,654654,84484,87684,8648461,168498,168468]
statuss=["M","M","M","M","M","E","E","E","E","E"]
elim= ["A","A","A","A","A","E","E","E","E","E"]
nombre_index=["cuadro1", "cuadro2", "cuadro3", "cuadro4", "cuadro5", "cuadro6", "cuadro7", "cuadro8", "cuadro9", "cuadro10"]
cotas_index = ["cota1234", "cota1334", "cota1434", "cota1534","cota1634", "cota1734", "cota1834", "cota1934", "cota2034", "cota2134"]

def registro():
    aux=True
    while aux == True:
        aux2=True
        while aux2 == True:
            nombre=input("\ningrese el nombre del cuadro:")
            if len(nombre) > 30:
                print("Nombre del cuadro demasiado largo, favor no exceder los 30 caracteres, el nombre que ingreso posee" , len(nombre), " caracteres" )
                aux2 = True 
            elif len(nombre) < 30:          
                aux2 = False
        aux3=True
        while aux3 == True:
            letras=input("\nIngrese 4 LETRAS para la cota: ")
            if letras.isalpha() == True and len(letras) == 4:
                aux3 = False
            else:
                print ("ingreso valores invalidos, intente nuevamente")
                aux3 = True
            
        aux4=True
        while aux4 == True:
            numeros=input("\nIngrese 4 NUMEROS para la cota: ")
            if numeros.isdigit() == True and len(numeros) == 4:
                aux4 = False
            else:
                print ("ingreso valores invalidos, intente nuevamente")
                aux4 = True
        cota = letras+numeros   
         
        while True:
            try:
                precio = int(input("\nPrecio de la obra: "))
            except ValueError:
                print("Debes escribir un número.")
                continue
            if precio < 0:
                print("Debes escribir un número positivo.")
                continue
            else:
                break 
        aux5=True
        while aux5 == True:
            status=input("\ningrese Estado de la pintura (M/E): ")
            status = status.upper()
            if status == "M" :
                aux5 = False
            elif status == "E" :
                aux5 = False
            else:
                print ("\ningreso valores invalidos, ingrese (M/E)")
                aux5 = True
        nombres.append(nombre)
        nombre_index.append(nombre)
        cotas.append(cota)
        cotas_index.append(cota)   
        precios.append(precio)
        statuss.append(status)

        time.sleep(1)
        print("\nHa registrado correctamente una pintura, felicidades\n\n")
        main()    


def busqueda():
    aux10=True
    while aux10 == True:
        busqueda = input("""Desea buscar por nombre o por cota?:
                            1)buscar por nombre             2)buscar por cota
                                                99)salir
         """)
        while True:
            if busqueda == "1":
                try:
                    nombre_busqueda = input("ingrese el nombre de la obra a buscar: ")
                    nombre_index.index(nombre_busqueda)
                    n = nombre_index.index(nombre_busqueda)
                    if elim[n] =="A":
                        print("Nombre: ",nombres[n])
                        print("Cota: ",cotas[n])
                        print("Precio: ",precios[n])
                        print("Estado: ",statuss[n])
                        break
                    else:
                        print("La busqueda que realizo no se encuentra registrada.")
                        continue    
                except ValueError:
                    print("La busqueda que realizo no se encuentra registrada.")
                    continue
                  
            elif busqueda == "2":
                try:
                    cota_busqueda = input("ingrese la cota de la obra a buscar: ")
                    cotas_index.index(cota_busqueda)
                    n = cotas_index.index(cota_busqueda)
                    if elim[n] =="A":
                        print("Nombre: ",nombres[n])
                        print("Cota: ",cotas[n])
                        print("Precio: ",precios[n])
                        print("Estado: ",statuss[n])
                        break
                    else:
                        print("La busqueda que realizo no se encuentra registrada.")
                        continue    
                except ValueError:
                    print("La busqueda que realizo no se encuentra registrada.")
                    continue
            elif busqueda == "99":
                main()
            else:
                print("Usted ingreso una opcion invalida, favor intente nuevamente!")
                break

def modificar():           
    while True:
        try:
            nombre_busqueda = input("ingrese el nombre de la obra a modificar: ")
            nombre_index.index(nombre_busqueda)
            n = nombre_index.index(nombre_busqueda)
            print("Nombre: ",nombres[n])
            print("Cota: ",cotas[n])
            print("Precio: ",precios[n])
            print("Estado: ",statuss[n])
            print("\n\n")
            aux5=True
            while aux5 == True:
                status=input("\ningrese Estado de la pintura (M/E): ")
                status = status.upper()
                if status == "E":
                    statuss[n]= status
                    print("Nombre: ",nombres[n])
                    print("Cota: ",cotas[n])
                    print("Precio: ",precios[n])
                    print("Estado: ",statuss[n])
                    print("\n")
                    aux5 = False
                    print("Modificacion exitosa!")
                    main()
                if status == "M":
                    statuss[n] = status
                    print("Nombre: ",nombres[n])
                    print("Cota: ",cotas[n])
                    print("Precio: ",precios[n])
                    print("Estado: ",statuss[n])
                    print("\n")
                    aux5 = False
                    print("Modificacion exitosa!")
                    main()
                else:
                    print("\nIngreso un dato invalido")
                    aux5 = True
            break
        except ValueError:
                    print("La busqueda que realizo no se encuentra registrada.")
                    continue
                  

def eliminar():
    while True:
        try:
            nombre_busqueda = input("ingrese el nombre de la obra a eliminar: ")
            nombre_index.index(nombre_busqueda)
            n = nombre_index.index(nombre_busqueda)
            print("Nombre: ",nombres[n])
            print("Cota: ",cotas[n])
            print("Precio: ",precios[n])
            print("Estado: ",statuss[n])
            print("Eliminacion: ",elim[n])
            print("\n\n")
            aux5=True
            while aux5 == True:
                eliminar=input("\ningrese Estado de la pintura (A/E): ")
                eliminar = eliminar.upper()
                if eliminar == "E":
                    elim[n]= eliminar
                    print("Nombre: ",nombres[n])
                    print("Cota: ",cotas[n])
                    print("Precio: ",precios[n])
                    print("Estado: ",statuss[n])
                    print("Eliminacion: ",elim[n])
                    print("\n")
                    aux5 = False
                    print("Modificacion exitosa!")
                    main()
                if eliminar == "A":
                    elim[n] = eliminar
                    print("Nombre: ",nombres[n])
                    print("Cota: ",cotas[n])
                    print("Precio: ",precios[n])
                    print("Estado: ",statuss[n])
                    print("Eliminacion: ",elim[n])
                    print("\n")
                    aux5 = False
                    print("Modificacion exitosa!")
                    main()
                else:
                    print("\nIngreso un dato invalido")
                    aux5 = True
            break
        except ValueError:
                    print("La busqueda que realizo no se encuentra registrada.")
                    continue

def compactador():
    print("MODULO DE ELIMINACION FISICA")


    

def main():
    print ("\nBienvenido!!")

    print ("""Que desea hacer?
        1)Registrar una pintura             2)Hacer una consulta
        3)Modificar Status                  4)Eliminar Pintura           
        5)Compactador                       99)Cerrar programa
                            
        """)
    aux=True
    while aux == True:
        seleccion=input("-->")
        if seleccion == "1":
            print ("Modulo de Registro de pintura!!")
            registro()
            aux = False
        elif seleccion == "2":
            busqueda()
        elif seleccion == "3":
            modificar()
            aux = False
        elif seleccion == "4":
            eliminar()
            aux = False
        elif seleccion == "5":
            compactador()
            aux = False
        elif seleccion == "99":
            break
        else:
            print ("Ingresó un valor inválido")
            aux = True
main()

