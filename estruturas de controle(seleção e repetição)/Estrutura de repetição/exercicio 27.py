x = 2
y = 5
a = 500
b = 450
c = 1
subt = 0
acum = 0
while c <= 5:
    subt = ((x/a)-(y/b))
    acum += subt
    a = b - 50
    b = a - 50
    c += 1
    print(acum)
