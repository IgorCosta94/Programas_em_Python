print("Lendo o arquivo inteiro para uma única string")
arquivo = open('a.txt','rt',encoding ='utf8')
#texto = arquivo.read()
print(arquivo.read())
arquivo.close()
