def mdc(a,b):
    x = a
    y = b
    mult = 1
    maximo = 1
    if a > b:
        for w in range(2,a+1,1):
            while  x % w == 0 or y % w == 0:
                if (x % w == 0)and (y % w == 0):
                    mult *= w
                    maximo *= w
                    x = x // w
                    y = y // w
                if (x % w == 0)and (y % w != 0):
                    mult *= w
                    x = x // w
                if (y % w == 0)and (x % w != 0):
                    mult *= w
                    y = y // w
            if x == 1 and y == 1:
                break

    else:
        for w in range(2,b+1,1):
            while  x % w == 0 or y % w == 0:
                if (x % w == 0)and (y % w == 0):
                    mult *= w
                    maximo *= w
                    x = x // w
                    y = y // w
                if (x % w == 0)and (y % w != 0):
                    mult *= w
                    x = x // w
                if (y % w == 0)and (x % w != 0):
                    mult *= w
                    y = y // w
            if x == 1 and y == 1:
                break
    print(f"O Máximo Divisor Comum - MDC de {a} e {b} é igual a: {maximo}")

n = int(input("Informe um número inteiro: "))

n2 = int(input("Informe outro número inteiro: "))

mdc(n,n2)
