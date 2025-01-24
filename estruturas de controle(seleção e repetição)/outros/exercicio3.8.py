n=int(input("Digite um numero= "))
a=0
b=0
c=n
for x in range(1,21,1):
    n=int(input("Digite um numero= "))
    if(n>=a):
        b=n
        a=n
    else:
        if(n<c):
            c=n

print(f"O maior é {b}")
print(f"O menor é {c}")
