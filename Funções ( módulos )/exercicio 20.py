def arredondamento(n,m):
    return round(n,m)


numero = float(input("Informe um numero fracionario para arredondamento: "))

casa = int(input("Informe o número de casas decimais arredondad: "))

print(f"O número {numero} arredondado com {casa} decimais é: {arredondamento(numero,casa)}")
