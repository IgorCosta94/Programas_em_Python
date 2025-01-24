n = float(input("Informe o valor da prestação em atraso: "))

juros = n + (n*0.10)
desconto = juros - (juros * 0.10)


print(f"Juros da prestação: {juros} reais")
print(f"Valor final a pagar: {desconto} reais")
print(f"Prejuizo para o comerciante: {juros-desconto} reais")
