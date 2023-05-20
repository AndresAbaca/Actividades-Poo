class Conjunto:
    __conjunto=set() 
    def __init__(self, lista):  
        self.__conjunto = set(lista)
    
    def getConjunto(self): 
        return self.__conjunto

    def __add__(self,otroConjunto):                                              
        return Conjunto( self.__conjunto.union( otroConjunto.getConjunto() ) )  
    
    def __sub__(self,otroConjunto):
        return Conjunto( self.__conjunto - otroConjunto.getConjunto())  
    
    def __eq__(self, otroConjunto):                                   
        return  ( self.__conjunto == otroConjunto.getConjunto())


    def MenuOpciones():
        print()
        print(" // Menu de Opciones // ")    
        print("presione 1 | Mostrar Conjuntos Disponibles")
        print("presione 2 | Union de 2 Conjuntos")
        print("presione 3 | Diferencia entre 2 Conjuntos")
        print("presione 4 | Igualdad de 2 conjuntos")
        print("presione 0 | Para salir")
        
        
    def Menu(C1,C2,C3):
       MenuOpciones
       op=int(input("Ingrese una opcion: "))
       print()
       while op != 0:
           if op == 1:
               print("Conjunto A = {}".format(C1.getConjunto()))
               print("Conjunto B = {}".format(C2.getConjunto()))
               print("Conjunto C = {}".format(C3.getConjunto()))
            
           elif op == 2:
            c1=str(input("Ingrese el primer conjunto a operar: "))
            c2=str(input("Ingrese el segundo conjunto a operar: "))
            if (c1 == "A" or c1=="B" or c1=="C") and (c2=="A" or c2=="B" or c2=="C"):
                if (c1 == "A" and c2 == "B") or (c1 == "B" and c2 == "A"):
                    suma = C1 + C2
                    print("La Suma entre A y B es: ", suma.getConjunto())
                elif (c1 == "A" and c2 == "C") or (c1 == "C" and c2 == "A"):
                    suma = C1 + C3
                    print("La Suma entre A y C es: ", suma.getConjunto())
                elif (c1 == "B" and c2 == "C") or (c1 == "C" and c2 == "B"):
                    suma = C2 + C3
                    print("La Suma entre B y C es: ", suma.getConjunto())
            else:
                print("Error en Selecionar los Conjuntos!")
                
           elif op == 3:  
                 c1=str(input("Ingrese el primer conjunto a operar: "))
                 c2=str(input("Ingrese el segundo conjunto a operar: "))
           if (c1 == "A" or c1=="B" or c1=="C") and (c2=="A" or c2=="B" or c2=="C"):
                if c1 == "A" and c2 == "B":
                    resta = C1 - C2
                    print("La Resta entre A y B es: ", resta.getConjunto())
                elif c1 == "A" and c2 == "C":
                    resta = C1 - C3
                    print("La Resta entre A y C es: ", resta.getConjunto())
                elif c1 == "B" and c2 == "C":
                    resta = C2 - C3
                    print("La Resta entre B y C es: ", resta.getConjunto())
                elif c1 == "B" and c2 == "A":
                    resta = C2 - C1
                    print("La Resta entre B y A es: ", resta.getConjunto())
                elif c1 == "C" and c2 == "A":
                    resta = C3 - C1
                    print("La Resta entre C y A es: ", resta.getConjunto())
                elif c1 == "C" and c2 == "B":
                    resta = C3 - C2
                    print("La Resta entre C y B es: ", resta.getConjunto())
                       
           elif op == 4:
            c1=str(input("Ingrese el primer conjunto: "))
            c2=str(input("Ingrese el segundo conjunto: "))
            if (c1 == "A" or c1=="B" or c1=="C") and (c2=="A" or c2=="B" or c2=="C"):
                if (c1 == "A" and c2 == "B") or (c1 == "B" and c2 == "A"):
                    print("Son Iguales los Conjuntos A y B: ", C1 == C2)
                elif (c1 == "A" and c2 == "C") or (c1 == "C" and c2 == "A"):
                    print("Son Iguales los Conjuntos A y C: ", C1 == C3)
                elif (c1 == "B" and c2 == "C") or (c1 == "C" and c2 == "B"):
                    print("Son Iguales los Conjuntos B y C: ", C2 == C3)
            else:
                print("Error los conjuntos no se pueden operar")
           else:
            print("Opcion Incorrecta")
           if op != 0:
               MenuOpciones()
               op=int(input("Ingrese una opcion:  "))
               print()
    print("Finalizando......")