import numpy as np
import csv
from ClaseAlumno import Alumno


class ManejadorAlumno:
    __cantidad = 0
    __dimension = 0
    __incremento = 1

    def __init__(self, dimension = 1, incremento = 1):
        self.__arregloAlumnos = np.empty(dimension, dtype = Alumno)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarAlumno(self, unAlumno):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloAlumnos.resize(self.__dimension)
        self.__arregloAlumnos[self.__cantidad] = unAlumno
        self.__cantidad += 1

    def testAlumnos (self):
        archivo = open('alumnos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)

        for fila in reader:
            dni = fila[0]
            apellido = fila[1]
            nombre = fila[2]
            carrera = fila[3]
            anioquecursa = fila[4]
            self.agregarAlumno(Alumno(dni, apellido, nombre, carrera, anioquecursa))
            
    def buscarAlumnos(self, dni):
        for Alumno in self.Alumno:
            if Alumno.dni == dni:
                return Alumno
        return None
    def getAlumnos(self):
        return self.Alumno

    def promedio_con_aplazos(self, dni):
        alumno = self.buscarAlumnos(dni)
        if alumno is not None:
           materias_aprobadas = self.__manejador_materias.get_materias_aprobadas(dni)
           promedio = sum(materia.get_nota() for materia in materias_aprobadas) / len(materias_aprobadas)
           return promedio
        else:
            return None

    def promedio_sin_aplazos(self, dni):
        alumno = self.buscarAlumnos(dni)
        if alumno is not None:
            materias_aprobadas = self.__manejador_materias.get_materias_aprobadas(dni)
            materias_aprobadas_sin_aplazos = [materia for materia in materias_aprobadas if materia.get_nota() >= 4]
            promedio = sum(materia.get_nota() for materia in materias_aprobadas_sin_aplazos) / len(materias_aprobadas_sin_aplazos)
            return promedio
        else:
            return None
    def listar_alumnos_ordenados(self):
        return sorted(self.getAlumnos)