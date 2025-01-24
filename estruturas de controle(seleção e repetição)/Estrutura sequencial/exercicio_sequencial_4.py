cap_tanque = int(input("Informe a capacidade do tanque: "))

qtde_abastecida = float(input("Informe a quantidade abastecida: "))

km_percorrida = float(input("Informe a kilometragem percorrida: "))

qtde_antes_abastecimento = 15.0

consumo = cap_tanque - qtde_abastecida

auto = qtde_antes_abastecimento * km_percorrida

print(f"Consumo: {consumo} litros")

print(f"autonomia antes do abastecimento: {auto} Km")
