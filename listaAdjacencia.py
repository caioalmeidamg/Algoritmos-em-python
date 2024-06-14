class grafo:

    def __init__(self, listaTuplas, bidirecional=False) -> None:
        self.listaAdjacencia = {}
        self.arestas = listaTuplas
        self.bidirecional: bool = bidirecional

        for aresta in self.arestas:
            if aresta.v1() not in self.listaAdjacencia:
                self.listaAdjacencia[aresta.v1()] = []
            if aresta.v2() not in self.listaAdjacencia:
                self.listaAdjacencia[aresta.v2()] = []

        for aresta in self.arestas:
            self.listaAdjacencia[aresta.v1()].append(aresta.v2())
            if self.bidirecional:
                self.listaAdjacencia[aresta.v2()].append(aresta.v1())        

    def retornaGrafo(self):
        return self.listaAdjacencia

    def imprimeGrafo(self):
        for vertice, adjacentes in self.listaAdjacencia.items():
            print(f"{vertice}: {adjacentes}")



class tupla:
    def __init__(self, numero1, numero2) -> None:
        self.origem: int = numero1
        self.destino: int = numero2

    def v1(self):
        return self.origem
    
    def v2(self):
        return self.destino
    
listadeTuplas = [
    tupla(1,2),
    tupla(2,3),
    tupla(3,4),
    tupla(4,5),
    tupla(5,1)
]

grafo(listadeTuplas).imprimeGrafo()




















# def criar_grafo():
#     return {}

# def adicionar_vertice(grafo, vertice):
#     if vertice not in grafo:
#         grafo[vertice] = []

# # Se o grafo for não-direcionado
# def adicionar_aresta(grafo, vertice1, vertice2):
#     if vertice1 not in grafo:
#         adicionar_vertice(grafo, vertice1)
#     if vertice2 not in grafo:
#         adicionar_vertice(grafo, vertice2)
#     grafo[vertice1].append(vertice2)
#     grafo[vertice2].append(vertice1) 

# def exibir_grafo(grafo):
#     print("Lista de Adjacência do Grafo:")
#     for vertice, adjacentes in grafo.items():
#         print(f"{vertice}: {adjacentes}")

# # Uso das funções
# grafo = criar_grafo()

# # Adicionando vértices e arestas dinamicamente
# adicionar_vertice(grafo, 'A')
# adicionar_vertice(grafo, 'B')
# adicionar_aresta(grafo, 'A', 'C')
# adicionar_aresta(grafo, 'B', 'D')
# adicionar_aresta(grafo, 'A', 'B')
# adicionar_aresta(grafo, 'C', 'D')

# # Exibindo o grafo
# exibir_grafo(grafo)



