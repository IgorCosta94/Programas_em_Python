peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))

imc = peso / (altura**2)

if imc < 18.5:
    print("Abaixo do peso")
else:
    if imc >= 18.5 and peso < 25.0:
        print("Peso normal")
    else:
        if imc >= 25.0 and peso < 30.0:
            print("Acima do peso")
        else:
            print("Obeso")
