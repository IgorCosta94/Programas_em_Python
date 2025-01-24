from dataclasses import dataclass

@dataclass

class algoritimo():
    nome: str
    prox: int

fila = [algoritimo("José",1),
        algoritimo("joão",2),
        algoritimo("Ciclano",3),
        algoritimo("beltrano",0)
        ]

comeco = 1

cont = fila[comeco]
i = 1

while i<=20:
    cont = fila[cont.prox]
    print(f"Nome{i}: {cont.nome}")
    if((i % 4) == 0):
        print()
    i += 1
