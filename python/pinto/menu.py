opcion = 0

DEFINICION_METRO = 1





def menu_de_km_a_millas(km):
    return km * 0.621371

def menu_millas_a_km(millas):
    return millas * 1.60934

def menu_principal() :
    
    while True:

        print("\n conversor de distancias")
        print("1: que reporonga es una milla")
        print("2: what the fuck is a kilometer")
        print("3: conversor")
        print("4: Salir")
        opcion = int(input("elige una opcion: "))

        if opcion == DEFINICION_METRO :

            print("Medida itineraria de los romanos, que equivalía a 1478,5 metro(s)")

        elif opcion == 2 :

            print("Unit of length equivalent to 1000 meters.")

    
        elif opcion == 3 :

            menu_conversor_distancias()

        else :

            print("chau")
            break

def menu_conversor_distancias():

    opcion = 0

    while True:

        print("\n que medida convertir")
        print("1: pasar millas a kilometros")
        print("2: pasar kilometors a millas")
        print("3: atras")

        try:

            opcion = float(input("elige una opcion: "))

        except ValueError:

            print("porfavor ingrese un numero valido")

            continue

        if opcion == 1:
            
            try:

                millas = float(input("cantidad de millas: "))
                millas = menu_millas_a_km(millas)
                print("cantidad de kilometros en millas: ", millas)

            except ValueError:

                print("ingrese un numero valido")

                continue

        elif opcion == 2:

            try:

                km = float(input("cantidad de km: "))
                km = menu_de_km_a_millas(km)
                print("cantidad de millas: ",km)

            except ValueError:

                print("ingrese un numero valido")

                continue

        elif opcion == 3:
            break

        else:
            print("opcion no valida")

menu_principal()