import time
from xlrd import open_workbook
import xlwt


nombres = []
cotas = []
precios=[]
statuss=[]
elim= []
nombre_index=[]
cotas_index = []

def registro():
    aux=True
    while aux == True:
        aux2=True
        while aux2 == True:
            nombre=input("\ningrese el nombre del cuadro: ")
            if len(nombre) > 30:
                print("Nombre del cuadro demasiado largo, favor no exceder los 30 caracteres, el nombre que ingreso posee" , len(nombre), " caracteres" )
                aux2 = True 
            elif len(nombre) < 30:          
                aux2 = False
            for name in nombres:
                if nombre == name:
                    print("Nombre del cuadro ya ingresado, intente con otro")
                    aux2 = True
        
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
                cota = letras+numeros
                for cot in cotas:
                    if cota == cot:
                        print("Cota del cuadro ya ingresado, intente con otro")
                        aux4 = True   
            else:
                print ("ingreso valores invalidos, intente nuevamente")
                aux4 = True
        
        
        
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
            status_final = nombre + " "+status
            if status == "M" :
                aux5 = False
            elif status == "E" :
                aux5 = False
            else:
                print ("\ningreso valores invalidos, ingrese (M/E)")
                aux5 = True
        q=nombre+" A"
        nombres.append(nombre)
        nombre_index.append(nombre)
        cotas.append(cota)
        cotas_index.append(cota)   
        precios.append(precio)
        statuss.append(status_final)
        elim.append(q)
        time.sleep(1)
        print("\nHa registrado correctamente una pintura, felicidades\n\n")
        main()
        break    


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
                    if elim[n] ==nombre_busqueda+" A":
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
                    if elim[n] ==nombre_busqueda+" A":
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
    aux145 =True          
    while aux145==True:
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
                status_final2 = nombre_busqueda+" "+status
                if status == "E":
                    statuss[n] = status_final2
                    print("Nombre: ",nombres[n])
                    print("Cota: ",cotas[n])
                    print("Precio: ",precios[n])
                    print("Estado: ",statuss[n])
                    print("\n")
                    aux5 = False
                    print("Modificacion exitosa!")
                    aux145 =False 
                    break
          
                if status == "M":
                    statuss[n] = status_final2 
                    print("Nombre: ",nombres[n])
                    print("Cota: ",cotas[n])
                    print("Precio: ",precios[n])
                    print("Estado: ",statuss[n])
                    print("\n")
                    aux5 = False
                    aux145 =False
                    print("Modificacion exitosa!")
                    break
                    
                else:
                    print("\nIngreso un dato invalido")
                    aux5 = True
                    
            break
        except ValueError:
                    print("La busqueda que realizo no se encuentra registrada.")
                    aux145 =True
    main()
                  

def eliminar():
    aux154= True
    while aux154== True:
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
           
                if eliminar == "E" :
                    for i in elim:
                        if i == nombre_busqueda+" A":
                            elim.remove(i)
                    elim[n] = nombre_busqueda+" "+eliminar
                    print("Nombre: ",nombres[n])
                    print("Cota: ",cotas[n])
                    print("Precio: ",precios[n])
                    print("Estado: ",statuss[n])
                    print("Eliminacion: ",elim[n])
                    print("\n")
                    aux5 = False
                    print("Modificacion exitosa!")
                    aux154=False
                    break
                if eliminar == "A":
                    for i in elim:
                        if i == nombre_busqueda+" E":
                            elim.remove(i)
                    elim[n] = nombre_busqueda+" "+eliminar
                    print("Nombre: ",nombres[n])
                    print("Cota: ",cotas[n])
                    print("Precio: ",precios[n])
                    print("Estado: ",statuss[n])
                    print("Eliminacion: ",elim[n])
                    print("\n")
                    aux5 = False
                    print("Modificacion exitosa!")
                    
                    aux154=False
                    break
                else:
                    print("\nIngreso un dato invalido")
                    aux5 = True
            
            break
        except ValueError:
                    print("La busqueda que realizo no se encuentra registrada.")
                    aux154=True
    main()

def compactador():
    

    fichero_distancias = xlwt.Workbook()
    datos = fichero_distancias.add_sheet("datos")
    for nombre in nombres:
        for w in elim:
            if w ==nombre+" A":
                for i in range(len(nombres)):
                    datos.write(i, 0, nombres[i])
                for i in range(len(cotas)):
                    datos.write(i, 1, cotas[i])
                for i in range(len(precios)):
                    datos.write(i, 2, precios[i])
                for i in range(len(statuss)):
                    datos.write(i, 3, statuss[i])
                for i in range(len(elim)):
                    datos.write(i, 4, elim[i])
                for i in range(len(nombre_index)):
                    datos.write(i, 5, nombre_index[i])
                for i in range(len(cotas_index)):
                    datos.write(i, 6, cotas_index[i])

    fichero_distancias.save("CUADROS.xls")


def guardar_excel():
    fichero_distancias = xlwt.Workbook()
    datos = fichero_distancias.add_sheet("datos")

    for i in range(len(nombres)):
        datos.write(i, 0, nombres[i])
    for i in range(len(cotas)):
        datos.write(i, 1, cotas[i])
    for i in range(len(precios)):
        datos.write(i, 2, precios[i])
    for i in range(len(statuss)):
        datos.write(i, 3, statuss[i])
    for i in range(len(elim)):
        datos.write(i, 4, elim[i])
    for i in range(len(nombre_index)):
        datos.write(i, 5, nombre_index[i])
    for i in range(len(cotas_index)):
        datos.write(i, 6, cotas_index[i])

    fichero_distancias.save("CUADROS.xls")


    

def main():
    wb = open_workbook('CUADROS.xls') 
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    column_index = 0
    column_index1 = 5
    column_index2 = 1
    column_index3 = 6
    column_index4 = 2
    column_index5 = 3
    column_index6 = 4
    column = sheet.cell_value(0, column_index)
    for row in range(0, sheet.nrows):
        nombres.append(sheet.cell_value(row, column_index))
        nombre_index.append(sheet.cell_value(row, column_index1))
        cotas.append(sheet.cell_value(row, column_index2))
        cotas_index.append(sheet.cell_value(row, column_index3))
        precios.append(sheet.cell_value(row, column_index4))
        statuss.append(sheet.cell_value(row, column_index5))
        elim.append(sheet.cell_value(row, column_index6))
    for name in nombres:
        if nombres.count(name) > 1:
            nombres.remove(name)
    for namein in nombre_index:
        if nombre_index.count(namein) > 1:
            nombre_index.remove(namein)
    for cot in cotas:
        if cotas.count(cot) > 1:
            cotas.remove(cot)
    for cotin in cotas_index:
        if cotas_index.count(cotin) > 1:
            cotas_index.remove(cotin)
    for pre in precios:
        if precios.count(pre) > 1:
            precios.remove(pre)
    for sta in statuss:
        if statuss.count(sta) > 1:
            statuss.remove(sta)
    for el in elim:
        if elim.count(el) > 1:
            elim.remove(el)

    print(nombres)
    print ("\nBienvenido!!")

    print ("""Que desea hacer?
        1)Registrar una pintura             2)Hacer una consulta
        3)Modificar Status                  4)Eliminar Pintura           
        5)Compactador                       6)Guardar datos
        99)Cerrar programa
                            
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
        elif seleccion == "6":
            guardar_excel()
            aux = False
        elif seleccion == "99":
            aux = False
            break
        else:
            print ("Ingresó un valor inválido")
            aux = True
main()
