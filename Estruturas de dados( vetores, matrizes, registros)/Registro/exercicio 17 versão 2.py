from dataclasses import dataclass
@dataclass
class agenda:
    dia: str
    hora: int
    nome: str
    telefone: int

horario = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

dados = [0] * 10
for w in range(0,10,1):
    dados[w] = agenda('',0,'',0)

for w in range(0,10,1):
    valor = 4
    valor2 = 4
    dados[w].nome = input("Informe o nome: ")
    dados[w].telefone = int(input("Informe o telefone: "))
    while ((valor != 0) and (valor2 != 0)):
        dados[w].dia = input("Informe o dia da consulta (segunda, terã, quarta, quinta, sexta): ")
        dados[w].hora = int(input("Informe a hora da consulta: "))

        if ((dados[w].dia == 'Segunda') or (dados[w].dia =='segunda')):   
            valor = 0
            d = 0
        elif ((dados[w].dia == 'Terça') or (dados[w].dia =='terça')):   
            valor = 0
            d = 1
        elif ((dados[w].dia == 'Quarta') or (dados[w].dia =='quarta')):   
            valor = 0
            d = 2
        elif ((dados[w].dia == 'Quinta') or (dados[w].dia =='quinta')):   
            valor = 0
            d = 3
        elif ((dados[w].dia == 'Sexta') or (dados[w].dia =='sexta')):   
            valor = 0
            d = 4
        else:
            print("Informe o DIA CORRETO")
            valor = 1

        if dados[w].hora == 14:
            valor2 = 0
            h = 0
        elif dados[w].hora == 15:
            valor2 = 0
            h = 1
        elif dados[w].hora == 16:
            valor2 = 0
            h = 2
        elif dados[w].hora == 17:
            valor2 = 0
            h = 3
        else:
            print("Informe a HORA CORRETA")
            valor2 = 1

        if horario[d][h] == 0:
            horario[d][h] = 1
            valor2 = 0
            print("\nHORÁRIO FOI RESERVADO COM SUCESSO\n")
        else:
            valor2 = 1
            print("\nHORÁRIO PARA ESTE DIA JÁ FOI RESERVADO\n")
            print("HORÁRIOS DISPONIVEIS")
            for x in range(0,5,1):
                for y in range(0,4,1):
                    if horario[x][y] == 0:
                        if x == 0:
                           d = 'segunda'
                        elif x == 1:
                            d = 'terça'
                        elif x == 2:
                            d = 'quarta'
                        elif x == 3:
                            d = 'quinta'
                        elif x == 4:
                            d = 'sexta'

                        if y == 0:
                           h = 14
                        elif y == 1:
                            h = 15
                        elif y == 2:
                            h = 16
                        elif y == 3:
                            h = 17
                    print(f"Dia {d} às {h} horas")

            
print(dados)
