x = int(input("Informe um valor inteiro e positivo (DIGITE -1 PARA ENCERRAR) "))

comp = -1
comp2 = x

while(x != -1):
    if(x > comp):
        comp = x
    elif(x < comp2):
        comp2 = x
    print(f"Maio valor = {comp}\nMenor valor = {comp2}")
    x = int(input("Informe um valor inteiro e positivo (DIGITE -1 PARA ENCERRAR) "))


print(f"O maior valor digitado foi de {comp}\nO menor valor digitado foi de {comp2}")
