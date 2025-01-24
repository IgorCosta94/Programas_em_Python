from dataclasses import dataclass
@dataclass

class listas():
    ante: int
    item: str
    prox: int

x = [listas(0 ,"Efetuar um saque no caixa",1),
        listas(4,"Comprar livros na livraria",2),
        listas(1,"Deixar o carro no estacionamento",3),
        listas(2,"Pegar as roupas na lavanderia",4),
        listas(-1,"Buscar encomenda no correio",-1),
        listas(4,"Comprar presente",5),
        listas(5,"Autenticar documentos no cartório",7),
        listas(6,"Comprar calçados no shopping",0)]

comeco = 3
tarefa = x[comeco]
i =1
print(f"Tarefa {i}: {tarefa.item}")
while tarefa.ante != -1:
    i += 1
    
    tarefa = x[tarefa.ante]
    print(f"Tarefa {i}: {tarefa.item}")
