codigo = int(input("Digite o codigo do produto: "))

if codigo == 1:
    print("Alimento não perecível")
elif codigo in range(2,4):
    print("Alimento perecível")
elif codigo == 5 or codigo == 6:
    print("Vestuário")
elif codigo == 7:
    print("Higiene pessoal")
elif codigo in range(8,15):
    print("Limpeza e utensílios domésticos")
else:
        print("Codigo invalido")
