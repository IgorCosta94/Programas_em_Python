import pickle

from dataclasses import dataclass
@dataclass

class abaste:
    data: str
    quilometragem: float
    tipo_comb: str
    qtde_comb: float
    preco: float

with open('abaste.pickle','rb') as arquivo:
    ler = pickle.load(arquivo)

print("\n RELATÓRIO")

for w in range(len(ler)-1):
    item = ler[w]
    item2 = ler[w+1]
    diferenca = round(item.preco - item2.preco,2)
    consumo_atual = round((item.quilometragem / item.qtde_comb),2)
    consumo_ante = round((item.quilometragem / item.qtde_comb) - (item2.quilometragem / item2.qtde_comb),2)
    print(f"Abastecimento {w+1}\nDiferença de preço: {diferenca}\nConsumo atual: {consumo_atual}\nConsumo anterior: {consumo_ante}")

