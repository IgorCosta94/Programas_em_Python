x1 = float(input("Digite o valor do primeiro ponto P(x1): "))
y1 = float(input("Digite o valor do segundo ponto P(y1): "))

x2 = float(input("Digite o valor do primeiro ponto Q(x2): "))
y2 = float(input("Digite o valor do segundo ponto Q(y2): "))

primeira_parte = ((x2 - x1)**2) + ((y2 - y1)**2)
segunda_parte = primeira_parte**0.5

print(f"A distancia entre os pontos é de: {segunda_parte}")
