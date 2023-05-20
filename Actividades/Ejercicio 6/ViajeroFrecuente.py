import csv
class ViajeroFrecuente:
    __num_viajero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0
    def __init__(self, num, dni, nom, apellido, millas):
        self.__num_viajero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = apellido
        self.__millas_acum = millas
    def getNumViajero(self):
        return(self.__num_viajero)
    def getTotalMillas(self):
        return(self.__millas_acum)
    def acumularMillas1(self,nuevas_millas):
        self.__millas_acum += nuevas_millas
        return(self.__millas_acum)
    def canjearMillas1(self,numerocanjeador):
        if(numerocanjeador <= self.__millas_acum):
            print("Error. millas insuficientes.")
        else:
            self.__millas_acum = self.__millas_acum - numerocanjeador
            print("Sus millas han sido canjeadas, su total de millas son: ",self.__millas_acum)
        return()
    
class ManejadorViajero:
    def __init__(self):
        self.__listaViajero= []
    def agregarViajero(self,unViajero):
        self.__listaViajero.append(unViajero)
    def testViajero(self):
        archivo = open('C:\\Users\\Andres\\Desktop\\Python\\Ejemplos practica\\Ejercicio 2\\Datos2.csv')
        reader = csv.reader(archivo,delimiter = ',')
        for i in reader:
            num = i[0]
            dni = i[1]
            nom = i[2]
            apellido = i[3]
            millas = int(i[4])
            unViajero = ViajeroFrecuente(num,dni,nom,apellido,millas)
            self.agregarViajero(unViajero)
        archivo.close()
    def buscaViajero(self,num):
        i=0
        Retorno = None
        b = False
        while not b and i < len(self.__listaViajero):
            if self.__listaViajero[i].getNumViajero()==num:
                b =True
                Retorno=i
            else:
                i+=1
        return Retorno
    def getMillas(self,n):
        return(self.__listaViajero[n].getTotalMillas())
    def acumularMillas(self,nuevas_millas,n):
        m = self.__listaViajero[n].acumularMillas1(nuevas_millas)
        return m
    def canjearMillas2(self,cant,n):
        self.__listaViajero[n].canjearMillas1(cant)
        return

    def buscaMaximo(self):
    i = 0
    b = len(self.__listaViajero)
    for i in range(b):
        if (i == b):
            return max_millas
        else:
            if(self.__listaViajero[i] > self.__listaViajero[i+1]):
                max_millas = self.__listaViajero[i].getTotalMillas()
            else:
                max_millas = self.__listaViajero[i+1].getTotalMillas()
     
        
     def compararViajeros(self):
    i = 0
    max = self.buscaMaximo()
    for i in range(len(self.__listaViajero)):
        if(self.__listaViajero[i].getTotalMillas == max):
            print("El viajero",self.__listaViajero[i].getNumViajero(),"tiene el maximo de millas.")
        return
