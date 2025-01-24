print("\nPara encerrar digite 0 - Zero para sálario\n")
salario = int(input("Informe quanto salarios minimos você recebe: "))
n_dependentes = int (input("Informe quantos dependentes possui: "))
n_CPF = int(input("Informe o número do seu CPF: "))

while salario != 0:
    if salario <= 2:
        print("Você está isento. NÃO DEVE PAGAR!!!!")
    elif salario == 3:
        if n_dependentes > 0:
            salario = 1412 * salario
            x= ((0.05 * n_dependentes) * salario)
            aliquota = (salario - (x-(0.05 * salario)))
            print(f"Você deve pagar um valor de {aliquota}")
    elif salario == 4:
        if n_dependentes > 0:
            salario = 1412 * salario
            x= ((0.05 * n_dependentes) * salario)
            aliquota = salario - (x-(0.075 * salario))
            print(f"Você deve pagar um valor de {aliquota}")
    elif salario == 5:
        if n_dependentes > 0:
            salario = 1412 * salario
            x= ((0.05 * n_dependentes) * salario)
            aliquota = salario - (x-(0.10 * salario))
            print(f"Você deve pagar um valor de {aliquota}")
    elif salario == 6:
        if n_dependentes > 0:
            salario = 1412 * salario
            x= ((0.05 * n_dependentes) * salario)
            aliquota = salario - (x-(0.15 * salario))
            print(f"Você deve pagar um valor de {aliquota}")
    elif salario == 7:
        if n_dependentes > 0:
            salario = 1412 * salario
            x= ((0.05 * n_dependentes) * salario)
            aliquota = salario - (x-(0.20 * salario))
            print(f"Você deve pagar um valor de {aliquota}")

    print("\nPara encerrar digite 0 - Zero para sálario\n")
    salario = int(input("Informe quanto salarios minimos você recebe: "))
    n_dependentes = int (input("Informe quantos dependentes possui: "))
    n_CPF = int(input("Informe o número do seu CPF: "))
