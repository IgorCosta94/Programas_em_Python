from dataclasses import dataclass
@dataclass

class pilha():
    pos: int
    nome: str
    prox: int

x = [0]*11
for w in range(10):

    if w > 0:
        x[w] = pilha(w,int(input("Nome: ")),w+1)
    else:
        x[w] = pilha(0,int(input("Nome: ")),1)
        
print(x)
print()
n = x[2].pos
print(x[n])
