x1 = int(input("Digite o primeiro numero: "))
x2 = int(input("Digite o segundo  numero: "))

numero1 = x1
numero2 = x2

div1 = 0
div2 = 0

divisor = 2

contador1 = 1


while((x1 != 1) or (x2 != 1)):
    div1 = x1 % divisor
    div2 = x2 % divisor
    
    if ((div1 == 0) and (div2 == 0)):
        contador1 = contador1 * divisor
        x1 = x1 // divisor
        x2 = x2 // divisor
    elif(div1 == 0):
        contador1 = contador1 * divisor
        x1 = x1 // divisor
    elif(div2 == 0):
        contador1 = contador1 * divisor
        x2 = x2 // divisor
    else:
        divisor += 1   


print(f"\nO Mínimo Múltiplo Comum - MMC entre {numero1} e {numero2} é igual a {contador1}")
