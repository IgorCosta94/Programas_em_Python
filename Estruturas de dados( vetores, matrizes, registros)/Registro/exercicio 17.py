from dataclasses import dataclass
@dataclass
class agenda:
    dia: str
    hora: int
    mes: str
    nome: str
    telefone: int

horario = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

dados = [0] * 10
for w in range(0,10,1):
    dia = input("informe o dia da consulta: ")
    hora = input("Informe o horário da consulta: ")

    if((dia == 'segunda') or (dia == 'Segunda')):
        d = 0
    elif((dia == 'terça') or (dia == 'Terça')):
        d = 1
    elif((dia == 'quarta') or (dia == 'Quarta')):
        d = 2
    elif((dia == 'quinta') or (dia == 'Quinta')):
        d = 3
    elif((dia == 'sexta') or (dia == 'Sexta')):
        d = 4
    else:
        print("Informe o dia correto -> Segunda, Terça, Quarta, Quinta, Sexta")

    if(hora == 14):
        h = 0
    elif(hora == 15):
        h = 1
    elif(hora == 16):
        h = 2
    elif(hora == 17):
        h = 3
    
    if(horario[d][h] == 0):
        horario[d][h] = 1
    else:
        print("Horario disponivel:")
        for x in range(0,5,1):
            for y in range(0,4,1):
                if horario[x][y] == 0:
                    if((x == 0): 
                        d = 'Segunda'
                    elif((x == 1): 
                        d = 'Terça'
                    elif((x == 2): 
                        d = 'Quarta'
                    elif((x == 3): 
                        d = 'Quinta'
                    elif((x == 4): 
                        d = 'Sexta'
                        

                    if(y == 0):
                        h = 14
                    elif(y == 1):
                        h = 15
                    elif(y == 2):
                        h = 16
                    elif(y == 3):
                        h = 17
                    print(f"Dia: {d}||Horário: {h}")


    
