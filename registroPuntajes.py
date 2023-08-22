class nodoPuntaje ():
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
        self.siguiente = None

class listaPuntaje ():
    def __init__(self):
        self.cabeza = None
    
    def agregaPuntaje(self, nombre, puntaje):
        nuevoPuntaje = nodoPuntaje(nombre, puntaje)
        if not self.cabeza or puntaje > self.cabeza.puntaje:
            nuevoPuntaje.siguiente = self.cabeza
            self.cabeza = nuevoPuntaje
        else:
            actuactual = self.cabeza
            while actuactual.siguiente and puntaje <= actuactual.siguiente.puntaje:
                actuactual = actuactual.siguiente
            nuevoPuntaje.siguiente = actuactual.siguiente
            actuactual.siguiente = nuevoPuntaje
    
    def mostrarPuntaje (self):
        actual = self.cabeza
        while actual:
            print(f"Nombre: {actual.nombre}, Puntaje: {actual.puntaje}")
            actual = actual.siguiente

"""mejores = listaPuntaje()
mejores.agregaPuntaje("ling", 500)
mejores.agregaPuntaje("colmi", 470)
mejores.agregaPuntaje("cuernos", 501)

mejores.mostrarPuntaje()"""