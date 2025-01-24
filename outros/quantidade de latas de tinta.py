H=float(input("Digite a altura, por favor!!: "))
R=float(input("Digite o raio, por favor!!: "))

area=(3.14*(R**2))+(2*3.14*R*H)

litro=area/3

qtde=litro/5

custo=qtde*50.00

print(f"O custo e de {custo} reais e a quantidade corresponde a {qtde}")
