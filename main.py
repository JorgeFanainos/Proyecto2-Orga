import time
import json
cuadros = {}
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
            status=input("\ningrese Estado de la pintura (EXHIBICION/MANTENIMIENTO): ")
            status = status.upper()
            if status == "EXHIBICION" :
                aux5 = False
            elif status == "MANTENIMIENTO" :
                aux5 = False
            else:
                print ("\ningreso valores invalidos, ingrese (EXHIBICION/MANTENIMIENTO)")
                aux4 = True
        data = {}
        data['cuadros'] = []
        data['cuadros'].append({
            'nombre': nombre,
            'cota': cota,
            'precio': precio,
            'status': status})

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        time.sleep(1)
        print("\nHa registrado correctamente una pintura, felicidades\n\n")
        main()    

    
                
               





def main():
    print ("Bienvenido!!")

    print ("""Que desea hacer?
        1)Registrar una pintura             2)hacer una consulta
        3)Poner Pintura en mantenimiento    4)Poner Pintura en Exhibicion
        5)Eliminar Pintura                  6)Compactador
        """)
    aux=True
    while aux == True:
        seleccion=input("-->")
        if seleccion == "1":
            print ("Modulo de Registro de pintura!!")
            registro()
            aux = False
        elif seleccion == "2":
            with open('data.json') as file:
                data = json.load(file)
                for cuadro in data['cuadros']:
                    print('nombre:', cuadro['nombre'])
                    print('cota:', cuadro['cota'])
                    print('precio:', cuadro['precio'])
                    print('status:', cuadro['status'])
                    print('')
            aux = False
        elif seleccion == "3":
            print ("Modulo de Poner en mantenimiento!!")
            aux = False
        elif seleccion == "4":
            print ("Modulo de Poner en Exhibicion!!")
            aux = False
        elif seleccion == "5":
            print ("Modulo de Eliminar!!")
            aux = False
        elif seleccion == "6":
            print ("Modulo de Compactar!!")
            aux = False
        else:
            print ("Ingresó un valor inválido")
            aux = True
main()
