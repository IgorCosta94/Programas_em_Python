def divisivel(numero):
    if numero % 6 == 0:
        print(f"O número {numero} é divisivel por 6")
    else:
        print(f"O número {numero} não é divisivel por 6")

n = int(input("Informe um número inteiro e descubra se ele é divisivel por 6: "))

divisivel(n)
