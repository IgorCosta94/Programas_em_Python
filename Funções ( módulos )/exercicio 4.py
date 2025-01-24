n = int(input("Informe um numero inteiro: "))

def quantidade(x):
    calculo = 0
    global cont
    cont = 0
    while x != 0:
        calculo = x % 10
        x = x // 10
        cont += 1
    return cont
        
a = quantidade(n)

print(a)



    
    
