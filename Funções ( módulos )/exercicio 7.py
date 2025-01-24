def resto(w,x):
    cont = 0
    q = w
    while w > 1 and w > 0:
        w -= x
        cont += 1

    if cont * x == w:
        return w
    elif cont * x > w:
        return (cont * x) - q

n = int(input("Informe o numerador: "))

n1 = int(input("Informe o denominador: "))

print(f"O resto da divisão de {n} por {n1} é {resto(n,n1)}")
