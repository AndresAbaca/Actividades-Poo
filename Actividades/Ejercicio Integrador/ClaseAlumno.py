class Alumno:
    __DNI = ''
    __apellido = ''
    __nombre = ''
    __carrera = ''
    __aniocursado = ''
    
    
    def __init__(self, dni, ap, nom, car, anioc):
        self.__DNI = dni
        self.__apellido = ap
        self.__nombre = nom
        self.__carrera = car 
        self.__añocursado = anioc
     
    def __lt__(self, other):
        if self.__aniocursado == other.getCursado():
            if self.__apellido == other.getApellido():
                return self.__nombre < other.getNombre()
            else:
                return self.__apellido < other.getApellido()
        else:
            return self.__añocursado < other.getCursado()    
        
    

    def getDni(self):
        return self.__DNI

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getCarrera(self):
        return self.__carrera

    def getCursado(self):
        return self.__añocursado

    def __str__(self):
        
        return(f'DNI:{self.__DNI}\nApellido: {self.__apellido}\nNombre: {self.__nombre}\nCarrera: {self.__carrera}\n Año: {self.__añocursado}\t')

