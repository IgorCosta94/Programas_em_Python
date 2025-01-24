import json

nomearq = input("Nome do arquivo")

with open(nomearq, encoding = 'utf8') as arquivo:
    dic = json.load(arquivo)

print("\nLista de compras: ")
for chave, item in dic.items():
    print(f"{chave}: {item['qtde']} {item['unidade']} {item['item']}")
