from dataclasses import dataclass

@dataclass
class cheque:
    data: str = ''
    valor: int = 0
    nome: str = ''



talao = [0] * 20
for x in range(20):
    talao[x] = cheque('', 0 ,'')

print(talao)    
    
