x = 1
y = 1
a = 2
b = 4
c = 1
soma = 0
while c <= 5:
    acum = ((x/y) - (a/b))
    soma += acum
    
    x += 2
    y = x * x
    a += 2
    b = a * a

    c += 1

print(soma)
