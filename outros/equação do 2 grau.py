a=int(input("Digite o valor de A: "))
b=int(input("Digite o valor de B: "))
c=int(input("Digite o valor de C: "))

discriminante=(b**2)+(4*a*c)
raiz=discriminante**0.5
x1=(-b+discriminante)/(2*a)
x2=(-b-discriminante)/(2*a)

print(f"X1={x1}")
print(f"X2={x2}")
