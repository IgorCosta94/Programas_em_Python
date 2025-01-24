x = int(input("Informe um numero inteiro e positivo: "))
y = int(input("Informe um numero inteiro e positivo: "))

cont = 0
total = 0

for a in range(x,y+1,1):
    cont = 0
    for b in range(1,a+1,1):
        if a % b == 0:
            cont += 1
    if cont == 2:
        print(f"O numero {a} é primo")
        total +=1

print(f"O total de números primos entre {x} e {y} é de {total}")
        
