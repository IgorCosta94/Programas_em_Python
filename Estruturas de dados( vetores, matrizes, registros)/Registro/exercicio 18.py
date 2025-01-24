from dataclasses import dataclass
@dataclass
class registro:
    proprietario: str
    combustivel:  str
    modelo:       str
    cor:          str
    ano:          int
    plc:          str
    plc2:         int

reg = [0] * 21


for w in range(1,5):
    reg[w] = registro('','','','',0,'',0)

for w in range(1,5):
    reg[w].proprietario = input("Informe o nome do proprietario: ")
    reg[w].combustivel  = input("Informe o tipo de combustível: ")
    reg[w].modelo = input("Informe o modelo do carro: ")
    reg[w].cor = input("Informe a cor do carro: ")
    reg[w].ano = int(input("Informe o ano do carro: "))
    reg[w].plc = input("Informe os três primeiros valores alfabéticos da placa: ")
    reg[w].plc2 = input("Informe os quatro últimos valores númericos da placa: ")
    print()
    

print("\nLista de proprietário com carros dos anos 2000 ou anterior e com vaga ocupada\n")

for w in range(1,5):
    if reg[w].ano <= 2000:
        if reg[w].combustivel == 'flex' or reg[w].combustivel == 'Flex':
            print(f"Nome do proprietário: {reg[w].proprietario}\n"
                  f"Placa: {reg[w].plc}-{reg[w].plc2}\n"
                  f"Vaga: {w}")
            
for w in range(1,4):
    for x in range(w+1,5):
        ordem = reg[w]
        if reg[w].ano < reg[x].ano:
            reg[w] = reg[x]
            reg[x] = ordem
print()

print("Lista de carros em ordem descendente por Ano:")

for w in range(1,5):
    print(f"Ano:          {reg[w].ano}\n"
          f"Modelo:       {reg[w].modelo}\n"
          f"Placa:        {reg[w].plc}-{reg[w].plc2}\n"
          f"Cor:          {reg[w].cor}\n"
          f"Proprietário: {reg[w].proprietario}\n"
          f"Vaga:         {w}")

    
print()

print("Deseja realizar a troca de veículo? Digite 1 para SIM e 0 - para NÃO")
print()
#valor = int(input("Informe o valor: ""\n"))
while int(input("Informe o valor: ")) != 0:
    vaga = int(input("Informe a vaga  a ser trocada: "))
    print("Informe as novas informações\n")
          
    reg[vaga].proprietario = input("Informe o nome do proprietario: ")
    reg[vaga].combustivel  = input("Informe o tipo de combustível: ")
    reg[vaga].modelo = input("Informe o modelo do carro: ")
    reg[vaga].cor = input("Informe a cor do carro: ")
    reg[vaga].ano = int(input("Informe o ano do carro: "))
    reg[vaga].plc = input("Informe os três primeiros valores alfabéticos da placa: ")
    reg[vaga].plc2 = input("Informe os quatro últimos valores númericos da placa: ")         
          

















print(reg)
