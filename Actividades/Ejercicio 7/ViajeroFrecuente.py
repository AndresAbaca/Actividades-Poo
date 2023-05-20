class ViajeroFrecuente:
    __num = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self, num, dni, nombre, apellido, millas = 0):
        self.__num = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas

    def __str__(self):
        return (f'Nombre: {self.__nombre}\nMillas acumuladas: {self.__millas_acum}')
        
    def get_nombre(self):
        return self.__nombre

    
    def getNumero(self):
        return self.__num
    

    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def __gt__(self, otro):
        return (self.__millas_acum > otro.__millas_acum)

    def __add__(self, otro):
        return ViajeroFrecuente(self.__num, self.__dni, self.__nombre, self.__apellido,
            self.__millas_acum + otro)

    __radd__ = __add__

    def __sub__(self, otro):
        total = self.__millas_acum
        if self.__millas_acum >= otro:
            total = self.__millas_acum - otro
        return ViajeroFrecuente(self.__num, self.__dni, self.__nombre, self.__apellido, total)
        
    __rsub__ = __sub__

    def __eq__(self, otro):
        return self.__millas_acum == otro

    __req__ = __eq__