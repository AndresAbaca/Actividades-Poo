import csv
from ClaseMaterias import Materia

class ManejadorMaterias:
    __listaMaterias = []

    def __init__(self):
        self.__listaMaterias = []

    def agregarMateria(self, unaMateria):
        self.__listaMaterias.append(unaMateria)
    def buscar_materias_aprobadas(self, dni):
        return [Materia for Materia in self.__listaMaterias if Materia.getId() == dni]
    
    def buscar_materias_aprobadas_por_nombre(self, materia):
        return [Materia for Materia in self.__listaMaterias if Materia.getMateria()==materia]
    def testMateria(self):
        archivo = open('C:\\Users\\Andres\\Desktop\\Python\\Ejercicio Integrador\\archivo.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)

        for fila in reader:
            dni = fila[0]
            nombremateria = fila[1]
            fecha = fila[2]
            nota = fila[3]
            aprobacion = fila[4]
            self.agregarMateria(Materia(dni, nombremateria, fecha, nota, aprobacion))