def primo(numero):
    if numero > 1 :
        cont = 0
        for w in range(1, numero + 1, 1):
            if numero % w == 0:
                cont += 1
        if cont == 2:
            print(f"O número {numero} é primo")
        else:
            print(f"O número {numero} não é primo")
    else:
        print(f"Tente da próxima!!!!\nE lembre-se, digite um número maior que 1")

n = int(input("Digite um número e descubra se ele é primo ou não: "))

primo(n)

