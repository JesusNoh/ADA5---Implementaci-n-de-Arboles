class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def es_vacio(self):
        return self.raiz is None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        elif valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._minimo_valor(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, temp.valor)
        return nodo

    def _minimo_valor(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo

    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        izquierda = self.altura(nodo.izquierda)
        derecha = self.altura(nodo.derecha)
        return max(izquierda, derecha) + 1

    def cantidad_hojas(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return self.cantidad_hojas(nodo.izquierda) + self.cantidad_hojas(nodo.derecha)

    def cantidad_nodos(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        return 1 + self.cantidad_nodos(nodo.izquierda) + self.cantidad_nodos(nodo.derecha)

    def mostrar_arbol_completo(self):
        self._mostrar_arbol_recursivo(self.raiz)

    def _mostrar_arbol_recursivo(self, nodo, nivel=0):
        if nodo is not None:
            self._mostrar_arbol_recursivo(nodo.derecha, nivel + 1)
            print(' ' * 4 * nivel + '->', nodo.valor)
            self._mostrar_arbol_recursivo(nodo.izquierda, nivel + 1)

    def recorrer_preorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is not None:
            print(nodo.valor, end=' ')
            self.recorrer_preorden(nodo.izquierda)
            self.recorrer_preorden(nodo.derecha)

    def recorrer_inorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is not None:
            self.recorrer_inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.recorrer_inorden(nodo.derecha)

    def recorrer_postorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is not None:
            self.recorrer_postorden(nodo.izquierda)
            self.recorrer_postorden(nodo.derecha)
            print(nodo.valor, end=" ")

    def recorrer_por_niveles(self):
        if self.raiz is None:
            return
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            print(nodo.valor, end=" ")
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)

if __name__ == "__main__":
    print("Iniciando la creación del árbol...")
    arbol = Arbol()

    arbol.insertar(50)
    arbol.insertar(30)
    arbol.insertar(70)
    arbol.insertar(20)
    arbol.insertar(40)
    arbol.insertar(60)
    arbol.insertar(80)
    print("Prueba de inserciones completa.")

    print("Árbol completo:")
    arbol.mostrar_arbol_completo()

    print("\nRecorridos del árbol:")
    print("PreOrden:")
    arbol.recorrer_preorden()
    print("\nInOrden:")
    arbol.recorrer_inorden()
    print("\nPostOrden:")
    arbol.recorrer_postorden()
    print("\nPor niveles:")
    arbol.recorrer_por_niveles()

    print(f"\n\nAltura del árbol: {arbol.altura()}")

    print(f"Cantidad de hojas: {arbol.cantidad_hojas()}")

    print(f"Cantidad de nodos: {arbol.cantidad_nodos()}")
