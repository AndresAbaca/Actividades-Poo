import csv
from ClaseRegistro import Registro

def mostrar_mayorT(lista):
    max_t = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_temperatura() > max_t:
                max_t = lista[i][j].get_temperatura() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")

def mostrar_menorT(lista):
    min_t= 100000
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_temperatura() < min_t:
                min_t = lista[i][j].get_temperatura() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")

def mostrar_mayorPres(lista):
    max_p = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_presion() > max_p:
                max_p = lista[i][j].get_presion() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")

def mostrar_menorPres(lista):
    min_p= 10000
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_presion() < min_p:
                min_p= lista[i][j].get_presion() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")

def mostrar_mayorHum(lista):
    max_h = -1
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_humedad() > max_h:
                max_h = lista[i][j].get_humedad() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")

def mostrar_menorHum(lista):
    min_h = 10000
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_humedad() < min_h:
                min_h = lista[i][j].get_humedad() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")

def temp_prom(lista):
    print("___TEMPERATURA PROMEDIO___")
    for i in range(len(lista)):
        suma = 0
        for j in range(len(lista[i])):
            suma += int(lista[i][j].get_temperatura())
        prom = suma/dias
        print(f"Hora:{i}\t Promedio:{prom}")

def listar_variables(lista):
    print('Ingrese dia para listar')
    dia = int(input('Dia: '))
    for i in range(len(lista)):
        print(lista[i][dia - 1])

def menu(lista):
    print('Elije una opcion.: ')
    print('1 - Mostrar el día y hora de menor y mayor valor.')
    print('2 - Indicar la temperatura promedio del mes por cada hora.')
    print('3 - listar los valores de las tres variables para cada hora del día dado')
    opcion = int(input('Opcion: '))
    match opcion:
        case 1:
            print(f"LA TEMPERATURA MAXIMA ES: ")
            mostrar_mayorT(lista)
            print(f"LA TEMPERATURA MINIMA ES: ")
            mostrar_menorT(lista)
            print(f"LA PRESION MAXIMA ES: ")
            mostrar_mayorPres(lista)
            print(f"LA PRESION MINIMA ES: ")
            mostrar_menorPres(lista)
            print(f"LA HUMEDAD MAXIMA ES: ")
            mostrar_mayorHum(lista)
            print(f"LA HUMEDAD MINIMA ES: ")
            mostrar_menorHum(lista)
        case 2:
            temp_prom(lista)
        case 3:
            listar_variables(lista)
        case _:
            print('Error')

if __name__ == '__main__':
    dias = 30
    horas = 24
    lista = []
    for i in range(horas):
        lista.append([0] * dias)

    archivo = open("C:\\Users\\Andres\\Desktop\\Python\\Ejemplos practica\\Ejercicio 3\\Registros.csv")
    reader = csv.reader(archivo, delimiter = ';')
    band = True
    for i in reader:
        if band:
            band=False
        else:
           dia = int(i[0])
           hora = int(i[1])
           temp = i[2]
           humedad = i[3]
           presion = i[4]
           lista[hora][dia - 1] = Registro(temp, humedad, presion)
    menu(lista)
    archivo.close()


