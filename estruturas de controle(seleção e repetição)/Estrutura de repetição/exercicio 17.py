n1 = int(input("Informe o primeiro termo "))
n2 = int(input("Informe o segundo termo "))

x1 = 1
x2 = 1
print(f"F 1 = {x1}\nF 2 = {x2}")
for x in range(3,n1+1,1):
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    print(f"F {x} = {x3}")

for x in range(n1+1,n2+1,1):
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    print(f"F {x} = {x3}")

for x in range(n2+1,21+n1,1):
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    print(f"F {x} = {x3}")
