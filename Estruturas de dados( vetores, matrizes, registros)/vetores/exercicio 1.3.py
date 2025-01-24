v = [1,1,2,2,3,3,4,2,6,6]
cont = 0
n = int(input("Informe um número que deseja pesquisar no vetor: "))

for x in range(len(v)):
    if n == v[x]:
        print(f"Número encontrado na posição {x+1}")
        cont += 1
        
print(f"Foram encontradas {cont} um(a) ocorrência(s) desse número")
print(v)

        
    
