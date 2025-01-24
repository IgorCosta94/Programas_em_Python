def quociente(w,x):
    cont = 0
    q =w
    while w > 1 and w > 0:
        w -= x
        cont += 1
        
    if cont * x == q:
        return cont
    elif cont * x > q:
        return cont - 1

n = int(input("Informe o numerador: "))

n1 = int(input("Informe o denominador: "))

print(f"O quociente da divisão de {n} por {n1} é {quociente(n,n1)}")
