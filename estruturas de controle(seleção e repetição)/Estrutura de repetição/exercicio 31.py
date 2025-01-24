sexo = input("Informe o sexo. 'M'- masculino ou 'F' - feminino")
olhos = input("Informe a cor dos olhos. 'A'- Azuis, 'V' - verdes, ou 'C' - castanhos")
cabelos = input("Informe a cor do cabelo. 'L' - loiros, 'C' - castanhos, 'P' - pretos")
idade = int(input("Informe a idade: "))
print("\nPara terminar digite -1 para idade\n")

acum_ih = 0
acum_H = 0
acum_TH = 0
acum_T = 0
acum_M = 0

while idade != -1:
    if idade > acum_ih:
        acum_ih = idade
        
    if sexo == 'M':
        acum_TH += 1
        if idade >= 18 or idade <= 35:
            acum_H += 1
    elif sexo == 'F':
        if olhos == 'V' and cabelos == 'L':
            acum_M += 1
            
    acum_T += 1
    
    sexo = input("Informe o sexo. 'M'- masculino ou 'F' - feminino")
    olhos = input("Informe a cor dos olhos. 'A'- Azuis, 'V' - verdes, ou 'C' - castanhos")
    cabelos = input("Informe a cor do cabelo. 'L' - loiros, 'C' - castanhos, 'P' - pretos")
    idade = int(input("Informe a idade: "))
    
##############################################################################################################################################
    
print(f"A maior idade entre os habitantes é igual a: {acum_ih}")
print(f"A porcentagem entre os homens com idade entre 18 e 35 anos é: {(acum_H * 100) /acum_TH}")
print(f"A porcentagem do total de indivíduos do sexo feminino entre 18 e 35,\ne com olhos verdes e cabelos loiros: {(acum_M * 100) / acum_T}")
