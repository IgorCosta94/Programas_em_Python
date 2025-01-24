import pickle

from dataclasses import dataclass
@dataclass

class abaste:
    data: str
    quilometragem: float
    tipo_comb: str
    qtde_comb: float
    preco: float

#abastecimento = []

#data = input("Qaul a data do abastecimento? (-1 para terminar): ")

#while data != '-1':
 #   quilometragem = float(input("Qual a quilometragem? "))
 #   tipo_comb = input("Qual o tipo de combustivel? ")
 #   qtde_comb = float(input("Qual a quantidade do combustivel? "))
 #   preco = float(input("Qual o preço do combustivel? "))

 #   abastecimento.append(abaste(data, quilometragem ,tipo_comb ,qtde_comb ,preco))

 #   data = input("Qaul a data do abastecimento? (-1 para terminar): ")

#with open('abaste.pickle', 'wb') as arquivo:
 #   pickle.dump(abastecimento,arquivo)


with open('abaste.pickle','rb') as arquivo:
    lerabs = pickle.load(arquivo)

print("\nResumo dos abastecimentos\n")

for w in range(len(lerabs)):
    item = lerabs[w]
    print(f"abastecimento{w+1}\nData: {item.data}\nQuilometragem: {item.quilometragem}\n"
          f"Tipo de combustivel: {item.tipo_comb}\nQuantidade de litros: {item.qtde_comb}\nPreço: {item.preco}\n")
    
