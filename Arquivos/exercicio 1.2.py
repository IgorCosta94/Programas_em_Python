import json

def leitura():
    dicionario = {}
    con = 1
    data = input("Informe a data do abastecimento (Digite -1 para terminar): ")

    while data != '-1':
        quilometragem = float(input("Informe a quilometragem do veículo: "))
        tipo_combustivel = input("Informe o tipo de combustível: ")
        qtde_litros = float(input("Informe a quantidade de litros abastecidos: "))
        preco = float(input("Informe o preço do combustível: "))

        dicionario.update({'Abastecimento' + str(con): {'Data':data,'Quilometrage':quilometragem,
                        'Tipo de combustivel':tipo_combustivel,'Quantidade de litros':qtde_litros,'Preço':preco}})
        con +=1
        data = input("Informe a data do abastecimento (Digite -1 para terminar): ")

    nomearq = input("\nNome do arquivo: ")
    with open(nomearq,'w', encoding = 'utf8') as arquivo:
        json.dump(dicionario, arquivo, indent = 4)

def exibicao():
    nomearq = input("\nNome do arquivo: ")
    with open(nomearq, encoding = 'utf8') as arquivo:
        dic = json.load(arquivo)

    print("Lista de abastecimentos")
    for chave, item in dic.items():
        print(f"{chave}: \nData: {item['Data']}\n"
              f"Quilometragem: {item['Quilometrage']}\n"
              f"Tipo de combustivel: {item['Tipo de combustivel']}\n"
              f"Quantidade de litros: {item['Quantidade de litros']}\n"
              f"Preço: {item['Preço']}\n") 

leitura()
exibicao()
