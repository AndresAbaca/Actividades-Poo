class Ventana:
    __titulo = ''
    __xvsi = 0
    __yvsi = 0
    __xvid = 0
    __yvid = 0

    def __init__(self, titulo, x1 = 0, y1 = 0, x2 = 500, y2 = 500):
        self.__titulo = titulo
        self.__xvsi = x1
        self.__yvsi = y1
        self.__xvid = x2
        self.__yvid = y2
        
    def getTitulo(self):
        return self.__titulo

    def mostrar(self):
        print(f'Titulo: {self.__titulo}')
        print(f'Vertice superior: ({self.__x1}, {self.__y1})')
        print(f'Vertice inferior: ({self.__x2}, {self.__y2})')
    
    def alto(self):
        return self.__yvid - self.__yvsi
    
    def ancho(self):
        return self.__xvid - self.__xvsi

    def moverDerecha(self, n = 1):
        if self.__yvid + n <= 500:
            self.__xvsi += n
            self.__xvid += n
            print('ventana modificada')
        else:
            print('error')
    
    def moverIzquierda(self, n = 1):
        if self.__xvsi - n >= 0 :
            self.__xvsi -= n
            self.__xvid -= n
            print('ventana modificada')

        else:
            print('error')
    
    def bajar(self, n = 1):
        if self.__yvid + n <= 500:
            self.__yvsi += n
            self.__yvid += n

        else:
            print('error')

    def subir(self, n = 1):
        if self.__yvsi - n >= 0:
            self.__yvsi -= n
            self.__yvid -= n
        else:
            print('error')

