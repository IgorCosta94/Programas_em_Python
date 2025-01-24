ma = [['0','0','0','0'],
      ['0','0','0','0'],
      ['0','0','0','0'],
      ['0','0','0','0']]
ma[0][1] = "mm"
ma[3][2] = "nn"
ma[2][0] = "aa"
ma[0][3] = "bb"
ma[1][1] = "oo"
print(ma)
print()
for x in range(3,-1,-1):
    for y in range(0,3,1):
        n = ma[x-1][y]
        ma[x-1][y] = ma[x][y]
        ma[x][y] = n
        


print(ma)
