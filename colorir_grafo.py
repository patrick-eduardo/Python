# -*- coding: utf-8 -*-
"""Grupo_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ceWemm92VQD2fD6FO-RjL78QnolO5OtL
"""

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import random
import copy

vertices = 6
arestas = 4 / (vertices-1)
E = nx.random_graphs.gnp_random_graph(n=vertices, p=arestas)
nx.draw(E,with_labels=False)

def retornar_menor_nao_presente(Grafo, vizinhos):
  lista_cores = []
  for v in vizinhos:
    lista_cores.append(Grafo.nodes[v]["Cor"])
  if len(lista_cores) == 0:
    return 1
  maximo = max(lista_cores)
  #+1 garante que a maior cor também esteja inclusa no vetor
  nova = list(range(1,maximo+1))

  i = 1

  while i < len(nova):
    #lista cores varia de 0 até k, onde k é o maior número da sequencia,
    #mas essa sequencia n é perfeita, isto é, ela pode ser 1,2,3,5,6
    if i not in lista_cores:
      return i
    i+=1

  return (i+1)


def definir_numero_cromatico(Grafo):
  nodes_nao_pintados = list(Grafo.nodes())
  maior_cor = 0
  for nodulo in nodes_nao_pintados:
    Grafo.nodes[nodulo]['Cor'] = 0

  for vazio in nodes_nao_pintados:
    vizinhos = Grafo.neighbors(vazio)
    cor_escolhida = retornar_menor_nao_presente(Grafo, vizinhos)
    if(maior_cor  < cor_escolhida):
      maior_cor = cor_escolhida
    Grafo.nodes[vazio]['Cor'] = cor_escolhida

  return (maior_cor,Grafo)

ret = definir_numero_cromatico(E)
print(ret[0])
novo=ret[1]

mapeamento_cores = {1: 'aquamarine', 2: 'orchid', 3: 'lightcoral', 4: 'gold', 5: 'violet', 6:'yellow'}

#Condição para exibir
if (len(mapeamento_cores) < (ret[0])):
  print("Impossível colorir, quantidade de cores necessárias indisponível.")

else:

#Pinta os vértices com base no atributo C usando o mapeamento de cores manual
  cores = [mapeamento_cores[novo.nodes[v]['Cor']] for v in novo.nodes()]
  nx.draw(novo, with_labels=False, node_color=cores)