import matplotlib.pyplot as plt
import networkx as nx

class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioGrafico:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        self.raiz = self._insertar_rec(self.raiz, clave)

    def _insertar_rec(self, actual, clave):
        if actual is None:
            return Nodo(clave)
        if clave < actual.clave:
            actual.izquierdo = self._insertar_rec(actual.izquierdo, clave)
        elif clave > actual.clave:
            actual.derecho = self._insertar_rec(actual.derecho, clave)
        return actual

    def imprimir_sencillo(self):
        print(f"Raíz: {self.raiz.clave}")
        print(f"Hijos de 50 -> Izq: {self.raiz.izquierdo.clave} | Der: {self.raiz.derecho.clave}")
        print(f"Hijos de 30 -> Izq: {self.raiz.izquierdo.izquierdo.clave} | Der: {self.raiz.izquierdo.derecho.clave}")
        print(f"Hijos de 70 -> Izq: {self.raiz.derecho.izquierdo.clave} | Der: {self.raiz.derecho.derecho.clave}")

    def graficar(self):
        G = nx.DiGraph()
        posiciones = {}

        def agregar_nodos(nodo, x=0, y=0, nivel=1):
            if nodo is not None:
                G.add_node(nodo.clave)
                posiciones[nodo.clave] = (x, y)
                separacion = 1 / (2 ** nivel)
                
                if nodo.izquierdo:
                    G.add_edge(nodo.clave, nodo.izquierdo.clave)
                    agregar_nodos(nodo.izquierdo, x - separacion, y - 1, nivel + 1)
                if nodo.derecho:
                    G.add_edge(nodo.clave, nodo.derecho.clave)
                    agregar_nodos(nodo.derecho, x + separacion, y - 1, nivel + 1)

        agregar_nodos(self.raiz)

        plt.figure(figsize=(8, 6))
        nx.draw(
            G, 
            pos=posiciones, 
            with_labels=True, 
            node_size=2000, 
            node_color="skyblue", 
            font_size=12, 
            font_weight="bold", 
            arrowsize=15
        )
        plt.title("Árbol Binario de Búsqueda (ABB) Inicial")
        plt.savefig("arbol_inicial.png", format="PNG")
        print("¡Imagen 'arbol_inicial.png' guardada con éxito!")
        plt.show()

# Ejecución principal
if __name__ == "__main__":
    arbol = ArbolBinarioGrafico()
    for v in [50, 30, 20, 40, 70, 60, 80]:
        arbol.insertar(v)

    print("\n--- ESTRUCTURA DE NODOS ---")
    arbol.imprimir_sencillo()
    print("---------------------------\n")

    arbol.graficar()