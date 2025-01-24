def fibo(numero):
    a = 1
    b = 1
    for w in range(3, numero + 1, 1):
        total = a + b
        a = b
        b = total

    print(total)

termo = int(input("Informe o número de termo que deseja saber a soma: "))

fibo(termo)
