n = int(input("Digite um numero: "))
contador=0
for x in range(1,n+1,1):

    if(n%x==0):
        contador+=1

if (contador == 2 ):
    print(f"O numero {n} é primo")
else:
    print(f"O numero {n} não é primo")
