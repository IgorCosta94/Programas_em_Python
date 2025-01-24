#m1 = [[0 for _ in range(5)]  for _ in range(5)]
m1 = [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]
cont = 0
cont1 = 0
cont2 = 0
for x in range(0,5,1):
    for y in range(0,5,1):
        m1[x][y] = int(input("Digite um número inteiro: "))

for x in range(0,5,1):
    for y in range(0,5,1):
        cont1 += m1[y][x]
        cont2 += m1[x][y]
        if((m1[x][y] % 2) == 1):
            cont += m1[x][y]
print(m1)
print(f"Soma dos números ímpares: {cont}")
print(F"Soma dos números de cada coluna: {cont1}")
print(F"Soma dos números de cada linha: {cont2}")
