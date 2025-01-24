x = 1
a = 1
b = 3
c = 1
subt = 0
acum = 0
while c <= 5:
    subt = ((x/(pow(a,3)))-(x/(pow(b,3))))
    acum += subt
    a += 2
    b += 2
    c += 1
    print(acum)
