Preco = float(input("Preço: "))
origem = int(input("Origem: "))

if(origem == 1):
    print(Preco," -Sul")
elif(origem == 2):
    print(Preco," -Norte")
elif(origem == 3):
    print(Preco," -Leste")
elif(origem == 4):
    print(Preco," -Oeste")
elif(origem == 7 or origem == 8 or origem == 9):
    print(Preco," -Sudeste")
elif(origem in range(10,21)):
    print(Preco," -Centro-Oeste")
elif(origem == 5 or origem == 6 or origem in range(25,31)):
    print(Preco," -Nordeste")
else:
    print(preco," -Impotado")
