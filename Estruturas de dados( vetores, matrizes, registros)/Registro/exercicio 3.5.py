from dataclasses import dataclass
@dataclass
class ingresso:
    lugar: int
    tipo_ingresso: str
    idade: int

lugares = [0] * 140
assentos = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
            [15,16,17,18,19,20,21,22,23,24,25,26,27,28],
            [29,30,31,32,33,34,35,36,37,38,39,40,41,42],
            [43,44,45,46,47,48,49,50,51,52,53,54,55,56],
            [57,58,59,60,61,62,63,64,65,66,67,68,69,70],
            [71,72,73,74,75,76,77,78,79,80,81,82,83,84],
            [85,86,87,88,89,90,91,92,93,94,95,96,97,98],
            [99,100,101,102,103,104,105,106,107,108,109,110,111,112],
            [113,114,115,116,117,118,119,120,121,122,123,124,125,126],
            [127,128,129,130,131,132,133,134,135,136,137,138,139,140]]

cont_m = 0
cont_i = 0
cont_12 = 0
cont_18 = 0
cont_maior = 0
for x in range(6):
    lugares[x] = ingresso(0, '' ,0)
    lugares[x].lugar =int(input("Informe o número do lugar: ")) 
    lugares[x].tipo_ingresso = input("Informe o tipo de ingresso('M'- meia entrada ou 'I' inteira)")
    lugares[x].idade = int(input("Informe a idade: "))
        
    if lugares[x].tipo_ingresso == 'M' or lugares[x].tipo_ingresso == 'm':
        cont_m += 1
    elif lugares[x].tipo_ingresso == 'I' or lugares[x].tipo_ingresso == 'i':
        cont_i += 1

    if  lugares[x].idade < 12:
        cont_12 += 1
    elif  lugares[x].idade > 12 and  lugares[x].idade < 18:
        cont_18 += 1
    elif  lugares[x].idade > 18:
        cont_maior += 1
            
    for i in range(0,10,1):
        for y in range(0,14,1):
            if lugares[x].lugar == assentos[i][y]:
                 assentos[i][y] =  '#'
    
print(assentos)
for x in range(6):
    print(lugares[x])

print(f"Quantidade de menores de 12 anos: {cont_12}\nQuantidade de menores de 18 anos: {cont_18}\nQuantidade de maiores de idade: {cont_maior}")
print(f"Quantidade de meia entrada: {cont_m}\nQuantidade de entrada inteira: {cont_i}")
print(assentos)
     

