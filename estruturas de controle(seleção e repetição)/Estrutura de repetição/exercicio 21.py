print(" -------------------------------------------------------")
print("|1,2,3,4 são os números para os respectivos canditado   |\n"
      "|5 para voto nulo                                       |\n"
      "|6 para voto em branco                                  |\n"
      "|0 para encerrar a votação                              |")
print(" -------------------------------------------------------")

total = 0
cand_1 = 0
cand_2 = 0
cand_3 = 0
cand_4 = 0
voto_b = 0

x = int(input("Informe seu voto: "))

while x != 0:
    if(x in range(0,7)):
        if(x == 1):
            cand_1 += 1
        elif(x == 2):
            cand_2 += 1
        elif(x == 3):
            cand_3 += 1
        elif(x == 4):
            cand_4 += 1
        elif(x == 6):
            voto_b += 1
   
        total += 1
        x = int(input("Informe seu voto: "))
    else:
        print("!!!!INFORME UM NÚMERO VALIDO")
        x = int(input("Informe seu voto: "))
print(f"TOTAL DE VOTO = {total}\n")
print(f"O canditado 1 teve um total de {cand_1} votos e um percentual de {(cand_1*100)//total}%")
print(f"O canditado 2 teve um total de {cand_2} votos e um percentual de {(cand_2*100)//total}%")
print(f"O canditado 3 teve um total de {cand_3} votos e um percentual de {(cand_3*100)//total}%")
print(f"O canditado 4 teve um total de {cand_4} votos e um percentual de {(cand_4*100)//total}%")
print(f"O número de votos em branco foi de {voto_b} e um  percentual de {(voto_b*100)//total}%")
