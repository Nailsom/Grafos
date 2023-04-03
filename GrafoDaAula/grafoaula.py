import Grafo
#import CentroArvore

G = Grafo.GrafoListaAdj()

G.DefinirN(4)

e = G.AdicionarAresta(1, 2)
e.Custo = 3
e = G.AdicionarAresta(2, 3)
e.Custo = 1
e = G.AdicionarAresta(1, 3)
e.Custo = 2
e = G.AdicionarAresta(1, 4)
e.Custo = 4

for v in G.V():
  for no in G.N(v,IterarSobreNo=True):
    u = no.Viz
    print((v, u), no.e.Custo)