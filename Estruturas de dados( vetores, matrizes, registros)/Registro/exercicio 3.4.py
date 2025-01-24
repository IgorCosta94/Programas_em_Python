from dataclasses import dataclass
@dataclass
class produto:
    nome: str 
    codigo: int 
    preco: float 
    baixa: list

estoque = [0] * 50

for x in range(50):
    estoque[x] = produto('',0,0.0,[0] * 6)
    estoque[x].nome = input("Qual o nome: ")
    estoque[x].preco = float(input("Qual o nome: "))

    for y in range(6):
        estoque[x].baixa[y] = 0
        
    print(estoque[x])

