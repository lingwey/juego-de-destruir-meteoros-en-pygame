#limiteLista = 3
class nodoPuntaje ():
    
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
        self.siguiente = None

class listaPuntaje ():
    
    def __init__(self):
        self.cabeza = None
        self.limiteLista = 3
    
    def agregaPuntaje(self, nombre, puntaje):
        nuevoPuntaje = nodoPuntaje(nombre, puntaje)
        if not self.cabeza or puntaje > self.cabeza.puntaje:
            nuevoPuntaje.siguiente = self.cabeza
            self.cabeza = nuevoPuntaje
        else:
            actual = self.cabeza
            while actual.siguiente and puntaje <= actual.siguiente.puntaje:
                actual = actual.siguiente
            nuevoPuntaje.siguiente = actual.siguiente
            actual.siguiente = nuevoPuntaje
        #controla la longitud de la lista
        if self.__len__() > self.limiteLista:
            actual = self.cabeza
            for i in range (self.limiteLista - 1):
                actual = actual.siguiente
            actual.siguiente = None
        self.guardarPuntajes() 
        
    def mostrarPuntaje (self):
        actual = self.cabeza
        while actual:
            print(f"Nombre: {actual.nombre}, Puntaje: {actual.puntaje}")
            actual = actual.siguiente
    
    def __len__ (self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def guardarPuntajes (self):
        with open("records.txt", "w") as archivo:
            actual = self.cabeza
            while actual:
                archivo.write(f"{actual.nombre}, {actual.puntaje}\n")
                actual = actual.siguiente
    
    def leerPuntajes (self):
        try:
            with open("records.txt", "r") as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    record = linea.strip().split(", ")
                    nombre = record[0]
                    puntaje = int(record[1])
                    self.agregaPuntaje(nombre, puntaje)
        except FileNotFoundError:
            pass
            
       
            

"""mejores = listaPuntaje()
mejores.agregaPuntaje("ling", 500)
mejores.agregaPuntaje("colmi", 470)
mejores.agregaPuntaje("cuernos", 501)
mejores.agregaPuntaje("draakari", 521)

mejores.mostrarPuntaje()

mejores.agregaPuntaje("ling", 500)
mejores.agregaPuntaje("colmi", 760)
mejores.agregaPuntaje("cuernos", 501)
mejores.agregaPuntaje("draakari", 521)

mejores.mostrarPuntaje()"""
        