from dataclasses import dataclass
@dataclass

class listas():
    item: str
    prox: int

x = [listas("Efetuar um saque no caixa",4),
        listas("Comprar livros na livraria",2),
        listas("Deixar o carro no estacionamento",3),
        listas("Pegar as roupas na lavanderia",5),
        listas("Buscar encomenda no correio",-1),
        listas("Comprar presente",6),
        listas("Autenticar documentos no cartório",7),
        listas("Comprar calçados no shopping",0)]

comeco = 2
tarefa = x[comeco]
i =1
print(f"Tarefa {i}: {tarefa.item}")
while tarefa.prox != -1:
    i += 1
    tarefa = x[tarefa.prox]
    print(f"Tarefa {i}: {tarefa.item}")
