abaste = "abastecimento.txt"
data = input("Informe a data do abastecimento (Digite -1 para terminar): ")

with open(abaste , 'a' , encoding = 'utf8') as arquivo:
    while data != '-1':
        arquivo.write(data +'\n')
        
        quilometragem = input("Informe a quilometragem do veículo: ")
        arquivo.write(quilometragem +'\n')
        
        tipo_combustivel = input("Informe o tipo de combustível: ")
        arquivo.write(tipo_combustivel +'\n')

        qtde_litros = input("Informe a quantidade de litros abastecidos: ")
        arquivo.write(qtde_litros +'\n')

        preco = input("Informe o preço do combustível: ")
        arquivo.write(preco +'\n')

        data = input("Informe a data do abastecimento:")


with open('abastecimento.txt', encoding = 'utf8') as arquivo:
    for w in arquivo:
        w = w.rstrip()
        print(w)
