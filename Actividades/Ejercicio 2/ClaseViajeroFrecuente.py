class ViajeroFrecuente():
    def  __init__(self, numviaj, dni, nom, apelli, millas):
        self.__num_viajero = numviaj
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = apelli
        self.__millas_acum = millas
    
    def getNumeroViajero(self):
        return self.__num_viajero
    
    def getCanitidadTotalDeMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self, nuevasMillas):
        if nuevasMillas < 0:
            print("Error. No ingreso una cantidad valida.")
        else:
            self.__millas_acum += nuevasMillas
    
    def canjearMillas(self, cantCanje):
        if cantCanje < 0:
            print("Error. No ingreso una cantidad valida.")
        else:
            if cantCanje > self.getCanitidadTotalDeMillas():
                print("Error. No tiene la cantidad necesaria de millas.")
            else:
                self.__millas_acum -= cantCanje
        return self.getCanitidadTotalDeMillas()
        
    