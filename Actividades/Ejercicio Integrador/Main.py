from ClaseManejadorAlumno import ManejadorAlumno
from ClaseManejadorMaterias import ManejadorMaterias
from ClaseAlumno import Alumno

    



if __name__ == '__main__':
  
  manejadoralumno = ManejadorAlumno()
  manejadormateria = ManejadorMaterias()
  manejadoralumno.testAlumnos()
  manejadormateria.testMateria()

  def opcion0(Al,Ma,Mm):
    print('Adios')
def opcion1(Al,Ma,Mm):
    print ('Ingrese el dni del alumno a consultar ')
alumnodni =(input())
notas=manejadoralumno.promedio_sin_aplazos(Alumno)
print('El total de notas por el alumno es{}'.format(notas))
def opcion2(Al,Ma,Mm):
    print ('Ingrese datos para generar informe: ')
lista = (input())
manejadoralumno.listar_alumnos_ordenados(lista)
switcher = {
0: opcion0,
1: opcion1,
2: opcion2
}
def switch(argument,mv,indice):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
func(mv,indice)

print('Ingrese Alumnos: ')
C=(input())
print('Ingrese notas ')
D=(input())
print(manejadormateria.__listaMaterias)

bandera = False
while not bandera:
 print("\nMENU DE OPCIONES")
 print("0 Salir")
 print("1 ITEM 3.1: Mostrar la Cantidad de kg descargados por un camión")
 print("2 ITEM 3.2: Mostrar Listado de descargar para un día")
opcion = int(input ('Ingrese una opcion:'))
switch(opcion, Al,Ma,Mm)
bandera = int(opcion)== 0