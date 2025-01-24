m1 = [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]

maiorL = 0
maiorC = 0

for x in range(0,5,1):
    for y in range(0,5,1):
        m1[x][y] = int(input("Digite um número inteiro: "))
        
for x in range(0,5,1):
    m2 = [0] * 10
    m3 = [0] * 10
    for y in range(0,5,1):
        if m1[x][y] > maiorL:
            m2[y] = m1[x][y]
        if m1[y][x] > maiorC:
            m3[y] = m1[y][x]
            
    print(f"Maior elemento da linha{x}: {m2}")
    print(f"Maior elemento da coluna{y}: {m3}")
