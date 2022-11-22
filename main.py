


def registro():
    aux=True
    while aux == True:
        aux2=True
        while aux2 == True:
            nombre=input("ingrese el nombre del cuadro:")
            if len(nombre) > 30:
                print("Nombre del cuadro demasiado largo, favor no exceder los 30 caracteres, el nombre que ingreso posee" , len(nombre), " caracteres" )
                aux2 = True 
            elif len(nombre) < 30:          
                aux2 = False
        aux3=True
        while aux3 == True:
            letras=input("Ingrese 4 LETRAS para la cota: ")
            aux3 = False
        aux4=True
        while aux4 == True:
            numeros=input("Ingrese 4 NUMEROS para la cota: ")
            aux4 = False


    
                
               





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
            print ("Modulo de Consulta!!")
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