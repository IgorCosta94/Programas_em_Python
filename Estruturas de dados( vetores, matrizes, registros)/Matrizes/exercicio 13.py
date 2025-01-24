m1 = [[1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11,12,13,14,15],
      [16,17,18,19,20],
      [21,22,23,24,25]]

#######AAAA###########################################################################

print("DIAGONAL PRINCIPAL")
for x in range(0,len(m1),1):
    for y in range(0,len(m1),1):
        if x == y and y == x:
            print(m1[x][y])
            
#######BBB############################################################################
            
print("TRIÃNGULO SUPERIOR")
for x in range(0,len(m1),1):
    for y in range(0,len(m1),1):
        if x > y and y < x:
            print(m1[x][y])
            
#######CCC############################################################################

print("TRIÃNGULO INFERIOR")
for x in range(0,len(m1),1):
    for y in range(0,len(m1),1):
        if y > x and x < y:
            print(m1[x][y])


#######DDD###########################################################################

print("TUDO EXCETO A DIAGONAL PRINCIPAL")
for x in range(0,len(m1),1):
    for y in range(0,len(m1),1):
        if x != y and y != x:
            print(m1[x][y])


#######EEE###########################################################################

print("DIAGONAL SECUNDÁRIA")
for x in range(0,len(m1),1):
    for y in range(0,len(m1),1):
        if (((x + y)+1) ==  len(m1)):
            print(m1[x][y])

#######FFF###########################################################################

print("TRIÂNGULO SUPERIOR À DIAGONAL SECUNDÁRIA")
for z in range(1, len(m1), 1):
    for a in range(1,len(m1),1):
        if ((z + a) == 5 ):
            print(m1[z][a])
        if (z + a) > 5 :
            print(m1[z][a])
                
#######GGG###########################################################################

print("TRIÂNGULO SUPERIOR À DIAGONAL SECUNDÁRIA")
for z in range(0, len(m1), 1):
    for a in range(0,len(m1),1):
        if ((z + a) < 4 ):
            print(m1[z][a])

#######HHH###########################################################################

print("TUDO EXCETO A DIAGONAL SECUNDÁRIA")
for x in range(0,len(m1),1):
    for y in range(0,len(m1),1):
        if (((x + y)+1) !=  len(m1)):
            print(m1[x][y])                
