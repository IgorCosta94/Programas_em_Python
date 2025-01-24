import json

dic = {}
con = 1
qtde = int(input(f"Qual a quantidade do {con}o.item ('0' para terminar)? "))
while qtde != 0:
    unidade = input("Qual a unidade? ")
    item = input("Qual o item? ")
    dic.update({'item' + str(con): {'qtde': qtde, 'unidade': unidade, 'item':item}})
    con += 1
    qtde = int(input(f"Qual a quantidade do {con}o.item? "))

nomearq = input("\nNome do arquivo")
with open(nomearq,'w', encoding = 'utf8') as arquivo:
    json.dump(dic, arquivo, indent = 4)
