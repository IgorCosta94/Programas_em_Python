from dataclasses import dataclass
@dataclass

class vinho:
    produto: str
    casta: str
    safra:str

x = []

def novos(x):
    for w in range(0,10,1):
        produto = input("Informe o nome do produto: ")
        casta = input("Informe o nome da casta: ")
        safra = input("Informe o nome da safra: ")
        x.append(vinho(produto,casta,safra))
    ocasiao(x)
    

def ocasiao(x):
    print()
    print(f"O vinho que deve ser aberto na ocasião especial é: {x[len(x)-1]}")
    ultimos5(x)

def ultimos5(x):
    print()
    print("Os últimos cincos mais antigos são")
    for w in range(5):
        print(x.pop())
        
novos(x)
