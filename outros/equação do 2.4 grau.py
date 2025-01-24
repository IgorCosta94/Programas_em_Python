altura = float(input("Informe sua altura: "))
sexo = input("Informe o sexo.(H) para homens e (M) para mulheres: ")

if (sexo == "H") or (sexo == "h"):
    calculo = (72.7*altura)-58
    print(f"O peso ideal para homens é {calculo}")
else:
    calculo = (62.1*altura)-44.7
    print(f"O peso ideal para mulheres é {calculo}")
