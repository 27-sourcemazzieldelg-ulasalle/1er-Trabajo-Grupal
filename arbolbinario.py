class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None  # Hijo izquierdo (numeros menores)
        self.derecho = None  # Hijo derecho (numeros mayores)

class ArbolBinario:
    def __init__(self):
        self.raiz = None  # La raíz del árbol

    def insertar(self, valor):
        # Si el árbol está vacío, el primer nodo será la raíz
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            # De lo contrario, llamamos al metodo _Insertar_en
            self._insertar_en(self.raiz, valor)

    def _insertar_en(self, nodo, valor):
        # Método auxiliar que recursivamente coloca el nodo en la posición adecuada
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_en(nodo.izquierdo, valor) #si el nodo no esta vacio, llamamos a la funcion recursiva
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_en(nodo.derecho, valor)

    def recorrer_inorden(self, nodo):
        if nodo is not None:
            self.recorrer_inorden(nodo.izquierdo)
            print(nodo.valor, end=" -> ")
            self.recorrer_inorden(nodo.derecho)

    def mostrar(self):
        print("Recorrido Inorden: ", end="")
        self.recorrer_inorden(self.raiz)
        print()

    def buscar(self, valor):
      return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)

    def borrar(self, valor):
        self.raiz = self._borrar_recursivo(self.raiz, valor)

    def _borrar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierdo = self._borrar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._borrar_recursivo(nodo.derecho, valor)
        else:
            # Caso 1: Nodo sin hijos o con un solo hijo
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

            # Caso 2: Nodo con dos hijos
            # Encontrar el sucesor inorden (el nodo más pequeño en el subárbol derecho)
            sucesor = self._minimo_valor_nodo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._borrar_recursivo(nodo.derecho, sucesor.valor)

        return nodo

    def _minimo_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

# Crear el árbol binario 
arbol = ArbolBinario()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(2)
arbol.insertar(8)
arbol.insertar(20)

# Mostrar el recorrido inorden del árbol
arbol.mostrar()

nodo_buscado = arbol.buscar(8)
if nodo_buscado:
    print("Valor encontrado:", nodo_buscado.valor)
else:
    print("Valor no encontrado")

arbol.borrar(15)  

arbol.mostrar()