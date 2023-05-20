import ClaseConjunto as ClaseConjunto
import Menu as menu
    
if __name__ == "__main__":              
   A = ClaseConjunto.Conjunto([1,2,3,4])
   B = ClaseConjunto.Conjunto([3,6,9])
   C = ClaseConjunto.Conjunto([1,4,3,2])
   menu.Menu(A,B,C)