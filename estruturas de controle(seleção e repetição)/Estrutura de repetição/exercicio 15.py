x1 = int(input("Digite um numero inteiro = "))
x2 = int(input("Digite um numero inteiro = "))

arm = 0
contador = 0

for x in range(1,11,1):
    arm = x * x2
    if(x1 - arm == 0)or(x1 - arm == 1):
        print(f"O quociente da divisão entre {x1} e {x2} corresponde a {x}")
