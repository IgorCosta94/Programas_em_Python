print("Lendo o arquivo linha a linha")
arquivo = open('a.txt','rt',encoding ='utf8')
linha = arquivo.readline()
while linha :
    print(linha, end = '')
    linha = arquivo.readline()
arquivo.close()
