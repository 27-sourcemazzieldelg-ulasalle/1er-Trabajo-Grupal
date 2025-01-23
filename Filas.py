class Node:
    def __init__(self):
        self.objeto = None
        self.siguiente = None

class Pila:
    def __init__(self):
        self.ultimo = None

    def apilar(self, objeto):
        nodo = Node()
        nodo.objeto = objeto
        nodo.siguiente = self.ultimo
        self.ultimo = nodo

    def borrar(self, objeto):
      if self.ultimo is None:  # caso especial si la pila esta vacia
          return None
      
      if self.ultimo.objeto == objeto:  # Si el objeto a borrar está en el último nodo
          self.ultimo = self.ultimo.siguiente  # El nuevo último nodo es el siguiente es decir none
          return  # Salir de la función
      
      nodo_actual = self.ultimo
      nodo_anterior = None  # Nodo anterior al nodo actual
      
      while nodo_actual is not None and nodo_actual.objeto != objeto:  # mientras no este vacio y el nodo sea diferente del objeto(numero)
          nodo_anterior = nodo_actual
          nodo_actual = nodo_actual.siguiente
      
      if nodo_actual is not None:  # Si se encontró el nodo
          nodo_anterior.siguiente = nodo_actual.siguiente  # Enlazar el nodo anterior con el siguiente del nodo a borrar
      else:
          print("Objeto no encontrado en la pila")  # Mensaje si el objeto no está en la pila

    def buscar(self,objeto):
      contador = 0
      if self.ultimo is None:
          return None
      else:
          nodo = self.ultimo
          while nodo is not None:
            contador += 1
            if nodo.objeto == objeto:
                print(f"Se encontra el objeto =",objeto,"en el nodo",contador -1)    
                return nodo
            nodo = nodo.siguiente
          return None

    def desapilar(self):  # Es la forma de sacar un elemento de la pila, tomando en cuenta el principio LIFO
        if self.ultimo is None:
            return None
        else:
            objeto = self.ultimo.objeto
            self.ultimo = self.ultimo.siguiente
            return objeto

    def imprimir_pila(self): #Metodo para imprimir la pila
      nodo_actual = self.ultimo
      while nodo_actual is not None:
          print(nodo_actual.objeto, end=" -> ")
          nodo_actual = nodo_actual.siguiente
      print("None")


pila = Pila()

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numeros:
    pila.apilar(i)

pila.buscar(5)

pila.imprimir_pila()

pila.borrar(4)

pila.imprimir_pila()
