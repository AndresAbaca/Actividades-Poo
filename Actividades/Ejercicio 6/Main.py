from ViajeroFrecuente import ManejadorViajero

if __name__== '__main__':
    lista = ManejadorViajero()
    lista.testViajero()
    b = input('Ingrese numero de viajero: ')
    n = lista.buscaViajero(b)
    opc = None
    if(n == None):
        print("El numero de viajero no existe.")
    else:
        while(opc != '0'):
            opc = input('''--Menu--
            1) Consultar cantidad de millas.
            2) Acumular Millas.
            3) Canjear millas.
            4) Buscar viajeros con el maximo de millas.
            0) Terminar con el programa.
            ''')
            if opc == '1':
                print(f"La cantidad total de millas es: {lista.getMillas(n)}")
            elif opc == '2':
                nuevas_millas = int(input('Ingrese la cantidad de millas nuevas: '))
                print(f"Su total de millas es: {lista.acumularMillas(nuevas_millas,n)}")
            elif opc == '3':
                cant = int(input('Ingrese cantidad de millas a canjear: '))
                lista.canjearMillas(cant,n)
            elif opc == '4':
                lista.comparaViajeros()
        print("Saliendo....")    