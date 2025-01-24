n = int(input("Informe um numero inteiro: "))

######################################################################################

def quantidade(x):
    s = x
    calculo = 0
    global cont
    cont = 0
    w = 0
    while x != 0:
        calculo = x % 10
        x = x // 10
        cont += 1
    inverso(s,cont)
    
######################################################################################

def inverso(q,m):
    v=q
    w = pow(10,m-1)
    soma = 0
    while w != 0:
        calculo = q % 10
        cont = w * calculo
        soma += cont
        w = w // 10
        q = q // 10
    soma = soma + v
    print(soma)
    inverso2(soma)

#########################################################################################
    
def inverso2(r):
    x = r
    soma = 0
    cont = 0
    
    while x != 0:
        calculo = x % 10
        x = x // 10
        cont += 1
        
    while cont > 0:
        calculo = (r % 10) * cont
        soma +=calculo
        cont -= 1
        r = r // 10
    print(f"O digito verificador corresponde ao seguinte valor: {soma}")
        
quantidade(n)

######################################################################################
