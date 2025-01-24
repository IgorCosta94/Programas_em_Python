import json

with open('a.json', encoding = 'utf8') as arquivo:
    a = json.load(arquivo)

for numcontato, dadoscontato in a.items():
    print(f"{dadoscontato['nome']}")
    print(f"    email: {dadoscontato['email']}")
    if dadoscontato['filhos'] is not None:
        print(f"    Filhos: {dadoscontato['filhos']}")
