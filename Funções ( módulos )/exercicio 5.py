n = int(input("Informe um numero inteiro: "))

######################################################################################

def quantidade(x):
    q = x
    calculo = 0
    global cont
    cont = 0
    w = 0
    while x != 0:
        calculo = x % 10
        x = x // 10
        cont += 1

######################################################################################
 
    w = pow(10,cont-1)
    soma = 0
    while w != 0:
        calculo = q % 10
        cont = w * calculo
        soma += cont
        w = w // 10
        q = q // 10   
    return soma
        
a = quantidade(n)

print(a)
