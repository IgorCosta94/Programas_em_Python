from dataclasses import dataclass
@dataclass
class passageiro:
    n_passagem: int = 0
    data: str = ''
    origem:  str = ''
    destino:  str = ''
    horario:  str = ''
    poltrona: int = 0
    idade: int = 0
    nome: str = ''


media = 0
y = [0] * 44
for x in range(44):
    y[x] = passageiro(0 , '' , '' , '' , '' , 0 , 18 ,'A')
    media += y[x].idade

media = media /44
print(media)

for x in range(44):
    if y[x].idade >= media:
        print(y[x].nome)

