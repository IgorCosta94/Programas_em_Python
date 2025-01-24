from dataclasses import dataclass
@dataclass



class regitem():
    item: str
    prox: int

lista = [regitem("Efetuar um saque no caixa",5),
        regitem("Comprar livros na livraria",3),
        regitem("Deixar o carro no estacionamento",7),
        regitem("Pegar as roupas na lavanderia",-1),
        regitem("Buscar encomenda no correio",0),
        regitem("Comprar presente",1),
        regitem("Autenticar documentos no cartório",4),
        regitem("Comprar calçados no shopping",6)]

comeco = 2
tarefa = lista[comeco]
i =1
print(f"Tarefa {i}: {tarefa.item}")
while tarefa.prox != -1:
    i += 1
    tarefa = lista[tarefa.prox]
    print(f"Tarefa {i}: {tarefa.item}")


