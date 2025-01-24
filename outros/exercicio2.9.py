n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))

operacao = input("Qual a operação desejada(+ , - , * , /): ")

if operacao == "+":
    calculo = n1 + n2
elif operacao == "-":
    calculo = n1 - n2
elif operacao == "*":
    calculo = n1 * n2
elif operacao == "/":
    calculo = n1 / n2

print(calculo)
