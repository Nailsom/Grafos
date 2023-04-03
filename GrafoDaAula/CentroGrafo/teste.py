from Grafo import GrafoListaAdj
from CentroArvore import CentroArvore

G = GrafoListaAdj(orientado = False)

G.DefinirN(5, VizinhancaDuplamenteLigada = True)

e = G.AdicionarAresta(1,2)
e = G.AdicionarAresta(1,3)
e = G.AdicionarAresta(1,4)
e = G.AdicionarAresta(1,5)

c = CentroArvore(G)

print("O centro da Arvore é: ", c)