listacompras = "mercado.txt"
item = input("Qual item incluir ('fim' para terminar)? ")
with open(listacompras,"a", encoding = 'utf8') as arquivo:
    while item != 'fim':
        arquivo.write(item +'\n')
        item = input("Qual item incluir? ")
