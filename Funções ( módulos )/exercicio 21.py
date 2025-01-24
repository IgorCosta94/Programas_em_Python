def digitacao():
    a = [0] * 10
    for w in range(0,10,1):
        a[w] = int(input("Informe os valores inteiros para o vetor: "))
    print()
    soma(a)
    
def soma (x):
    total = 0
    for w in range(0,len(x),1):
        total += x[w]
    print(f"Soma: {total}")
    print()
    media(total,x)
    
def media(y,z):
    valor = y / len(z)
    print(f"Média: {valor}")
    print()
    desvio(valor,z)

def desvio(x,y):
    dp = 0
    for w in range(0,len(y),1):
        dp += pow(y[w]-x,2)
    dp = dp / len(y)
    print(f"Desvio Padrão: {dp}")
    print()
    sub(y)

def sub(x):
    for w in range(0,len(x),1):
        if x[w] < 0:
            x[w] = 0
    for a in range(0,len(x),1):
        for b in range(a+1,len(x),1):
            if x[a] == x[b]:
                x[b] = 0
    print()        
    print(x)
    
digitacao()
