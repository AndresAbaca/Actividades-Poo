class Materia:
    __dni=''
    __materia = ''
    __fecha = ''
    __nota = 0
    __aprobacion = ''

    def __init__(self, dni, mat, fecha, nota, a):
        self.__dni = dni
        self.__materia = mat
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = a
        
    
    def getNota(self):
        return self.__nota
    
    def getApobado(self):
        return self.__aprobacion
    
    def getId(self):
        return self.__dni
        
    def getMateria(self):
        return self.__materia

    def getfecha(self):
        return self.__fecha
    
    