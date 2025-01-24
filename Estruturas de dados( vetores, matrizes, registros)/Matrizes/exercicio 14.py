m1 = [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]

for w in range(0, len(m1), 1):
    for x in range(0,len(m1), 1):
        m1[w][x] = int(input("INFORME UM NÚMERO INTEIRO:"))
##########################AAAAAAAAAAAAAAAAAAA########################################
for w in range(0, len(m1), 1):
    for x in range(0,len(m1), 1):
        y = m1[w][x]
        if w == 2:
            m1[w][x] = m1[4][x]
            m1[4][x] = y

##########################BBBBBBBBBBBBBBBBBBBB########################################
for w in range(0, len(m1), 1):
    for x in range(0,len(m1), 1):
        y = m1[x][w]
        if w == 1:
            m1[x][w] = m1[x][3]
            m1[x][3] = y


##########################CCCCCCCCCCCCCCCCCCCC########################################

for w in range(0, len(m1), 1):
    for x in range(0, len(m1), 1):
        y = m1[w][0]
        y1 = m1[w][1]
        if w == 0 and x == 4:
            m1[w][0] = m1[w][x]
            m1[w][x] = y
        if w == 1 and x == 3:
            m1[w][1] = m1[w][x]
            m1[w][x] = y1
        if w == 3 and x == 3:
            m1[w][1] = m1[w][x]
            m1[w][x] = y1
        if w == 4 and x == 4:
            m1[w][0] = m1[w][x]
            m1[w][x] = y

        
#########################IMPRESSÃO######################################################
print(m1)
 
    #[ [1, 2, 3, 4, 5],
      #[6, 7, 8, 9, 10],
     # [11,12,13,14,15],
     # [16,17,18,19,20],
     # [21,22,23,24,25]]
 
